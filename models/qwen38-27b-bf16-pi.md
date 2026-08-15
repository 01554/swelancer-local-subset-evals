# Qwen3.8-27B — BF16 (pi)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) BF16 (53 GB, full precision, dense 27B) |
| engine | llama.cpp server-cuda |
| decode | 26–29 tok/s |
| score | 17/24, $48,000 (probe 3/3 · differential 3/5 · battle16 11/16) |
| avg min/task | 15.0 (probe3) / 43.8 (all24), max ~2 h — cap never reached |

## Read (English)

**A grinder that converts time into wins.** Task time scales with difficulty
(probe 15 min → overall 43.8 min, up to two hours on hard tasks), and the
investment pays: 11/16 on battle16, where the fail-fast Gemma-4 took 2/16 and
the 478 GB kimik3_reap576 took 6/16. New leader of this subset at 53 GB —
a dense 16-bit 27B beating a ~60B-active 2-bit MoE with a 1.75T-parameter
expert pool, i.e. a clean datapoint that low-bit quantization costs more than
a big expert pool buys.

**Robust to the benchmark's traps.** Never fell for the phantom `<user-tool>`
(run with the same promptv1 note as all rtx6000 arms; behavior without the note
is untested). First-ever passes on five tasks no other build had solved,
including the reference-dependent 29916_609 and the visually-specified
37688_441 — the latter cracked by following a dangling code reference rather
than by seeing the screenshot.

**Caveat**: its 17/24 carries a speed bonus relative to the Mac Studio columns —
at 26 tok/s it never met the 10800 s cap that terminated many Kimi attempts.

## 寸評(日本語)

**時間を勝ちに変換するグラインダー。** 所要時間が難易度に比例し(probe 15分 → 全体 43.8分、最長2時間)、その投資が battle16 の 11/16 として回収された(Gemma 2/16、478GB の reap576 でも 6/16)。53GB の BF16 密モデルが「アクティブ ~60B・2bit・総量 1.75T」の MoE を破ったことは、低ビット量子化のコストがエキスパート数の利得を上回るというきれいな実測点。

**ベンチの罠に強い。** 幻の `<user-tool>` には一度も釣られなかった(promptv1 は他アームと同一適用。打消しなしでの挙動は未検証)。他のどのビルドも解けなかった5問を初クリアし、うち 37688_441 はスクショを見ずに、コード内の宙ぶらりん参照から仕様を逆算して解いた。

**但し書き**: 17/24 には速度ボーナスが乗っている — 26 tok/s ではキャップ(10800s)に一度も達しておらず、キャップ切れ頻発だった Mac Studio 列とは条件の効き方が違う。
