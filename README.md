# swelancer-local-subset-evals

SWE-Lancer (IC SWE, Diamond) subset evaluations of local models on local
hardware. This repo is the new home of the eval kit that previously lived in
[`kimi-k3-gguf-prune/evals`](https://github.com/01554/kimi-k3-gguf-prune/tree/main/evals)
— task selection rules, per-task results, and the replication kit. History
prior to the split remains in the old repo.

<!-- RESULTS:BEGIN -->
## Results

_Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this section._

✅ pass ❌ fail ⏱️ timeout (rollout cap hit, unfinished) 🔄 running — not run

### Leaderboard

| column | agent | environment | pass | earned | avg min/task |
|---|---|---|---:|---:|---:|
| qwen38_27b_bf16_pi_promptv1 | pi | rtx6000-96gb | 17/24 | $48,000 | 43.8 |
| kimik3_streamed896_iq2xxs_18000s | Kimi Code CLI | macstudio-512gb | 7/11 | $35,750 | ? |
| kimik3_reap640_iq1s | Kimi Code CLI | macstudio-512gb | 6/10 | $35,500 | ? |
| kimik3_reap576_iq2xxs | Kimi Code CLI | macstudio-512gb | 13/24 | $19,000 | ? |
| kimik3_streamed896_iq2xxs_18000s_attempt2 | Kimi Code CLI | macstudio-512gb | 3/3 | $10,000 | ? |
| gemma4_31b_nvfp4_pi_promptv1 | pi | rtx6000-96gb | 7/24 | $9,250 | 6.2 |
| qwen38_a95b_udiq1s_10800s | ? | macstudio-512gb | 5/6 | $7,000 | ? |
| k27_q2_2bit | Kimi Code CLI | macstudio-512gb | 3/24 | $2,000 | ? |
| qwen38_reap256_iq1s_10800s | ? | macstudio-512gb | 3/8 | $2,000 | ? |

## macstudio-512gb

| task | $ | k27_q2_2bit | kimik3_reap640_iq1s | kimik3_reap576_iq2xxs | kimik3_streamed896_iq2xxs_18000s | kimik3_streamed896_iq2xxs_18000s_attempt2 | qwen38_a95b_udiq1s_10800s | qwen38_reap256_iq1s_10800s |
|---|---:|---|---|---|---|---|---|---|
| 28096_836 | 500 | ✅ | ✅ | ✅ | ✅ | · | ❌ | ✅ |
| 18827_741 | 1,000 | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ |
| 29618_781 | 500 | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ |
| 14294 | 4,000 | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| 24508_791 | 1,000 | ❌ | ✅ | ✅ | ✅ | · | ✅ | ❌ |
| 15815_1 | 4,000 | ❌ | ❌ | ✅ | ❌ | ✅ | pending | ❌ |
| 27353_776 | 500 | ❌ | ✅ | ❌ | ✅ | · | ✅ | ❌ |
| 15925 | 2,000 | ❌ | ❌ | ✅ | ❌ | ✅ | pending | ❌ |
| 29916_609 | 500 | ❌ | ❌ | ❌ | ❌ | · | · | · |
| 6883 | 32,000 | ❌ | ✅ | ❌ | ✅ | · | · | · |
| 43395_530 | 250 | ❌ | 🔄 | ✅ | ✅ | · | · | · |
| 25901_945 | 2,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 40259_1089 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 18746_833 | 1,000 | ❌ | 🔄 | ❌ | — | · | · | · |
| 4324 | 2,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 44429_1100 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 40208_1108 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 44618_1007 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 19132_872 | 1,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 41885_1134 | 500 | ❌ | 🔄 | ✅ | — | · | · | · |
| 50064_846 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 50314_790 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 37688_441 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 44040_470 | 250 | ❌ | 🔄 | ✅ | — | · | · | · |
| **pass** | | **3/24** | **6/10** | **13/24** | **7/11** | **3/3** | **5/6** | **3/8** |
| **earned** | | $2,000 | $35,500 | $19,000 | $35,750 | $10,000 | $7,000 | $2,000 |
| **timeouts** | | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## rtx6000-96gb

| task | $ | gemma4_31b_nvfp4_pi_promptv1 | qwen38_27b_bf16_pi_promptv1 |
|---|---:|---|---|
| 28096_836 | 500 | ✅ | ✅ |
| 18827_741 | 1,000 | ❌ | ✅ |
| 29618_781 | 500 | ✅ | ✅ |
| 14294 | 4,000 | ✅ | ✅ |
| 24508_791 | 1,000 | ✅ | ✅ |
| 15815_1 | 4,000 | ❌ | ✅ |
| 27353_776 | 500 | ❌ | ❌ |
| 15925 | 2,000 | ✅ | ❌ |
| 29916_609 | 500 | ❌ | ✅ |
| 6883 | 32,000 | ❌ | ✅ |
| 43395_530 | 250 | ❌ | ❌ |
| 25901_945 | 2,000 | ❌ | ❌ |
| 40259_1089 | 500 | ❌ | ✅ |
| 18746_833 | 1,000 | ❌ | ✅ |
| 4324 | 2,000 | ❌ | ❌ |
| 44429_1100 | 250 | ❌ | ✅ |
| 40208_1108 | 500 | ❌ | ✅ |
| 44618_1007 | 250 | ✅ | ❌ |
| 19132_872 | 1,000 | ✅ | ✅ |
| 41885_1134 | 500 | ❌ | ❌ |
| 50064_846 | 250 | ❌ | ✅ |
| 50314_790 | 250 | ❌ | ✅ |
| 37688_441 | 500 | ❌ | ✅ |
| 44040_470 | 250 | ❌ | ✅ |
| **pass** | | **7/24** | **17/24** |
| **earned** | | $9,250 | $48,000 |
| **timeouts** | | 0 | 0 |

<!-- RESULTS:END -->

- Per-task results, split by execution environment: [`results/`](results/)
- Environment / speed table (read before comparing across CSVs): [`environments.md`](environments.md)
- 各タスクの日本語解説: [`TASKS.ja.md`](TASKS.ja.md)
- Task selection rules and common conditions: [`SELECTION.md`](SELECTION.md)
- How to re-run any cell on your hardware: [`REPLICATION.md`](REPLICATION.md)

**Agent policy**: to judge real-world usability, rollouts use each model vendor's official CLI agent where one exists, `pi` where none does, and both when time permits.

Column naming: `<model>_<quant>_<agent/cli>_<condition labels>`; the rollout
cap (10800 s unless suffixed) and any prompt deviation (e.g. `promptv1`) are
part of the label. One attempt per task; never re-roll failures.

Cell values: `pass` / `fail` (finished, graded incorrect) / `timeout` (rollout cap hit before the agent finished) / `running` / `not_run`. Older macstudio columns predate the fail-vs-timeout distinction; per the source repo, 8 of 10 reap576 battle16 fails were cap-terminated and will be reclassified as data becomes available.
