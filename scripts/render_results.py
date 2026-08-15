#!/usr/bin/env python3
"""Render results/*.csv into the README.md results section.

Replaces everything between the RESULTS:BEGIN / RESULTS:END markers.
Cell vocabulary: pass / fail / timeout / running / not_run (or empty).
Run from the repo root: python3 scripts/render_results.py
"""
import csv
import glob
import os

BEGIN, END = "<!-- RESULTS:BEGIN -->", "<!-- RESULTS:END -->"
SETS = ("sanity3", "hard5", "extended16")

out = [
    "_Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this section._",
    "",
    "CSV cell vocabulary: `pass` / `fail` (finished, graded wrong) / `timeout` (rollout cap hit, unfinished) / `running` / `not_run`. In the tables below: - = not recorded / unrecoverable (未取得) · ≥N = N timeouts verified, rest unaudited.",
    "",
    "Task sets (details in [SELECTION.md](SELECTION.md)): **sanity3** = the 3 smallest-input tasks the K2.7 baseline solved (does-it-still-work gate) · "
    "**hard5** = the 5 smallest-input tasks K2.7 failed · **extended16** = 16 more K2.7-failed tasks, "
    "selected by shortest title+description",
    "",
    "_Per-task cells live in [`results/*.csv`](results/); tables below aggregate by set. "
    "Arms are only ranked against arms that ran the same work: incomplete runs are listed unranked with their coverage._",
    "",
]

meta = {}
if os.path.exists("results/columns.csv"):
    for r in csv.DictReader(open("results/columns.csv")):
        meta[r["column"]] = r

def disp(col):
    """Linked short name for boards: one hop to the models/ commentary
    page (which carries the HF link), falling back to the HF url, then to
    the raw id. Raw ids stay in the CSVs and the run-conditions table."""
    m = meta.get(col, {})
    target = m.get("page") or m.get("url")
    if m.get("display") and target:
        return f"[{m['display']}]({target})"
    return col

summary = []   # (env, col, passes, decided, money, timeouts)
setstat = {}   # (env, col) -> {set: (passes, decided, money, set_size)}
env_size = {}  # env -> total tasks in its CSV
env_tables = []
for path in sorted(glob.glob("results/*.csv")):
    env = os.path.basename(path)[:-4]
    if env == "columns":  # metadata, not an environment
        continue
    rows = list(csv.reader(open(path)))
    header, data = rows[0], rows[1:]
    cols = header[3:]
    env_size[env] = len(data)
    env_tables.append(f"## {env}")
    env_tables.append("")
    env_tables.append("| set | " + " | ".join(cols) + " |")
    env_tables.append("|---|" + "---|" * len(cols))
    for s in SETS:
        cells = []
        srows = [r for r in data if r[1] == s]
        for i in range(len(cols)):
            p = sum(1 for r in srows if r[3 + i] == "pass")
            n = sum(1 for r in srows if r[3 + i] in ("pass", "fail", "timeout"))
            m = sum(float(r[2]) for r in srows if r[3 + i] == "pass")
            setstat.setdefault((env, cols[i]), {})[s] = (p, n, m, len(srows))
            cells.append(f"{p}/{n}" if n else "—")
        env_tables.append(f"| {s} ({len(srows)}) | " + " | ".join(cells) + " |")
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
        touts.append(str(t) if aware else (f"≥{t}" if t else "-"))
        summary.append((env, cols[i], p, n, m, t))
    env_tables.append("| **total pass** | " + " | ".join(passes) + " |")
    env_tables.append("| **earned** | " + " | ".join(moneys) + " |")
    env_tables.append("| **timeouts** | " + " | ".join(touts) + " |")
    env_tables.append("")

# ---- boards ------------------------------------------------------------
lb_lines = []
complete = [s for s in summary if s[3] == env_size[s[0]]]
if complete:
    lb_lines += [
        "### Overall — arms that ran all 24 tasks",
        "",
        "| column | agent | environment | pass | earned | avg min/task |",
        "|---|---|---|---:|---:|---:|",
    ]
    for env, col, p, n, m, t in sorted(complete, key=lambda s: (-s[4], -s[2])):
        mrow = meta.get(col, {})
        g = lambda k: mrow.get(k) or "-"
        lb_lines.append(
            f"| {disp(col)} | {g('agent')} | {env} | {p}/{n} | ${m:,.0f} | {g('avg_min_all24')} |"
        )
    lb_lines.append("")

for s in SETS:
    board = []
    for (env, col), st in setstat.items():
        p, n, m, size = st[s]
        if size and n == size:
            board.append((env, col, p, n, m))
    if not board:
        continue
    size = board[0][3]
    avg_key = f"avg_min_{s}"
    has_avg = any(meta.get(col, {}).get(avg_key) for _, col, *_ in board)
    lb_lines += [
        f"#### {s} ({size} tasks) — arms that finished the set",
        "",
        "| column | environment | pass | earned |" + (" avg min/task |" if has_avg else ""),
        "|---|---|---:|---:|" + ("---:|" if has_avg else ""),
    ]
    for env, col, p, n, m in sorted(board, key=lambda b: (-b[2], -b[4])):
        row = f"| {disp(col)} | {env} | {p}/{n} | ${m:,.0f} |"
        if has_avg:
            row += f" {meta.get(col, {}).get(avg_key) or '-'} |"
        lb_lines.append(row)
    lb_lines.append("")

partial = [s for s in summary if s[3] != env_size[s[0]]]
if partial:
    lb_lines += [
        "### Incomplete runs — not ranked (cells: pass/decided of set size)",
        "",
        "| column | environment | sanity3 | hard5 | extended16 | earned so far |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for env, col, p, n, m, t in sorted(partial, key=lambda s: (-s[4], -s[2])):
        st = setstat[(env, col)]
        cells = []
        for s in SETS:
            sp, sn, sm, size = st[s]
            cells.append(f"{sp}/{sn} of {size}" if sn else "—")
        lb_lines.append(f"| {disp(col)} | {env} | " + " | ".join(cells) + f" | ${m:,.0f} |")
    lb_lines.append("")

out += lb_lines + env_tables

# per-run conditions table -> environments.md (same rows as the leaderboard)
env_lines = [
    "| column | agent | environment | ctx | sampling | avg min/task sanity3 | avg min/task all24 |",
    "|---|---|---|---|---|---:|---:|",
]
for env, col, p, n, m, t in sorted(summary, key=lambda s: (-s[4], -s[2])):
    mrow = meta.get(col, {})
    g = lambda k: mrow.get(k) or "-"
    env_lines.append(
        f"| {col} | {g('agent')} | {env} | {g('ctx')} | {g('sampling')} | {g('avg_min_sanity3')} | {g('avg_min_all24')} |"
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
