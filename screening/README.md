# 2026-08 full-pool screening (Qwen3.8-27B NVFP4) & next-gen subset proposal

A **selection run**, not an eval: conditions differ from the eval arms and are
recorded here. Goal: map the full 198-task IC-SWE Diamond pool against a
current-generation local model and extract a subset that still discriminates.

## Conditions (screening config)

| | |
|---|---|
| model | unsloth/Qwen3.8-27B-NVFP4 (22.6 GB), vLLM |
| sampling | temp 0.6 · top-p 0.95 (NOT the eval arms' 1.0) |
| speculative | MTP n=3 (output-lossless) |
| prefix caching | on (94.9% hit rate) |
| reasoning | model default (deepest); a 16-task probe additionally ran `reasoning_effort=low` baked into the chat template |
| agent | Qwen Code CLI 0.21.11, promptv1 note, text-only, cap 10800 s |
| parallelism | 3 shards vs one vLLM instance (~220 tok/s aggregate) |

## Results, full pool

- 24-task subset (eval arm, temp 1.0): 22/24 — see `results/rtx6000-96gb.csv`
- Remaining 174 (this screening): **135 pass / 37 fail / 1 timeout / 1 unrecorded-rerun→fail**
- Fail group re-run once under identical config: **19 of 39 passed on the second
  attempt (49%)** — single-attempt variance accounts for half of first-pass failures
- **Stable fail core: the 20 tasks failing 2/2** → `screening/double_fails_20.txt`

## Reasoning-depth probe (16 tasks)

- 8 slowest xhigh-passes re-run at `low`: **6/8 still pass, avg 107 min → 12 min (~9×)**
- 8 double-fails re-run at `low`: 1 rescued (44728_421), 6 still fail,
  1 became a 182-min cap timeout (18230_905)
- Practical read: low-first, escalate-to-xhigh is the cost-optimal ladder;
  the double-fail core is depth-invariant

## Proposal: next-gen subset "resolute20"

The 20 double-fails (2 attempts, temp 0.6, deepest thinking, 2026-08 model
generation). Annotations: 44728_421 falls to *low* thinking (exploration-trap
task); 18230_905 exceeds the 3 h cap even at low. Replaces the saturated
sanity3/hard5/extended16 axes for models at or above the Qwen3.8-27B tier;
the old 24-task set remains the cross-generation comparison anchor.

Raw per-task results: `screening/` CSVs. Durations in the shard console logs
(archived on the runner host).
