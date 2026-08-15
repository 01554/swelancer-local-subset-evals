# swelancer-local-subset-evals

SWE-Lancer (IC SWE, Diamond) subset evaluations of local models on local
hardware. This repo is the new home of the eval kit that previously lived in
[`kimi-k3-gguf-prune/evals`](https://github.com/01554/kimi-k3-gguf-prune/tree/main/evals)
— task selection rules, per-task results, and the replication kit. History
prior to the split remains in the old repo.

<!-- RESULTS:BEGIN -->
## Results

_Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this section._

✅ pass ❌ fail ⏱️ timeout (rollout cap hit, unfinished) 🔄 running — not run · in metadata rows, - = not recorded / unrecoverable (未取得), ≥N = N timeouts verified, rest unaudited

### Leaderboard

| column | agent | environment | pass | earned | avg min/task (probe3 / all24) |
|---|---|---|---:|---:|---:|
| qwen38_27b_bf16_pi_promptv1 | pi | rtx6000-96gb | 17/24 | $48,000 | 15.0 / 43.8 |
| kimik3_reap640_iq1s | Kimi Code CLI | macstudio-512gb | 7/18 | $35,750 | - / - |
| kimik3_streamed896_iq2xxs_18000s | Kimi Code CLI | macstudio-512gb | 7/11 | $35,750 | 185.0 / - |
| kimik3_reap576_iq2xxs | Kimi Code CLI | macstudio-512gb | 13/24 | $19,000 | - / - |
| kimik3_streamed896_iq2xxs_18000s_attempt2 | Kimi Code CLI | macstudio-512gb | 3/3 | $10,000 | - / - |
| gemma4_31b_nvfp4_pi_promptv1 | pi | rtx6000-96gb | 7/24 | $9,250 | 4.3 / 6.2 |
| qwen38_a95b_udiq1s_10800s | Qwen Code CLI 0.21.10-0.21.11 | macstudio-512gb | 5/6 | $7,000 | 130.3 / - |
| k27_q2_2bit | Kimi Code CLI | macstudio-512gb | 3/24 | $2,000 | - / - |
| qwen38_reap256_iq1s_10800s | Qwen Code CLI 0.21.11 | macstudio-512gb | 3/8 | $2,000 | 88.0 / - |

Task sets (details in [SELECTION.md](SELECTION.md)): **probe** = 3 sanity tasks every build should pass · **differential** = 5 tasks the K2.7 baseline failed · **battle16** = 16 hard tasks, also K2.7-failed, selected by shortest description

_Per-task cells live in [`results/*.csv`](results/); tables below aggregate by set._

## macstudio-512gb

| set | k27_q2_2bit | kimik3_reap640_iq1s | kimik3_reap576_iq2xxs | kimik3_streamed896_iq2xxs_18000s | kimik3_streamed896_iq2xxs_18000s_attempt2 | qwen38_a95b_udiq1s_10800s | qwen38_reap256_iq1s_10800s |
|---|---|---|---|---|---|---|---|
| probe (3) | 3/3 | 3/3 | 3/3 | 3/3 | — | 2/3 | 3/3 |
| differential (5) | 0/5 | 2/5 | 4/5 | 2/5 | 3/3 | 3/3 | 0/5 |
| battle16 (16) | 0/16 | 2/10 | 6/16 | 2/3 | — | — | — |
| **total pass** | **3/24** | **7/18** | **13/24** | **7/11** | **3/3** | **5/6** | **3/8** |
| **earned** | $2,000 | $35,750 | $19,000 | $35,750 | $10,000 | $7,000 | $2,000 |
| **timeouts** | - | ≥8 | ≥8 | ≥1 | - | 0 | 0 |

## rtx6000-96gb

| set | gemma4_31b_nvfp4_pi_promptv1 | qwen38_27b_bf16_pi_promptv1 |
|---|---|---|
| probe (3) | 2/3 | 3/3 |
| differential (5) | 3/5 | 3/5 |
| battle16 (16) | 2/16 | 11/16 |
| **total pass** | **7/24** | **17/24** |
| **earned** | $9,250 | $48,000 |
| **timeouts** | 0 | 0 |

<!-- RESULTS:END -->

- Per-task results, split by execution environment: [`results/`](results/)
- Environment / speed table (read before comparing across CSVs): [`environments.md`](environments.md)
- Per-model commentary (behavior profiles): [`models/`](models/)
- Per-task commentary: [`TASKS.md`](TASKS.md) (English) / [`TASKS.ja.md`](TASKS.ja.md) (日本語)
- Task selection rules and common conditions: [`SELECTION.md`](SELECTION.md)
- How to re-run any cell on your hardware: [`REPLICATION.md`](REPLICATION.md)

**Agent policy**: to judge real-world usability, rollouts use each model vendor's official CLI agent where one exists, `pi` where none does, and both when time permits.

Column naming: `<model>_<quant>_<agent/cli>_<condition labels>`; the rollout
cap (10800 s unless suffixed) and any prompt deviation (e.g. `promptv1`) are
part of the label. One attempt per task; never re-roll failures.

Cell values: `pass` / `fail` (finished, graded incorrect) / `timeout` (rollout cap hit before the agent finished) / `running` / `not_run`. Older macstudio columns predate the fail-vs-timeout distinction; per the source repo, 8 of 10 reap576 battle16 fails were cap-terminated; those cells may be reclassified if per-task data is published.
