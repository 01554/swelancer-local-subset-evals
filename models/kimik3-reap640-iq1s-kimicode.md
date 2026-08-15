# Kimi-K3 REAP640 — UD-IQ1_S base (Kimi Code CLI)

| | |
|---|---|
| checkpoint | [Kimi-K3-REAP-512GB-GGUF](https://huggingface.co/hellohazime/Kimi-K3-REAP-512GB-GGUF) REAP640-IQ1_S (441 GB) — 640 of 896 experts kept per layer, en+code saliency; experts uniform 1.56 bpw |
| engine | llama.cpp k3-stream (Metal), resident; decode ~3 tok/s |
| score | 7/18, $35,750 (sanity3 3/3 · hard5 2/5 · extended16 2/10, 6 tasks never ran) |
| timeouts | 11 — every audited fail was cap-terminated (8 in extended16, 3 in hard5 at 186 min each) |

## Run conditions

| | |
|---|---|
| engine | llama.cpp [`k3-stream` fork](https://github.com/01554/llama.cpp/tree/k3-stream) (Metal), `llama-server` |
| serve flags | `-ngl 99 -c 131072 --jinja --cache-reuse 0 --temp 1.0 --top-p 0.95` |
| sampling | temperature 1.0 · top-p 0.95 |
| context | 131,072 |
| rollout cap | 10800 s per task (whole-task wall clock; [why ours, not the paper's](../REPLICATION.md)) |
| agent | Kimi Code CLI, one attempt per task |

## Read (English)

**Owner of the single biggest scalp.** 6883 ($32,000 — hardware keyboard
shortcuts, the highest prize in the whole selection) fell to this arm at
~186 min, right at the cap. That one task is why its earned column looks
huge; per-task it trails REAP576 clearly (5/8 vs 7/8 on the 8-task set).

**Complementary, not dominated.** It holds passes REAP576 does not:
27353_776, 44429_1100, and 6883 itself. The pattern of non-overlapping wins
across arms is this project's recurring variance lesson — single attempts
at temp 1.0 measure "solved this run", not "can solve".

**Unfinished**: 6 extended16 tasks never ran (the machine moved on to the
Qwen sprint), so its totals are not comparable to complete arms — which is
why it sits in the unranked table. Every audited extended16 fail was a cap
kill at ~3 tok/s.

## 寸評(日本語)

**単発最高額の首を持つアーム。** 6883($32,000、ハードウェアキーボード
ショートカット実装)を cap ぎわ約186分で仕留めた。earned が膨らんで
見えるのはこの1問のせいで、タスク単位では REAP576 に明確に劣る(8タスク
5/8 vs 7/8)。

**支配されてはいない。** 27353_776・44429_1100・6883 は 576 が落として
このアームだけが通した問題。アーム間で勝ちが重ならないこのパターンが、
temp 1.0 単発試行の分散という本プロジェクト繰り返しの教訓。

**未完**: extended16 のうち6問は未走(マシンが Qwen スプリントに転用された
ため)。だから完走アームとは合計を比べられず、順位なし表にいる。監査済み
の extended16 負けは全部 cap 切れ。
