# Environments

Wall-clock rollout caps interact with hardware speed: a `fail` on a slow
machine often means "did not finish before the cap", while the same cap is
never reached on a fast one. Columns therefore live in per-environment CSVs
under [`results/`](results/), and cross-environment comparisons should be read
with this table in hand.

| environment | hardware | engine | typical decode | cap reached in practice? |
|---|---|---|---|---|
| macstudio-512gb | Mac Studio M3 Ultra, 512 GB unified | llama.cpp (Metal, k3-stream fork) | ~3 tok/s (resident), ~2 tok/s (SSD-streamed) | often — 8/10 battle16 fails were cap-terminated |
| rtx6000-96gb | RTX PRO 6000 Blackwell 96 GB, DDR4 host | llama.cpp server-cuda (Docker) | 26-64 tok/s (model-dependent) | never |

## Measured speeds (rtx6000-96gb)

```csv
date,model,quant,size_gb,engine,ctx,prefill_tps,decode_tps,notes
2026-08-14,Gemma-4-31B-IT,NVFP4 (CISCai turbo),19.3,llama.cpp server-cuda,131072,358,63.9,"prefill on short prompts; decode stable during eval"
2026-08-15,Qwen3.8-27B,BF16 (unsloth),53.0,llama.cpp server-cuda,131072,285-1573,26-29,"29 fresh / 26 with long ctx during sweep; prefill 1573 with cache reuse"
```

## Per-run conditions

Same rows as the README leaderboard; fill your own rows in results/columns.csv.

<!-- RUNCONDITIONS:BEGIN -->
| column | agent | environment | ctx | sampling | avg min/task |
|---|---|---|---|---|---:|
| qwen38_27b_bf16_pi_promptv1 | pi | rtx6000-96gb | 131072 | temp 1.0 / top-p 0.95 | 43.8 |
| kimik3_streamed896_iq2xxs_18000s | Kimi Code CLI | macstudio-512gb | ? | ? | ? |
| kimik3_reap640_iq1s | Kimi Code CLI | macstudio-512gb | ? | ? | ? |
| kimik3_reap576_iq2xxs | Kimi Code CLI | macstudio-512gb | ? | ? | ? |
| kimik3_streamed896_iq2xxs_18000s_attempt2 | Kimi Code CLI | macstudio-512gb | ? | ? | ? |
| gemma4_31b_nvfp4_pi_promptv1 | pi | rtx6000-96gb | 131072 | temp 1.0 / top-p 0.95 | 6.2 |
| qwen38_a95b_udiq1s_10800s | ? | macstudio-512gb | ? | ? | ? |
| k27_q2_2bit | Kimi Code CLI | macstudio-512gb | ? | ? | ? |
| qwen38_reap256_iq1s_10800s | ? | macstudio-512gb | ? | ? | ? |
<!-- RUNCONDITIONS:END -->
