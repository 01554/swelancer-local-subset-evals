# Kimi-K3 REAP576 — UD-IQ2_XXS base (Kimi Code CLI)

| | |
|---|---|
| checkpoint | [Kimi-K3-REAP-512GB-GGUF](https://huggingface.co/hellohazime/Kimi-K3-REAP-512GB-GGUF) REAP576-IQ2_XXS (478.5 GB / 446 GiB) — 576 of 896 experts kept per layer, en+code saliency; quant mix IQ1_M/IQ2_XXS/IQ3_XXS ≈ 1.91 bpw |
| engine | llama.cpp k3-stream (Metal), resident; prefill 48.3 / decode 2.98 tok/s |
| score | 13/24, $19,000 (probe 3/3 · differential 4/5 · battle16 6/16) |
| timeouts | ≥8 — all 8 of its audited battle16 fails hit the 10800 s cap |

## Read (English)

**The strongest K3 arm per task, and the "bits beat experts" datapoint.**
On the 8-task set it went 7/8 ($13,000) where the larger-expert-count
REAP640 (1.56 bpw) went 5/8 — fewer experts at ~1.91 bpw beat more experts
at 1.56 bpw. Its trio sweep (14294 / 15815_1 / 15925) was the first solve
of those tasks by any 512 GB config in this project.

**Cap-starved on battle16.** 6/16 with every audited failure cap-terminated:
at 3 tok/s, three hours is simply not much agentic work (compare the
BF16-27B's 11/16 at 26 tok/s, never capped). One pass — 4324 — landed at
~186 min, right on the wall. The 21600 s re-run study exists for exactly
this column.

**Blind spot**: its one differential miss, 27353_776 (theme-color inference),
fell to REAP640, the unpruned Qwen and nobody else pruned — cap status of
that fail is unaudited.

## 寸評(日本語)

**K3系で最強のアームで、「expert数よりビット数」の実測点。** 8タスクで
7/8($13,000) — expert数で勝る REAP640(1.56bpw)の 5/8 を上回った。トリオ
(14294/15815_1/15925)の一斉クリアは、このプロジェクトの512GB構成で初。

**battle16 では cap に絞め殺された。** 6/16、監査済みの負け8つは全部
10800秒の壁 — 3 tok/s の3時間は、エージェント仕事としては短い(26 tok/s
で一度も cap に触れなかった 27B の 11/16 と対照的)。4324 は約186分、壁
ぎわの合格。21600秒の再走計画はこの列のためにある。

**穴**: differential 唯一の取りこぼし 27353_776(テーマ色推論)。この fail
の cap 該当性だけは未監査。
