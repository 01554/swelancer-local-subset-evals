# Kimi-K3 full 896 experts — UD-IQ2_XXS, SSD-streamed (Kimi Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Kimi-K3-GGUF](https://huggingface.co/unsloth/Kimi-K3-GGUF) UD-IQ2_XXS (711 GB) — nothing pruned |
| engine | llama.cpp k3-stream `--moe-stream` (cache 380 GiB) on a 512 GiB machine; decode ~2 tok/s |
| cap | 18000 s (1.5× the standard 10800 s, compensating the slower decode) |
| score | 7/11, $35,750 (sanity3 3/3 · hard5 2/5 · extended16 2/3; 13 extended16 tasks never ran) |
| avg min/task | sanity3 **185.0** — 9¼ hours for the three easiest tasks |

## Run conditions

| | |
|---|---|
| engine | llama.cpp [`k3-stream` fork](https://github.com/01554/llama.cpp/tree/k3-stream) (Metal), `llama-server` |
| serve flags | `-ngl 99 -c 131072 --jinja --cache-reuse 0 --temp 1.0 --top-p 0.95` `--moe-stream --moe-stream-cache 380` |
| sampling | temperature 1.0 · top-p 0.95 |
| context | 131,072 |
| rollout cap | 18000 s per task (whole-task wall clock; [why ours, not the paper's](../REPLICATION.md)) |
| agent | Kimi Code CLI, one attempt per task |

## Read (English)

**The existence proof, and the cost of it.** A 711 GB model doing real
agentic work on a 512 GiB machine is the headline; 185 minutes *average*
on the three easiest tasks is the fine print. The arm was stopped by its
owner after 11 tasks because the wall-clock economics are absurd — a
cap-terminated fail burns five hours for zero.

**It still took 6883.** The $32,000 task fell here too (like REAP640, at
the cap's edge), plus 43395_530 — so even three extended16 tasks were enough
to show the unpruned model competes when given time.

**The trio saga lives here.** First attempt on 14294/15815_1/15925: 0/3 —
briefly the strangest cell in the table (pruned builds solved what the full
model couldn't). A separately-labeled second attempt went **3/3**
(`_attempt2` column; never merged into this one, per protocol). Verdict:
single-attempt variance, not pruning magic. This resolution is the
project's clearest argument for labeled re-runs over silent re-rolls.

## The uncapped probe (separate column, 2026-08-18)

Owner's question: *if the wall clock is the thing killing this arm, what
happens without one?* We re-ran the **five tasks the 53 GB Qwen3.8-27B
(Qwen Code arm) failed** with **no rollout cap** (72 h runaway backstop only)
and ctx 262,144 — column `kimik3_streamed896_iq2xxs_uncapped262k`, never
merged with the capped arm.

**Result: 4/5, $1,500** — 41885_1134 (393 min), 44618_1007 (599 min),
50064_846 (545 min), 29916_609 (304 min) passed; 50314_790 failed naturally
at 285 min. Mean 425 min/task.

Two findings, both load-bearing:

- **The cap was hiding real ability.** Every one of those four passes took
  longer than the 300-minute cap this arm used in its main column, and
  three of them longer than any cap we have ever run. The unpruned 1.75T
  model *can* solve tasks the fast 27B cannot — 44618_1007 and 29916_609
  had also defeated both pruned K3 builds.
- **It is still not a usable answer.** 4 wins cost 31 machine-hours. The
  27B earns $53,750 across the full 24 in about 12 hours total. On any
  practical clock, size loses to speed; the giant's edge only exists in a
  regime nobody deploys in.

50314_790 is the one cell no build in this project has ever passed — a
capability wall, not a clock wall.

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

## 無制限プローブ(別列、2026-08-18)

オーナーの問い: *このアームを殺しているのが時計なら、時計を外したらどうなる?*
**53GBの Qwen3.8-27B(Qwen Code腕)が落とした5問**を、**cap なし**(暴走保険の
72時間のみ)・ctx 262,144 で再走した。列は
`kimik3_streamed896_iq2xxs_uncapped262k`(capあり列とは絶対に合算しない)。

**結果: 4/5、$1,500** — 41885_1134(393分)、44618_1007(599分)、
50064_846(545分)、29916_609(304分)が正解、50314_790 は285分で自然フェイル。
平均425分/タスク。

読みは2つ、どちらも重要:

- **cap は本物の能力を隠していた。** 4勝すべてが、この列の本来の cap(300分)を
  超えた時間で取られている。うち3つは我々が設定したどの cap よりも長い。削って
  いない1.75Tは、速い27Bが解けない問題を**実際に解ける** — 44618_1007 と
  29916_609 は枝刈り版K3の両方も退けた問題だった。
- **それでも実用の答えではない。** 4勝に31マシン時間。27B は24問全体で
  $53,750 を約12時間で稼ぐ。**実用的な時計の下では、規模は速度に負ける。**
  巨人の優位は、誰も運用しないレジームにしか存在しない。

50314_790 は本プロジェクトのどのビルドも一度も通していない唯一のセル —
時計の壁ではなく能力の壁。
