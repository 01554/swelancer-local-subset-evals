# swelancer-local-subset-evals

SWE-Lancer (IC SWE, Diamond) subset evaluations of local models on local
hardware. This repo is the new home of the eval kit that previously lived in
[`kimi-k3-gguf-prune/evals`](https://github.com/01554/kimi-k3-gguf-prune/tree/main/evals)
— task selection rules, per-task results, and the replication kit. History
prior to the split remains in the old repo.

- **Human-readable results table: [`RESULTS.md`](RESULTS.md)** (auto-generated — regenerate with `python3 scripts/render_results.py`)
- Per-task results, split by execution environment: [`results/`](results/)
- Environment / speed table (read before comparing across CSVs): [`environments.md`](environments.md)
- Task selection rules and common conditions: [`SELECTION.md`](SELECTION.md)
- How to re-run any cell on your hardware: [`REPLICATION.md`](REPLICATION.md)

Column naming: `<model>_<quant>_<agent/cli>_<condition labels>`; the rollout
cap (10800 s unless suffixed) and any prompt deviation (e.g. `promptv1`) are
part of the label. One attempt per task; never re-roll failures.

Cell values: `pass` / `fail` (finished, graded incorrect) / `timeout` (rollout cap hit before the agent finished) / `running` / `not_run`. Older macstudio columns predate the fail-vs-timeout distinction; per the source repo, 8 of 10 reap576 battle16 fails were cap-terminated and will be reclassified as data becomes available.
