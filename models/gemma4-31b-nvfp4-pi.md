# Gemma-4-31B-IT — NVFP4 (pi)

| | |
|---|---|
| checkpoint | [CISCai/gemma-4-31B-it-NVFP4-turbo-GGUF](https://huggingface.co/CISCai/gemma-4-31B-it-NVFP4-turbo-GGUF) (19.3 GB) |
| engine | llama.cpp server-cuda, native NVFP4 kernels on Blackwell |
| decode | 63.9 tok/s |
| score | 7/24, $9,250 (sanity3 2/3 · hard5 3/5 · extended16 2/16) |
| avg min/task | 4.3 (sanity3) / 6.2 (all24) |

## Run conditions (as recorded in [columns.csv](../results/columns.csv))

| | |
|---|---|
| engine | llama.cpp server-cuda (Docker) |
| sampling | temperature 1.0 · top-p 0.95 |
| context | 131,072 |
| rollout cap | 10800 s per task (never reached on this hardware) |
| agent | pi, with the `promptv1` phantom-`​``python`-neutralizing note |

## Read (English)

**A fail-fast sprinter.** Task times sit in a flat 3–10 minute band regardless of
difficulty — Gemma-4 never grinds. It converges on *a* fix quickly, states it
confidently, and stops. On easy tasks this is efficiency; on extended16 it means
under-exploration, and the 2/16 there is the price.

**Instruction-following is its strength and its trap.** Without the `promptv1`
note it follows the benchmark's phantom "reply with a ```python block"
instruction to the letter and one-turns to death on every task (2/2 reproduced) —
the only model observed to need the note to function at all. It also fell for
the phantom `<user-tool>` twice (18827_741, 4324 — $3,000 of losses), politely
waiting for a human tester that does not exist.

**Notable**: its 14294 fix took a structurally different (and cruder) approach
than the upstream Expensify fix — evidence of solving rather than recalling.
Passed 44618_1007, which k27 and reap576 both failed (reap640 later ran it too and failed at the cap; the streamed-896 arm never ran it — so this is the only pass among the four builds that ran it).

## 寸評(日本語)

**即断即決のスプリンター。** 難易度に関係なく全タスク3〜10分のフラットな時間分布で、難問に粘るということをしない。簡単な問題では効率だが、extended16 では探索不足がそのまま 2/16 に出た。

**指示追従の強さが長所であり罠。** promptv1 打消しなしでは幻の「```python で応答せよ」指示に忠実に従い全タスク1ターン死(観測したモデルで唯一、打消し必須)。幻の `<user-tool>` にも2回釣られ、実在しない人間テスターを律儀に待って $3,000 分を落とした。

**特記**: 14294 の修正は本家 Expensify の修正と構造的に異なる(より力技の)別解で、暗記でなくその場で解いた証拠。44618_1007 を通した(k27・reap576 は fail、reap640 も後日走って cap 切れ fail。streamed896 のみ未実走 — 実走4ビルド中唯一の pass)。
