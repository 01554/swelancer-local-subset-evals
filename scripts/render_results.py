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
    rows = list(csv.reader(open(path)))
    header, data = rows[0], rows[1:]
    cols = header[3:]
    out.append(f"## {env}")
    out.append("")
    out.append("| task | set | $ | " + " | ".join(cols) + " |")
    out.append("|---|---|---:|" + "---|" * len(cols))
    for r in data:
        cells = [SYM.get(v, v) for v in r[3:]]
        out.append(f"| {r[0]} | {r[1]} | {float(r[2]):,.0f} | " + " | ".join(cells) + " |")
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
    out.append("| **pass** | | | " + " | ".join(passes) + " |")
    out.append("| **earned** | | | " + " | ".join(moneys) + " |")
    out.append("| **timeouts** | | | " + " | ".join(touts) + " |")
    out.append("")

lb_lines = [
    "### Leaderboard",
    "",
    "| column | environment | pass | earned |",
    "|---|---|---:|---:|",
]
lb = sorted(summary, key=lambda s: (-s[4], -s[2]))
for env, col, p, n, m, t in lb:
    lb_lines.append(f"| {col} | {env} | {p}/{n} | ${m:,.0f} |")
lb_lines.append("")
out[4:4] = lb_lines

section = "\n".join([BEGIN, "## Results", ""] + out + [END])
readme = open("README.md").read()
assert BEGIN in readme and END in readme, "markers not found in README.md"
head, rest = readme.split(BEGIN, 1)
_, tail = rest.split(END, 1)
open("README.md", "w").write(head + section + tail)
print(f"README.md results section updated ({len(summary)} columns)")
