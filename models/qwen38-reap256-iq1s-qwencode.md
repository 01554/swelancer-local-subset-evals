# Qwen3.8-2.4T-A95B REAP-256GB — IQ1_S base (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [Qwen3.8-2.4T-A95B-REAP-256GB-GGUF](https://huggingface.co/hellohazime/Qwen3.8-2.4T-A95B-REAP-256GB-GGUF) (246 GB / 229 GiB) — 304 of 512 experts kept per layer by routing counts **and** 6 of 8 width superblocks per expert by activation energy; byte-copy of UD-IQ1_S, no requantization |
| engine | llama.cpp (Metal), fully resident `-ngl 99`; decode ~10 tok/s — also loads on stock mainline |
| agent | Qwen Code CLI 0.21.11 (pinned) |
| score | 3/8, $2,000 (probe 3/3 · differential 0/5) |
| timeouts | 0 — every fail was a natural exit, well under the cap |
| avg min/task | probe3 88.0 (vs 130.3 for its unpruned parent) |

## Read (English)

**Probe sweep, differential wipeout — the KLD tail made flesh.** Held-out
KLD vs its parent said most tokens survive (code median 0.020, argmax
86.6%) with damage concentrated in a heavy tail; the bench agrees:
routine tasks all pass, all five K2.7-hard tasks fail, each by finishing
wrong rather than running out of clock (zero timeouts, fails at 17–163
min).

**One genuine scalp over its parent**: 28096_836 — the tool-format stumble
that cost the unpruned arm its only loss did not recur here (single
attempts; could be luck). Everywhere else the parent is strictly better.
The honest reading: at a 1.56 bpw base there is no headroom to pay the
pruning tax on hard tasks — this is the *fits-256GB* build, not the best
build. The Q2-base keep-304 flagship (405 GB) is the follow-up experiment
this table demands.

**What it is for**: a 2.4T-parameter model doing real agentic work,
resident, on a 256 GB-class machine, at ~1.9× its parent's streamed speed
(88 vs 130 min on probe3) — and the first of our prunes that loads on
unmodified mainline llama.cpp.

## 寸評(日本語)

**probe 全勝・differential 全滅 — KLD テールの実体化。** 親モデルとの
held-out KLD は「大半のトークンは無傷(code 中央値 0.020、argmax 一致
86.6%)、被害はテール集中」だったが、ベンチも同じ形になった: 定型は
全部通り、K2.7 が落とした難問5問は全部落ちる。しかも全て時間切れでは
なく自然終了(timeout ゼロ、17〜163分)— 時計ではなく答えが間違う。

**親から取った首はひとつ**: 28096_836。親の唯一の負け(ツール形式の
躓き)がここでは再発しなかった(単発試行なので運の可能性あり)。それ以外
は親が全面的に上。正直な結論として、1.56bpw ベースには難問で枝刈り税を
払う余力がない — これは「256GB に収める」ビルドであって「最強」ビルド
ではない。この表が要求する次の実験が Q2 ベース keep-304(405GB)。

**存在意義**: 2.4T パラメータのモデルが 256GB 級マシンに常駐して実務
エージェントとして動く。親のストリーミング比 ~1.9倍速(probe3 88分 vs
130分)、かつ**うちの枝刈りで初めて素の mainline llama.cpp でロード
できるビルド**。
