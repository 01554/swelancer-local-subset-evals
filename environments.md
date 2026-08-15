# Environments

Wall-clock rollout caps interact with hardware speed: a `fail` on a slow
machine often means "did not finish before the cap", while the same cap is
never reached on a fast one. Columns therefore live in per-environment CSVs
under [`results/`](results/), and cross-environment comparisons should be read
with this table in hand.

| environment | hardware | engine | typical decode | cap reached in practice? |
|---|---|---|---|---|
| macstudio-512gb | Mac Studio M3 Ultra, 512 GB unified (driven remotely from devbox) | llama.cpp (Metal, k3-stream fork) | ~3 tok/s (resident), ~2 tok/s (SSD-streamed) | often — 8/10 battle16 fails were cap-terminated |
| rtx6000-96gb | RTX PRO 6000 Blackwell 96 GB, DDR4 host | llama.cpp server-cuda (Docker) | 26-64 tok/s (model-dependent) | never |

## Measured speeds (rtx6000-96gb)

```csv
date,model,quant,size_gb,engine,ctx,prefill_tps,decode_tps,notes
2026-08-14,Gemma-4-31B-IT,NVFP4 (CISCai turbo),19.3,llama.cpp server-cuda,131072,358,63.9,"prefill on short prompts; decode stable during eval"
2026-08-15,Qwen3.8-27B,BF16 (unsloth),53.0,llama.cpp server-cuda,131072,285-1573,26-29,"29 fresh / 26 with long ctx during sweep; prefill 1573 with cache reuse"
```
