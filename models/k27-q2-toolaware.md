# Kimi-K2.7 — Q2 (custom tool-aware solver)

| | |
|---|---|
| checkpoint | [unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF) UD-Q2_K_XL (~341 GB) — the project's original baseline |
| engine | llama.cpp (Metal), macstudio-512gb |
| agent | **custom tool-aware solver, not a CLI** — this run predates the CLI harness (June 198-task run; disclosed in the original writeup) |
| score | 3/24, $2,000 — **by construction, not a measurement** |
| avg min/task | - (per-task durations not recorded) |

## Run conditions

| | |
|---|---|
| engine | llama.cpp (Metal), `llama-server` |
| sampling | temperature 1.0 · top-p 0.95 |
| context | 131,072 |
| limits | **no per-task wall clock** — instead a 900 s per-response cutoff, sized to fit 198 tasks into ~2 weeks (fired on 109/198 tasks, 75 zeroed; disclosed in the [original writeup](https://zenn.dev/hellohazime/articles/kimi_k27_code_swelancer_local)) |
| agent | custom tool-aware solver (pre-CLI), one attempt per task |

## Read (English)

**This column is the yardstick, not a contestant.** Every task set in this
eval was *defined* from this arm's full 198-task run: sanity3 = 3 tasks it
solved, hard5 and extended16 = tasks it failed. Its 3/24 is therefore
tautological — it cannot score anything else. Rank it accordingly (i.e.,
don't).

**What it is for**: anchoring. Any build that passes a hard5 or
extended16 task has, on that task, beaten the K2.7-Q2 baseline under
comparable local-serving conditions. The 198-task run it comes from is the
only full-split run in this project.

**Condition caveat**: agent differs from every other macstudio arm (custom
solver vs Kimi Code CLI), and its fails predate the fail/timeout
distinction. Treat cross-agent comparisons with the usual suspicion.

## 寸評(日本語)

**この列は物差しであって選手ではない。** sanity3 はこのアームが解けた3問、
hard5 と extended16 は落とした問題から定義されているので、3/24 は
同語反復 — 原理的にこれ以外の点が付かない。順位表に載せる意味はない。

**用途はアンカー。** 他のビルドが hard5/extended16 を通したら、その
タスクでは K2.7-Q2 基準を超えた、と読むための列。元になった198タスク
全走はこのプロジェクト唯一のフル走行でもある。

**条件の但し書き**: agent が他の mac 列と違う(自作ソルバ、CLI以前)。
fail/timeout の区別も記録がない。
