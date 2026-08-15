#!/usr/bin/env python3
"""Render results/*.csv into the README.md results section.

Replaces everything between the RESULTS:BEGIN / RESULTS:END markers.
Cell vocabulary: pass / fail / timeout / running / not_run (or empty).
Run from the repo root: python3 scripts/render_results.py
"""
import csv
import glob
import os

SYM = {"pass": "✅", "fail": "❌", "timeout": "⏱️", "running": "🔄", "not_run": "—", "": "·"}
BEGIN, END = "<!-- RESULTS:BEGIN -->", "<!-- RESULTS:END -->"

out = [
    "_Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this section._",
    "",
    "✅ pass ❌ fail ⏱️ timeout (rollout cap hit, unfinished) 🔄 running — not run",
    "",
]

summary = []
for path in sorted(glob.glob("results/*.csv")):
    env = os.path.basename(path)[:-4]
    if env == "columns":  # metadata, not an environment
        continue
    rows = list(csv.reader(open(path)))
    header, data = rows[0], rows[1:]
    cols = header[3:]
    out.append(f"## {env}")
    out.append("")
    out.append("| task | $ | " + " | ".join(cols) + " |")
    out.append("|---|---:|" + "---|" * len(cols))
    for r in data:
        cells = [SYM.get(v, v) for v in r[3:]]
        out.append(f"| {r[0]} | {float(r[2]):,.0f} | " + " | ".join(cells) + " |")
    passes, moneys, touts = [], [], []
    for i in range(len(cols)):
        p = sum(1 for r in data if r[3 + i] == "pass")
        t = sum(1 for r in data if r[3 + i] == "timeout")
        m = sum(float(r[2]) for r in data if r[3 + i] == "pass")
        n = sum(1 for r in data if r[3 + i] in ("pass", "fail", "timeout"))
        passes.append(f"**{p}/{n}**")
        moneys.append(f"${m:,.0f}")
        touts.append(str(t) if t else "0")
        summary.append((env, cols[i], p, n, m, t))
    out.append("| **pass** | | " + " | ".join(passes) + " |")
    out.append("| **earned** | | " + " | ".join(moneys) + " |")
    out.append("| **timeouts** | | " + " | ".join(touts) + " |")
    out.append("")

meta = {}
if os.path.exists("results/columns.csv"):
    for r in csv.DictReader(open("results/columns.csv")):
        meta[r["column"]] = r

lb_lines = [
    "### Leaderboard",
    "",
    "| column | agent | environment | pass | earned | avg min/task |",
    "|---|---|---|---:|---:|---:|",
]
lb = sorted(summary, key=lambda s: (-s[4], -s[2]))
for env, col, p, n, m, t in lb:
    mrow = meta.get(col, {})
    g = lambda k: mrow.get(k) or "?"
    lb_lines.append(
        f"| {col} | {g('agent')} | {env} | {p}/{n} | ${m:,.0f} | {g('avg_task_min')} |"
    )
lb_lines.append("")
out[4:4] = lb_lines

# per-run conditions table -> environments.md (same rows as the leaderboard)
env_lines = [
    "| column | agent | environment | ctx | sampling | avg min/task |",
    "|---|---|---|---|---|---:|",
]
for env, col, p, n, m, t in lb:
    mrow = meta.get(col, {})
    g = lambda k: mrow.get(k) or "?"
    env_lines.append(
        f"| {col} | {g('agent')} | {env} | {g('ctx')} | {g('sampling')} | {g('avg_task_min')} |"
    )
EBEGIN, EEND = "<!-- RUNCONDITIONS:BEGIN -->", "<!-- RUNCONDITIONS:END -->"
envmd = open("environments.md").read()
if EBEGIN in envmd and EEND in envmd:
    head, rest = envmd.split(EBEGIN, 1)
    _, tail = rest.split(EEND, 1)
    envmd = head + "\n".join([EBEGIN] + env_lines + [EEND]) + tail
    open("environments.md", "w").write(envmd)
    print("environments.md run-conditions table updated")
else:
    print("WARNING: RUNCONDITIONS markers missing in environments.md")

section = "\n".join([BEGIN, "## Results", ""] + out + [END])
readme = open("README.md").read()
assert BEGIN in readme and END in readme, "markers not found in README.md"
head, rest = readme.split(BEGIN, 1)
_, tail = rest.split(END, 1)
open("README.md", "w").write(head + section + tail)
print(f"README.md results section updated ({len(summary)} columns)")
