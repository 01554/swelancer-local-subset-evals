# Qwen3.8-2.4T-A95B — UD-IQ1_S, SSD-streamed (Qwen Code CLI)

| | |
|---|---|
| checkpoint | [unsloth/Qwen3.8-2.4T-A95B-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF) UD-IQ1_S (508 GB, experts 1.56 bpw) — nothing pruned |
| engine | llama.cpp k3-stream `--moe-stream` (cache 400 GiB); decode 5.3–6.3 tok/s |
| agent | Qwen Code CLI 0.21.10→0.21.11 (pinned mid-arm after npm moved) |
| score | 6/7 so far, $11,000 — probe 2/3 · differential 4/4 decided, final task (15925) running |
| timeouts | 0 — its one fail was a 21-minute natural exit |

## Read (English)

**The best macstudio arm per task, and a grinder like its 27B sibling.**
Differential 4/4 so far (15925 still running), including two passes (18827_741, 29618_781)
that ran 184–186 minutes, i.e. essentially the whole cap converted into a
win. The "converts time into wins" profile the 27B showed on RTX appears
here at 1/5th the speed.

**Its one fail is a protocol stumble, not a reasoning one.** On 28096_836
(the easiest probe task) it emitted a ```` ```python ```` text block instead
of a hermes tool call on turn one; the CLI session ended in ~21 min. A
direct API probe confirmed the serving stack's tool pipeline worked —
recorded as genuine 1.56 bpw tool-format instability. Its own pruned
derivative (REAP256) passed that same task.

**Housekeeping**: an earlier first batch was discarded for a harness defect
(stream idle timeout killing slow prefills) before any of these numbers;
disclosed in SELECTION.md. Serving is fork-only (`--moe-stream` is not in
mainline).

## 寸評(日本語)

**mac 側の最優秀アームで、27B と同じ「時間を勝ちに変える」型。**
differential ここまで 4/4(15925 走行中)。うち 18827_741 と 29618_781 は 184〜186分 —
cap をほぼ使い切っての合格で、速度1/5の環境で 27B と同じ粘り勝ち
プロファイルを見せた。

**唯一の負けは推論ではなくプロトコルの躓き。** 最も簡単な 28096_836 で
初手に hermes ツール呼び出しではなく ```` ```python ```` テキストを出して
CLI セッションが約21分で終了。API 直叩きでサーバ側ツール配管の正常は
確認済みなので、1.56bpw のツール形式不安定として記録。同じ問題を、
自分の枝刈り版(REAP256)は通している。

**注記**: これらの数字の前に、ハーネス欠陥(ストリーム無応答タイムアウト)
で1バッチ破棄している(SELECTION.md に開示)。配信は fork 限定
(`--moe-stream` は mainline 未収載)。
