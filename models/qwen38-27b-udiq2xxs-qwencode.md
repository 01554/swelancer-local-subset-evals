# Qwen3.8-27B — UD-IQ2_XXS (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) UD-IQ2_XXS (8.4 GB, dynamic ~2.1 bpw; same base weights as the BF16/NVFP4 arms) |
| engine | llama.cpp `server-cuda` (Docker) + MTP speculative decoding (`--spec-type draft-mtp --spec-draft-n-max 2`) |
| decode | 87.7 tok/s plain / 119.9 tok/s with MTP (draft acceptance 57–75%) |
| score | 7/24, $9,250 (sanity3 3/3 · hard5 3/5 · extended16 1/16) |
| avg min/task | 24.6 (all24); cap never reached |

## Run conditions

| | |
|---|---|
| serve flags | `-m …UD-IQ2_XXS.gguf --alias qwen3.8-27b-iq2 -ngl 999 -c 131072 --temp 1.0 --top-p 0.95 --spec-type draft-mtp --spec-draft-n-max 2` |
| sampling | temperature 1.0 · top-p 0.95 |
| context | 131,072 |
| rollout cap | 10800 s (never reached) |
| agent | Qwen Code CLI (`@qwen-code/qwen-code@0.21.11`), same setup as the other qwencode arms; base URL `http://172.17.0.1:8080/v1` |
| modality | text-only (standing condition) |
| speculative decoding | MTP n=2 — output-lossless (verify-accept), speed-only; noted here because it is the first arm to use it |

### Incident note (2026-08-17)

Mid-arm, the host's root disk filled (image pulls were landing in
`/var/lib/containerd` on the root disk — a config gap now fixed by relocating
the containerd store to the data SSD with a bind mount). One in-flight task
hung and 13 subsequent rollouts aborted before the agent could start; per the
harness-error precedent those were treated as not attempted and re-run after
recovery. 11 pre-incident results were preserved; the interrupted task's first
attempt was discarded.

## Read (English)

**2-bit is where this model finally breaks — and it breaks from the details
outward.** sanity3 stayed perfect (the model is not "degenerated" in the
K3-REAP sense: no repetition loops, tools still work, $4,000-class fixes still
land — it even solved 14294 in 16 minutes). What collapsed is extended16:
**1/16** against 14/16 for NVFP4 on identical weights. The first hard5 losses
were the pixel-perfect task (15815_1) and the theme-color task (27353_776) —
precision-flavored failures, consistent with quantization noise erasing fine
distinctions before it touches broad competence.

**The 22.6 GB → 8.4 GB step costs 15 tasks.** NVFP4 22/24 vs IQ2_XXS 7/24 is
the sharpest quantization cliff measured in this repo, far larger than the
BF16→NVFP4 step (19→22, i.e. noise). For this dense 27B the frontier is
unambiguous: **4-bit free, 2-bit expensive.**

**Speed footnote**: first arm to use MTP speculative decoding (+37% decode,
output-lossless). Even so it averaged 24.6 min/task — fail-fast dynamics, like
Gemma-4: same $9,250 total, by coincidence or by convergent behavior of models
that under-explore.

## 寸評(日本語)

**2bit がこのモデルの崩壊点 — ただし崩れ方は「細部から外へ」。** sanity3 は満点で、K3-REAP で見たような反復ループ型の崩壊ではない(ツールも動くし、14294 の $4,000 修正を16分で通す地力は残る)。壊れたのは extended16 で、同一重みの NVFP4 が 14/16 のところ **1/16**。hard5 の初黒星もピクセル精度(15815_1)とテーマ色(27353_776)という「精密さ」系で、量子化ノイズが広い能力より先に細かい弁別を消すという読みに合致する。

**22.6GB → 8.4GB の一段で15問を失った。** NVFP4 22/24 vs IQ2 7/24 は本リポジトリ観測史上最大の量子化クリフで、BF16→NVFP4 の差(19→22、ノイズ圏)とは桁が違う。この密27Bにおける結論は明快: **4bit はタダ、2bit は高くつく。**

**速度の脚注**: MTP 投機デコード初採用アーム(+37%、出力無劣化)。それでも平均24.6分/問と fail-fast 型の挙動で、奇しくも獲得額は Gemma-4 と同じ $9,250 — 探索不足のモデルは似た場所に収束するのかもしれない。
