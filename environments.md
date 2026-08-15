# Environments

Wall-clock rollout caps interact with hardware speed: a `fail` on a slow
machine often means "did not finish before the cap", while the same cap is
never reached on a fast one. Columns therefore live in per-environment CSVs
under [`results/`](results/), and cross-environment comparisons should be read
with this table in hand.

| environment | hardware | engine | typical decode | cap reached in practice? |
|---|---|---|---|---|
| macstudio-512gb | Mac Studio M3 Ultra, 512 GB unified | llama.cpp (Metal, k3-stream fork) | ~3 tok/s resident; streamed arm ~2/3 of that | often — source repo reports 8/10 reap576 battle16 fails were cap-terminated |
| rtx6000-96gb | RTX PRO 6000 Blackwell 96 GB, DDR4 host | llama.cpp server-cuda (Docker) | 26-64 tok/s (model-dependent) | never |

## Measured speeds (rtx6000-96gb)

```csv
date,model,quant,size_gb,engine,ctx,prefill_tps,decode_tps,notes
2026-08-14,Gemma-4-31B-IT,NVFP4 (CISCai turbo),19.3,llama.cpp server-cuda,131072,358,63.9,"prefill on short prompts; decode stable during eval"
2026-08-15,Qwen3.8-27B,BF16 (unsloth),53.0,llama.cpp server-cuda,131072,285-1573,26-29,"29 fresh / 26 with long ctx during sweep; prefill 1573 with cache reuse"
```


All macstudio-512gb figures are quoted from the source repo's [SELECTION.md](SELECTION.md)/[REPLICATION.md](REPLICATION.md); nothing in that row was measured by the rtx6000 side.

## Measured speeds (macstudio-512gb)

First-hand measurements from the mac side (complements the quoted-figures note above):

```csv
date,model,quant,size_gb,engine,ctx,prefill_tps,decode_tps,notes
2026-08-08,Kimi-K3-REAP576,UD-IQ2_XXS,478.5,llama.cpp k3-stream (Metal),131072,48.3,2.98,"resident"
2026-08-13,Qwen3.8-2.4T-A95B,UD-IQ1_S,508,llama.cpp k3-stream (Metal),131072,,5.3-6.3,"--moe-stream cache 400 GiB; decode range over agentic workload"
2026-08-15,Qwen3.8-REAP-256GB,IQ1_S,246,llama.cpp (Metal),4096,23.2-23.3,9.6-10.0,"resident; llama-cli single-shot smoke (48-token gen), fork and stock mainline"
```

## Per-run conditions

Same rows as the README leaderboard; fill your own rows in results/columns.csv.

macstudio avg-min figures are wall time from task start to grading end
(run-dir birth → results.csv mtime in the harness `runs/` archive), so they
include SWE-Lancer grading time on top of the agent rollout; rollout caps
therefore bound them only loosely (a capped 180 min rollout can show ~185-190
min here, more when grading is heavy).

<!-- RUNCONDITIONS:BEGIN -->
| column | agent | environment | ctx | sampling | avg min/task probe3 | avg min/task all24 |
|---|---|---|---|---|---:|---:|
| qwen38_27b_bf16_pi_promptv1 | pi | rtx6000-96gb | 131072 | temp 1.0 / top-p 0.95 | 15.0 | 43.8 |
| kimik3_reap640_iq1s | Kimi Code CLI | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 | ? | ? |
| kimik3_streamed896_iq2xxs_18000s | Kimi Code CLI | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 | 185.0 | ? |
| kimik3_reap576_iq2xxs | Kimi Code CLI | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 | ? | ? |
| kimik3_streamed896_iq2xxs_18000s_attempt2 | Kimi Code CLI | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 | ? | ? |
| gemma4_31b_nvfp4_pi_promptv1 | pi | rtx6000-96gb | 131072 | temp 1.0 / top-p 0.95 | 4.3 | 6.2 |
| qwen38_a95b_udiq1s_10800s | Qwen Code CLI 0.21.10-0.21.11 | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 / top-k 20 | 130.3 | ? |
| k27_q2_2bit | Kimi Code CLI | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 | ? | ? |
| qwen38_reap256_iq1s_10800s | Qwen Code CLI 0.21.11 | macstudio-512gb | 131072 | temp 1.0 / top-p 0.95 / top-k 20 | 88.0 | ? |
<!-- RUNCONDITIONS:END -->
