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
    "✅ pass ❌ fail ⏱️ timeout (rollout cap hit, unfinished) 🔄 running — not run · in metadata rows, - = not recorded / unrecoverable (未取得), ≥N = N timeouts verified, rest unaudited",
    "",
    "Task sets (details in [SELECTION.md](SELECTION.md)): **probe** = the 3 smallest-input tasks the K2.7 baseline solved (does-it-still-work gate) · "
    "**differential** = the 5 smallest-input tasks K2.7 failed · **battle16** = 16 more K2.7-failed tasks, "
    "selected by shortest title+description",
    "",
    "_Per-task cells live in [`results/*.csv`](results/); tables below aggregate by set._",
    "",
]

meta = {}
if os.path.exists("results/columns.csv"):
    for r in csv.DictReader(open("results/columns.csv")):
        meta[r["column"]] = r

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
    out.append("| set | " + " | ".join(cols) + " |")
    out.append("|---|" + "---|" * len(cols))
    for s in ("probe", "differential", "battle16"):
        cells = []
        srows = [r for r in data if r[1] == s]
        for i in range(len(cols)):
            p = sum(1 for r in srows if r[3 + i] == "pass")
            n = sum(1 for r in srows if r[3 + i] in ("pass", "fail", "timeout"))
            cells.append(f"{p}/{n}" if n else "—")
        out.append(f"| {s} ({len(srows)}) | " + " | ".join(cells) + " |")
    passes, moneys, touts = [], [], []
    for i in range(len(cols)):
        p = sum(1 for r in data if r[3 + i] == "pass")
        t = sum(1 for r in data if r[3 + i] == "timeout")
        m = sum(float(r[2]) for r in data if r[3 + i] == "pass")
        n = sum(1 for r in data if r[3 + i] in ("pass", "fail", "timeout"))
        passes.append(f"**{p}/{n}**")
        moneys.append(f"${m:,.0f}")
        # only claim a timeout count for columns whose run recorded the
        # fail/timeout distinction; otherwise it is unknown, not zero
        aware = meta.get(cols[i], {}).get("timeout_aware")
        touts.append(str(t) if aware else (f"\u2265{t}" if t else "-"))
        summary.append((env, cols[i], p, n, m, t))
    out.append("| **total pass** | " + " | ".join(passes) + " |")
    out.append("| **earned** | " + " | ".join(moneys) + " |")
    out.append("| **timeouts** | " + " | ".join(touts) + " |")
    out.append("")

lb_lines = [
    "### Leaderboard",
    "",
    "| column | agent | environment | pass | earned | avg min/task (probe3 / all24) |",
    "|---|---|---|---:|---:|---:|",
]
lb = sorted(summary, key=lambda s: (-s[4], -s[2]))
for env, col, p, n, m, t in lb:
    mrow = meta.get(col, {})
    g = lambda k: mrow.get(k) or "-"
    lb_lines.append(
        f"| {col} | {g('agent')} | {env} | {p}/{n} | ${m:,.0f} | {g('avg_min_probe3')} / {g('avg_min_all24')} |"
    )
lb_lines.append("")
out[4:4] = lb_lines

# per-run conditions table -> environments.md (same rows as the leaderboard)
env_lines = [
    "| column | agent | environment | ctx | sampling | avg min/task probe3 | avg min/task all24 |",
    "|---|---|---|---|---|---:|---:|",
]
for env, col, p, n, m, t in lb:
    mrow = meta.get(col, {})
    g = lambda k: mrow.get(k) or "-"
    env_lines.append(
        f"| {col} | {g('agent')} | {env} | {g('ctx')} | {g('sampling')} | {g('avg_min_probe3')} | {g('avg_min_all24')} |"
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
