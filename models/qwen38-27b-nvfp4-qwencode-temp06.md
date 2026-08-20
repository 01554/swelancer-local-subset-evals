# Qwen3.8-27B — NVFP4, temp 0.6 + MTP (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-NVFP4](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4) — same weights and server as the [temp 1.0 arm](qwen38-27b-nvfp4-qwencode.md) |
| engine | vLLM + `--enable-prefix-caching` (94.9% hit) + MTP speculative n=3 (output-lossless) |
| score | 20/24, $50,250 (sanity3 3/3 · hard5 4/5 · extended16 13/16) |
| avg min/task | **16.5** (vs 53.0 for the temp 1.0 arm — 3.2×) |

## Run conditions

Identical to the [temp 1.0 arm](qwen38-27b-nvfp4-qwencode.md) except: sampling
temperature **0.6** (top-p 0.95 unchanged), prefix caching enabled, MTP
speculative decoding enabled (speed-only), and thinking at model default.
Same agent (Qwen Code CLI 0.21.11), promptv1, text-only, cap 10800 s, one
attempt per task. This is the same configuration as the 174-task screening run.

## Read (English) — the temperature A/B verdict

Same 24 tasks, same weights, only the serving stack differs. **20/24 vs the
temp-1.0 arm's 22/24; discordant on 4 tasks (both arms failed 40208_1108 and
37688_441; this arm additionally lost 15815_1 and 50314_790).** A 2-task gap
sits far inside single-attempt variance (our own re-roll experiment showed 49%
of fails flip on retry), so this is **no evidence that temp 0.6 hurts** — and
the blog-reported 12-point agentic gain for 0.6 did not reproduce either.
What is unambiguous is the wall clock: **3.2× faster per task** from prefix
caching + MTP + shorter sampling tails. Practical default: this stack, with
temp treated as a non-factor until more attempts say otherwise.

## 寸評(日本語)

同一24問・同一重みでサービング条件だけ替えた温度 A/B。**20/24 vs temp1.0 の 22/24、割れたのは実質2問**(共通 fail 2問を除くと本アームだけ 15815_1 / 50314_790 を落とした)。2問差は1発試行の分散圏内(fail の49%が再走で反転する実測あり)で、**「0.6 が劣る」証拠にはならず、ブログの「0.6 が 12点勝つ」も再現せず**。確実なのは所要時間で、キャッシュ+MTP 込みで **1問あたり3.2倍速**。実用のデフォルトはこの構成で良く、温度は当面「効かないダイヤル」扱いが妥当。
