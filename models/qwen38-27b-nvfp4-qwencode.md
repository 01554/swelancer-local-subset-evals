# Qwen3.8-27B — NVFP4 (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-NVFP4](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4) (22.6 GB safetensors, compressed-tensors NVFP4; same base weights as the BF16 arms) |
| engine | vLLM (`vllm/vllm-openai:latest`, Docker) |
| decode | ~63 tok/s single-stream (2.4× the BF16 llama.cpp serving) |
| score | **22/24, $54,500 — best on record** (sanity3 3/3 · hard5 5/5 · extended16 14/16) |
| avg min/task | see columns.csv; cap never reached |

## Run conditions

| | |
|---|---|
| serve flags | `--model … --served-model-name qwen3.8-27b-nvfp4 --override-generation-config '{"temperature":1.0,"top_p":0.95}' --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3` |
| sampling | temperature 1.0 · top-p 0.95 (top-k left at engine default; official rec is top-k 20 — noted, not applied, for cross-arm consistency) |
| reasoning | model default (thinking on, deepest level) |
| context | 131,072 (`--max-model-len` default clamped by request sizes) |
| KV cache | engine default for this checkpoint (FP8 per its `kv_cache_scheme`) |
| rollout cap | 10800 s per task (never reached) |
| agent | Qwen Code CLI (`@qwen-code/qwen-code@0.21.11`), same env as the BF16 qwencode arm; base URL `http://172.17.0.1:8080/v1` (docker bridge — LAN-independent after the incident below) |
| modality | text-only (standing condition) |

### Engine gotchas (first-hand)

- `--quantization modelopt` fails: this checkpoint declares `compressed-tensors`; let vLLM auto-detect
- Without `--tool-call-parser qwen3_coder` tool calls arrive as raw `<tool_call><function=…>` text (hermes parser does NOT match); agents then silently degrade
- MTP speculative decoding was **not** enabled on this run (noted for future arms)

### Incident note (2026-08-16)

After 3 tasks, a LAN/DHCP failure took down the host's IPv4 for ~1 h: 21 rollouts
aborted before the agent could even install (`npm` unreachable) and were recorded
as instant fails. Per this kit's harness-error precedent (SELECTION.md), those
were treated as **not attempted**: the rows were removed and the tasks re-run
once network returned. The 3 completed pre-incident tasks were kept. 14294's
first attempt was also discarded as its rollout straddled the outage.

## Read (English)

**Best result on this subset to date, at 4 bits.** Same weights as the BF16
arms, quantized to NVFP4 (FP4 weights + FP8 block scales, native on Blackwell),
and the score *rose*: 19/24 → 22/24. The honest read is not "4-bit beats
16-bit" but "NVFP4 is statistically indistinguishable from BF16 here, and
single-attempt variance landed on the good side" — which is exactly the
lossless-quantization claim, demonstrated on 3-hour-class real tasks rather
than short benchmark suites.

**It ran a 16-task unbeaten streak**, took the $32,000 task, both
previously-Gemma-only and never-solved-by-anyone tasks (44618_1007, 50064_846
— the latter closing the last unsolved cell in the union table), and passed
2/3 of the visually-specified tasks text-blind. Its 2 losses (40208_1108,
37688_441) were both solved by other arms — the union of runs now covers 24/24.

**Speed changes the economics**: 2.4× the BF16 decode rate on half the VRAM
footprint, with the same wall-clock cap never in sight. For this hardware
class, NVFP4 + a maker's-own CLI is currently the efficiency frontier.

## 寸評(日本語)

**4bit で歴代最高記録。** 重みは BF16 アームと同一物の NVFP4 量子化(FP4 重み+FP8 ブロックスケール、Blackwell ネイティブ)で、スコアはむしろ 19/24 → 22/24 に上昇。正確な読みは「4bit が 16bit に勝った」ではなく「**NVFP4 は BF16 と統計的に区別がつかず、1発試行の分散が良い方に出た**」— つまり無劣化量子化の主張が、短問ベンチではなく3時間級の実案件で実証された形。

**16連勝の無敗記録**を作り、$32,000 の大物、Gemma 専売だった 44618_1007、そして**誰も解けていなかった 50064_846**(和集合表の最後の未踏セル)まで陥落させた。負けた2問(40208 / 37688)は他アームが解いており、**全ランの和集合は 24/24 に到達**。

**経済性が別次元**: BF16 比で VRAM 半分以下・decode 2.4倍・品質同等。この機体クラスでは「NVFP4+純正 CLI」が現時点の効率フロンティア。
