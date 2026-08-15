# Kimi-K3 full 896 experts — UD-IQ2_XXS, SSD-streamed (Kimi Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF) UD-IQ2_XXS (711 GB) — nothing pruned |
| engine | llama.cpp k3-stream `--moe-stream` (cache 380 GiB) on a 512 GiB machine; decode ~2 tok/s |
| cap | 18000 s (1.5× the standard 10800 s, compensating the slower decode) |
| score | 7/11, $35,750 (probe 3/3 · differential 2/5 · battle16 2/3; 13 battle16 tasks never ran) |
| avg min/task | probe3 **185.0** — 9¼ hours for the three easiest tasks |

## Read (English)

**The existence proof, and the cost of it.** A 711 GB model doing real
agentic work on a 512 GiB machine is the headline; 185 minutes *average*
on the three easiest tasks is the fine print. The arm was stopped by its
owner after 11 tasks because the wall-clock economics are absurd — a
cap-terminated fail burns five hours for zero.

**It still took 6883.** The $32,000 task fell here too (like REAP640, at
the cap's edge), plus 43395_530 — so even three battle16 tasks were enough
to show the unpruned model competes when given time.

**The trio saga lives here.** First attempt on 14294/15815_1/15925: 0/3 —
briefly the strangest cell in the table (pruned builds solved what the full
model couldn't). A separately-labeled second attempt went **3/3**
(`_attempt2` column; never merged into this one, per protocol). Verdict:
single-attempt variance, not pruning magic. This resolution is the
project's clearest argument for labeled re-runs over silent re-rolls.

## 寸評(日本語)

**存在証明と、その代償。** 711GB を 512GiB 機で実務エージェントとして
動かせたことが見出しで、「最も簡単な3問の平均185分」が但し書き。11問
時点でオーナー判断で停止 — cap 切れ負けは5時間燃やしてゼロ点になる。

**それでも 6883 は取った。** $32,000 の最高額問題をここも cap ぎわで
仕留め、43395_530 も通した。時間さえ与えれば削っていない本体は戦える。

**トリオ騒動の現場。** 初回 0/3(削った方が解けて本体が解けない、表で
一番奇妙なセル)→ 別ラベルの2回目で **3/3**(`_attempt2` 列。この列には
決して合算しない)。結論は枝刈りの魔法ではなく単発試行の分散。無言の
リロールではなくラベル付き再走を、という本プロジェクトの一番分かり
やすい根拠になった。
