# swelancer-local-subset-evals

SWE-Lancer (IC SWE, Diamond) subset evaluations of local models on local
hardware. This repo is the new home of the eval kit that previously lived in
[`kimi-k3-gguf-prune/evals`](https://github.com/01554/kimi-k3-gguf-prune/tree/main/evals)
— task selection rules, per-task results, and the replication kit. History
prior to the split remains in the old repo.

<!-- RESULTS:BEGIN -->
## Results

_Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this section._

CSV cell vocabulary: `pass` / `fail` (finished, graded wrong) / `timeout` (rollout cap hit, unfinished) / `running` / `not_run`. In the tables below: - = not recorded / unrecoverable (未取得) · ≥N = N timeouts verified, rest unaudited.

Task sets (details in [SELECTION.md](SELECTION.md)): **sanity3** = the 3 smallest-input tasks the K2.7 baseline solved (does-it-still-work gate) · **hard5** = the 5 smallest-input tasks K2.7 failed · **extended16** = 16 more K2.7-failed tasks, selected by shortest title+description

_Per-task cells live in [`results/*.csv`](results/); tables below aggregate by set. Arms are only ranked against arms that ran the same work: incomplete runs are listed unranked with their coverage._

### Overall — arms that ran all 24 tasks

| column | agent | environment | pass | earned | avg min/task |
|---|---|---|---:|---:|---:|
| [Qwen3.8-27B BF16 (Qwen Code)](models/qwen38-27b-bf16-qwencode.md) | Qwen Code CLI | rtx6000-96gb | 19/24 | $53,750 | 29.1 |
| [Qwen3.8-27B BF16](models/qwen38-27b-bf16-pi.md) | pi | rtx6000-96gb | 17/24 | $48,000 | 43.8 |
| [K3 REAP576 IQ2_XXS](models/kimik3-reap576-iq2xxs-kimicode.md) | Kimi Code CLI | macstudio-512gb | 13/24 | $19,000 | 140.9 |
| [Gemma-4-31B NVFP4](models/gemma4-31b-nvfp4-pi.md) | pi | rtx6000-96gb | 7/24 | $9,250 | 6.2 |
| [K2.7-Code Q2 (baseline)](models/k27-q2-toolaware.md) | custom tool-aware solver (pre-CLI) | macstudio-512gb | 3/24 | $2,000 | 72.9 |

#### sanity3 (3 tasks) — 3 tasks the K2.7 baseline solved (smallest inputs) — does-it-still-work gate

| column | environment | pass | earned | avg min/task |
|---|---|---:|---:|---:|
| [K2.7-Code Q2 (baseline)](models/k27-q2-toolaware.md) | macstudio-512gb | 3/3 | $2,000 | 14.1 |
| [K3 REAP640 IQ1_S](models/kimik3-reap640-iq1s-kimicode.md) | macstudio-512gb | 3/3 | $2,000 | 67.7 |
| [K3 REAP576 IQ2_XXS](models/kimik3-reap576-iq2xxs-kimicode.md) | macstudio-512gb | 3/3 | $2,000 | 63.9 |
| [K3 full-896 streamed (cap 18000s)](models/kimik3-896-iq2xxs-streamed-kimicode.md) | macstudio-512gb | 3/3 | $2,000 | 185.0 |
| [Qwen3.8 REAP-256GB](models/qwen38-reap256-iq1s-qwencode.md) | macstudio-512gb | 3/3 | $2,000 | 88.0 |
| [Qwen3.8 REAP-512GB](models/qwen38-reap512-iq2xxs-qwencode.md) | macstudio-512gb | 3/3 | $2,000 | 96.0 |
| [Qwen3.8-27B BF16](models/qwen38-27b-bf16-pi.md) | rtx6000-96gb | 3/3 | $2,000 | 15.0 |
| [Qwen3.8-27B BF16 (Qwen Code)](models/qwen38-27b-bf16-qwencode.md) | rtx6000-96gb | 3/3 | $2,000 | 13.7 |
| [Qwen3.8-2.4T UD-IQ1_S streamed](models/qwen38-a95b-udiq1s-qwencode.md) | macstudio-512gb | 2/3 | $1,500 | 130.3 |
| [Gemma-4-31B NVFP4](models/gemma4-31b-nvfp4-pi.md) | rtx6000-96gb | 2/3 | $1,000 | 4.3 |
| [Qwen3.8 REAP-512GB (no counter-note)](models/qwen38-reap512-iq2xxs-qwencode.md) | macstudio-512gb | 1/3 | $500 | 24.3 |

#### hard5 (5 tasks) — the 5 smallest tasks the K2.7 baseline failed

| column | environment | pass | earned | avg min/task |
|---|---|---:|---:|---:|
| [Qwen3.8-2.4T UD-IQ1_S streamed](models/qwen38-a95b-udiq1s-qwencode.md) | macstudio-512gb | 5/5 | $11,500 | 140.0 |
| [Qwen3.8-27B BF16 (Qwen Code)](models/qwen38-27b-bf16-qwencode.md) | rtx6000-96gb | 5/5 | $11,500 | 31.2 |
| [K3 REAP576 IQ2_XXS](models/kimik3-reap576-iq2xxs-kimicode.md) | macstudio-512gb | 4/5 | $11,000 | 134.5 |
| [Qwen3.8-27B BF16](models/qwen38-27b-bf16-pi.md) | rtx6000-96gb | 3/5 | $9,000 | 48.0 |
| [Gemma-4-31B NVFP4](models/gemma4-31b-nvfp4-pi.md) | rtx6000-96gb | 3/5 | $7,000 | 6.6 |
| [K3 REAP640 IQ1_S](models/kimik3-reap640-iq1s-kimicode.md) | macstudio-512gb | 2/5 | $1,500 | 167.3 |
| [K3 full-896 streamed (cap 18000s)](models/kimik3-896-iq2xxs-streamed-kimicode.md) | macstudio-512gb | 2/5 | $1,500 | - |
| [K2.7-Code Q2 (baseline)](models/k27-q2-toolaware.md) | macstudio-512gb | 0/5 | $0 | 27.7 |
| [Qwen3.8 REAP-256GB](models/qwen38-reap256-iq1s-qwencode.md) | macstudio-512gb | 0/5 | $0 | 96.0 |

#### extended16 (16 tasks) — 16 more K2.7-failed tasks (shortest problem statements)

| column | environment | pass | earned | avg min/task |
|---|---|---:|---:|---:|
| [Qwen3.8-27B BF16 (Qwen Code)](models/qwen38-27b-bf16-qwencode.md) | rtx6000-96gb | 11/16 | $40,250 | 31.4 |
| [Qwen3.8-27B BF16](models/qwen38-27b-bf16-pi.md) | rtx6000-96gb | 11/16 | $37,000 | 47.9 |
| [K3 REAP576 IQ2_XXS](models/kimik3-reap576-iq2xxs-kimicode.md) | macstudio-512gb | 6/16 | $6,000 | 157.4 |
| [Gemma-4-31B NVFP4](models/gemma4-31b-nvfp4-pi.md) | rtx6000-96gb | 2/16 | $1,250 | 6.6 |
| [K2.7-Code Q2 (baseline)](models/k27-q2-toolaware.md) | macstudio-512gb | 0/16 | $0 | 98.0 |

### Incomplete runs — not ranked (cells: pass/decided of set size)

| column | environment | sanity3 | hard5 | extended16 | earned so far |
|---|---|---:|---:|---:|---:|
| [K3 REAP640 IQ1_S](models/kimik3-reap640-iq1s-kimicode.md) | macstudio-512gb | 3/3 of 3 | 2/5 of 5 | 2/10 of 16 | $35,750 |
| [K3 full-896 streamed (cap 18000s)](models/kimik3-896-iq2xxs-streamed-kimicode.md) | macstudio-512gb | 3/3 of 3 | 2/5 of 5 | 2/3 of 16 | $35,750 |
| [Qwen3.8-2.4T UD-IQ1_S streamed](models/qwen38-a95b-udiq1s-qwencode.md) | macstudio-512gb | 2/3 of 3 | 5/5 of 5 | — | $13,000 |
| [K3 full-896 streamed, attempt 2](models/kimik3-896-iq2xxs-streamed-kimicode.md) | macstudio-512gb | — | 3/3 of 5 | — | $10,000 |
| [Qwen3.8 REAP-256GB](models/qwen38-reap256-iq1s-qwencode.md) | macstudio-512gb | 3/3 of 3 | 0/5 of 5 | — | $2,000 |
| [Qwen3.8 REAP-512GB](models/qwen38-reap512-iq2xxs-qwencode.md) | macstudio-512gb | 3/3 of 3 | — | — | $2,000 |
| [Qwen3.8 REAP-512GB (no counter-note)](models/qwen38-reap512-iq2xxs-qwencode.md) | macstudio-512gb | 1/3 of 3 | — | — | $500 |

## macstudio-512gb

| set | k27_q2_2bit | kimik3_reap640_iq1s | kimik3_reap576_iq2xxs | kimik3_streamed896_iq2xxs_18000s | kimik3_streamed896_iq2xxs_18000s_attempt2 | qwen38_a95b_udiq1s_10800s | qwen38_reap256_iq1s_10800s | qwen38_reap512_iq2xxs_10800s | qwen38_reap512_iq2xxs_promptv1m_10800s |
|---|---|---|---|---|---|---|---|---|---|
| sanity3 (3) | 3/3 | 3/3 | 3/3 | 3/3 | — | 2/3 | 3/3 | 1/3 | 3/3 |
| hard5 (5) | 0/5 | 2/5 | 4/5 | 2/5 | 3/3 | 5/5 | 0/5 | — | — |
| extended16 (16) | 0/16 | 2/10 | 6/16 | 2/3 | — | — | — | — | — |
| **total pass** | **3/24** | **7/18** | **13/24** | **7/11** | **3/3** | **7/8** | **3/8** | **1/3** | **3/3** |
| **earned** | $2,000 | $35,750 | $19,000 | $35,750 | $10,000 | $13,000 | $2,000 | $500 | $2,000 |
| **timeouts** | - | 11 | 9 | ≥1 | - | 0 | 0 | 0 | 0 |

## rtx6000-96gb

| set | gemma4_31b_nvfp4_pi_promptv1 | qwen38_27b_bf16_pi_promptv1 | qwen38_27b_bf16_qwencode_promptv1 |
|---|---|---|---|
| sanity3 (3) | 2/3 | 3/3 | 3/3 |
| hard5 (5) | 3/5 | 3/5 | 5/5 |
| extended16 (16) | 2/16 | 11/16 | 11/16 |
| **total pass** | **7/24** | **17/24** | **19/24** |
| **earned** | $9,250 | $48,000 | $53,750 |
| **timeouts** | 0 | 0 | 0 |

<!-- RESULTS:END -->

- Per-task results, split by execution environment: [`results/`](results/)
- Environment / speed table (read before comparing across CSVs): [`environments.md`](environments.md)
- Per-model commentary (behavior profiles): [`models/`](models/)
- Per-task commentary: [`TASKS.md`](TASKS.md) (English) / [`TASKS.ja.md`](TASKS.ja.md) (日本語)
- Task selection rules and common conditions: [`SELECTION.md`](SELECTION.md)
- How to re-run any cell on your hardware: [`REPLICATION.md`](REPLICATION.md)

**Agent policy**: to judge real-world usability, rollouts use each model vendor's official CLI agent where one exists, `pi` where none does, and both when time permits. From 2026-08-16 all new arms also carry a prompt counter-note neutralizing the benchmark's phantom scaffold instructions (`promptv1` on rtx / `promptv1m` on macstudio; see SELECTION.md).

Column naming: `<model>_<quant>_<agent/cli>_<condition labels>`; the rollout
cap (10800 s unless suffixed) and any prompt deviation (e.g. `promptv1`) are
part of the label. One attempt per task; never re-roll failures.

Cell values: `pass` / `fail` (finished, graded incorrect) / `timeout` (rollout cap hit before the agent finished) / `running` / `not_run`. Older macstudio columns predate the fail-vs-timeout distinction; per the source repo, 8 of 10 reap576 extended16 fails were cap-terminated; those cells may be reclassified if per-task data is published.
