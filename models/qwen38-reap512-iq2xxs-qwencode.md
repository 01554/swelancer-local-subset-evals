# Qwen3.8-2.4T-A95B REAP-512GB — IQ2_XXS base (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [Qwen3.8-2.4T-A95B-REAP-512GB-GGUF](https://huggingface.co/hellohazime/Qwen3.8-2.4T-A95B-REAP-512GB-GGUF) (404 GB / 376 GiB) — 304 of 512 experts by routing counts, width untouched; byte-copy of the unpruned UD-IQ2_XXS, which at 656.6 GB cannot load on a 512 GiB machine at all |
| engine | llama.cpp (Metal), fully resident `-ngl 99`; decode 9.3–9.5 tok/s — fork and stock mainline both verified |
| KLD vs parent | en 0.110 / argmax 87.6% · code 0.196 / median **0.007** / argmax **90.0%** — the highest-fidelity prune in this project |
| score | promptv1m: **5/8, $8,000** (sanity3 3/3 · hard5 2/5) · bare-prompt control: sanity3 1/3 |
| timeouts | 1 (15815_1 at 185 min); other fails natural (bare-prompt control: ~20-min one-turn exits) |
| avg min/task | sanity3 96.0 · hard5 97.8 (bare-prompt control: 24.3, fails fast) |

## Run conditions

| | |
|---|---|
| engine | llama.cpp (Metal) — fork **or stock mainline**, both verified |
| serve flags | `-ngl 99 -c 131072 --jinja --temp 1.0 --top-p 0.95 --top-k 20` |
| sampling | temperature 1.0 · top-p 0.95 · top-k 20 (per the Unsloth card) |
| context | 131,072 |
| rollout cap | 10800 s per task |
| agent | Qwen Code CLI 0.21.11 (pinned); `QWEN_STREAM_IDLE_TIMEOUT_MS=0`; promptv1m column sets `QWEN_PROMPT_NOTE=v1m` |

## Read (English)

**The sanity gate earning its keep.** This build has the best KLD of any
prune we've shipped (code argmax 90%), yet the bare-prompt sanity3 went 1/3
— it one-turn-died on 18827_741 and 29618_781 with *verbatim-identical*
```` ```python ```` text blocks, obeying the benchmark prompt's phantom
scaffold instruction. Run-log verified, deterministic-looking, and exactly
the failure class the KLD oracle cannot see. The likely mechanism is
uncomfortable: **the more faithfully a build follows instructions, the
harder it falls for the phantom** — Gemma-4 (rtx) needed the same cure.

**The controlled fix.** With one appended paragraph stating that python
blocks are not executed and tool calls are the only way to act
(`promptv1m`, now standard for all new arms), the same cells became
parent-style grind-passes: 18827_741 went from a 20-minute death to a
74-minute $1,000 win; 29618_781 from 19 minutes to a 185-minute wire-to-wire
$500. **3/3.**

**Where it stands after hard5 (owner-requested extension)**: 2/5 —
took 14294 ($4,000) and beat its parent's clock on the heaviest task
(15925, ~104k-token issue: solved in 99 min where the streamed parent
needed 183 cap-edge minutes), but dropped two tasks the parent grinds out
and lost 15815_1 to the cap. Total 5/8 vs the parent's 7/8: the KLD ladder
(parent > 512GB > 256GB) reproduces exactly as a bench ladder
(7/8 > 5/8 > 3/8). Fidelity costs capability; resident speed buys some of
it back.

## 寸評(日本語)

**sanity ゲートが給料分の仕事をした回。** KLD はプロジェクト最良
(code argmax 90%)なのに、素のプロンプトでは sanity3 が 1/3 — 18827_741
と 29618_781 で一言一句同じ ```` ```python ```` ブロックを吐いて1ターン死。
ベンチプロンプトに残る「幻のスキャフォールド指示」への服従で、ログ検証
済み・決定論的挙動。KLD オラクルには原理的に見えない故障クラスで、
**指示追従が良いビルドほど深く罠に落ちる**(rtx の Gemma-4 と同じ処方が
必要だった)。

**対照実験による治療。** 「python ブロックは実行されない、行動手段は
ツール呼び出しのみ」という一段落(`promptv1m`、以後全アーム標準)を足した
だけで、同じセルが親と同じ粘り勝ちに変貌: 18827_741 は20分死→74分で
$1,000、29618_781 は19分死→185分完走で $500。**3/3。**

**hard5 延長戦後の立ち位置**(オーナー指示の追加測定): 2/5 — 14294
($4,000)を取り、最重量の 15925(issue 本文~104k トークン)は**親の半分の
時間**(99分 vs 183分)で解いた。一方で親が粘り出す2問を落とし、15815_1
は cap 切れ。総合 5/8 vs 親 7/8 — **KLD の梯子(親 > 512GB > 256GB)が
そのままベンチの梯子(7/8 > 5/8 > 3/8)として再現**した。忠実度は能力に
直結し、常駐速度がその一部を買い戻す。
