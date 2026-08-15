# Qwen3.8-27B — BF16 (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) BF16 (53 GB, full precision, dense 27B) — same weights and server as the pi arm |
| engine | llama.cpp `ghcr.io/ggml-org/llama.cpp:server-cuda` (Docker) |
| decode | 26–29 tok/s |
| score | 19/24, $53,750 (sanity3 3/3 · hard5 5/5 · extended16 11/16) |
| avg min/task | 13.7 (sanity3) / 29.1 (all24) — 11.7 h total, cap never reached |

## Run conditions

| | |
|---|---|
| serve flags | identical to the [pi arm](qwen38-27b-bf16-pi.md) — same running server instance |
| sampling | temperature 1.0 · top-p 0.95 (server-side defaults) |
| context | 131,072 |
| rollout cap | 10800 s per task (never reached; verified — zero cap markers in run logs) |
| agent | Qwen Code CLI (`@qwen-code/qwen-code@0.21.11`, pinned), `qwen -y` positional-prompt mode, one attempt per task |
| agent config | OpenAI-compatible env (`OPENAI_BASE_URL` → host llama-server, `QWEN_STREAM_IDLE_TIMEOUT_MS=0`); same `promptv1` note as all rtx6000 arms |
| modality | text-only (standing condition of this eval) |

## Read (English)

**The maker's own agent squeezes more out of the same model.** Identical
weights, server, sampling and prompt as the pi arm — only the harness differs —
and the score moves 17/24 → **19/24** ($48,000 → $53,750). It swept
sanity3+hard5 **8/8** (best on record, above reap576's 7/8), recovering both
hard5 tasks pi lost (27353_776, 15925).

**Where the two harnesses diverge** (same model, 5 tasks split): Qwen Code won
27353_776, 15925, 43395_530, 25901_945, 4324; pi won 29916_609 and 50314_790.
The pattern reads as Qwen Code being stronger at grinding a code change to
completion, pi at going out and reading referenced material — it remains the
only rtx6000 arm to pass the reference-dependent 29916_609.

**Both visually-specified tasks fell** (43395_530, 25901_945) despite the
text-only condition — apparently inferable from neighboring code. 37688_441
too, making Qwen Code 3/3 on the visually-dependent group that pi went 1/3 on.

**Per-task pace is between sprint and grind**: 29.1 min average vs pi's 43.8 on
the same model — fewer, denser turns; same-task times range from half of pi's
to nearly double (46 min on 14294 vs pi's 25).

## 寸評(日本語)

**純正ハーネスが同じモデルからより多くを引き出した。** 重み・サーバー・サンプリング・プロンプトは pi アームと完全同一で、ハーネスだけ替えて 17/24 → **19/24**($53,750)。sanity3+hard5 は**記録上最高の 8/8**(reap576 の 7/8 超え)で、pi が落とした hard5 の2問(27353_776 / 15925)を両方回収した。

**ハーネス個性の割れ方**(同一モデルで5問が分岐): Qwen Code は 27353 / 15925 / 43395 / 25901 / 4324 を取り、pi は 29916_609 / 50314_790 を取った。「コード修正を最後まで詰める力は Qwen Code、参照先を読みに行く探索は pi」という読みで、外部参照依存の 29916_609 を通した rtx6000 アームは今も pi だけ。

**視覚依存3問を全部取った**(pi は 1/3)。テキストオンリー条件でもデザイン仕様を周辺コードから復元できることの傍証。

**ペースはスプリントとグラインドの中間**: 同一モデルで平均 29.1分(pi 43.8分)。ただしタスク別では pi の半分〜2倍近くまで振れる(14294 は 46分 vs pi 25分)。
