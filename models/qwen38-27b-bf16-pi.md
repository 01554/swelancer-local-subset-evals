# Qwen3.8-27B — BF16 (pi)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) BF16 (53 GB, full precision, dense 27B) |
| engine | llama.cpp server-cuda |
| decode | 26–29 tok/s |
| score | 17/24, $48,000 (sanity3 3/3 · hard5 3/5 · extended16 11/16) |
| avg min/task | 15.0 (sanity3) / 43.8 (all24), max ~2 h — cap never reached |

## Run conditions (as recorded in [columns.csv](../results/columns.csv))

| | |
|---|---|
| engine | llama.cpp `ghcr.io/ggml-org/llama.cpp:server-cuda` (Docker, same image as the gemma4 run) |
| serve flags | `-m Qwen3.8-27B-BF16-00001-of-00002.gguf --mmproj mmproj-BF16.gguf --alias qwen3.8-27b -ngl 999 -c 131072 --temp 1.0 --top-p 0.95` |
| sampling | temperature 1.0 · top-p 0.95 (server-side defaults) |
| context | 131,072 |
| rollout cap | 10800 s per task (never reached; longest task ~2 h) |
| agent | pi 0.84.1 (`@earendil-works/pi-coding-agent@0.84.1`), print mode (`-p`), one attempt per task |
| agent config | custom provider via `~/.pi/agent/models.json` (`api: openai-completions`, host llama-server over LAN); same `promptv1` note as all rtx6000 arms |
| in-container quirks | node 22 via nvm (same as gemma4 run) |
| modality | text-only. Not an explicit choice at setup time: pi treats models as text-only when `input` is omitted in models.json (default `[\"text\"]`). Verified post-hoc from server logs: zero image payloads across all rtx6000 arms, so pi and Qwen Code arms are modality-matched. Kept deliberately going forward — the Kimi precedent has no record of image use either |

## Read (English)

**A grinder that converts time into wins.** Task time scales with difficulty
(sanity3 15 min → overall 43.8 min, up to two hours on hard tasks), and the
investment pays: 11/16 on extended16, where the fail-fast Gemma-4 took 2/16 and
the 478 GB kimik3_reap576 took 6/16. New leader of this subset at 53 GB —
a dense 16-bit 27B beating a ~60B-active 2-bit MoE with a 1.75T-parameter
expert pool, i.e. a clean datapoint that low-bit quantization costs more than
a big expert pool buys.

**Robust to the benchmark's traps.** Never fell for the phantom `<user-tool>`
(run with the same promptv1 note as all rtx6000 arms; behavior without the note
is untested). Passes on five tasks with no prior pass on record. The clean case is
29916_609, attempted and failed by all four Kimi builds; for the other
four (18746_833 / 44429_1100 / 40208_1108 / 37688_441) only k27 and
reap576 had attempted them (reap640 / streamed-896 pending). Also
notable: the visually-specified 37688_441 — cracked by following a dangling code reference rather
than by seeing the screenshot.

**Caveat**: its 17/24 carries a speed bonus relative to the Mac Studio columns —
at 26 tok/s it never met the 10800 s cap that terminated many Kimi attempts.

## 寸評(日本語)

**時間を勝ちに変換するグラインダー。** 所要時間が難易度に比例し(sanity3 15分 → 全体 43.8分、最長2時間)、その投資が extended16 の 11/16 として回収された(Gemma 2/16、478GB の reap576 でも 6/16)。53GB の BF16 密モデルが「アクティブ ~60B・2bit・総量 1.75T」の MoE を破ったことは、低ビット量子化のコストがエキスパート数の利得を上回るというきれいな実測点。

**ベンチの罠に強い。** 幻の `<user-tool>` には一度も釣られなかった(promptv1 は他アームと同一適用。打消しなしでの挙動は未検証)。記録上先行 pass の無い5問を通した(全ビルド実走で全滅していたのは 29916_609 のみ。残り4問は k27 と reap576 の fail 記録のみで、reap640 / streamed896 は未完走)。うち 37688_441 はスクショを見ずに、コード内の宙ぶらりん参照から仕様を逆算して解いた。

**但し書き**: 17/24 には速度ボーナスが乗っている — 26 tok/s ではキャップ(10800s)に一度も達しておらず、キャップ切れ頻発だった Mac Studio 列とは条件の効き方が違う。
