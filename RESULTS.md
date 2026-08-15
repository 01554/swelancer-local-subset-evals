# Results

Auto-generated from [`results/*.csv`](results/) by `scripts/render_results.py` — edit those, not this file.

✅ pass ❌ fail ⏱️ timeout (rollout cap hit, unfinished) 🔄 running — not run

## Leaderboard

| column | environment | pass | earned |
|---|---|---:|---:|
| qwen38_27b_bf16_pi_promptv1 | rtx6000-96gb | 17/24 | $48,000 |
| streamed896_iq2xxs_18000s | macstudio-512gb | 7/11 | $35,750 |
| reap640_iq1s | macstudio-512gb | 6/10 | $35,500 |
| reap576_iq2xxs | macstudio-512gb | 13/24 | $19,000 |
| streamed896_iq2xxs_18000s_attempt2 | macstudio-512gb | 3/3 | $10,000 |
| gemma4_31b_nvfp4_pi_promptv1 | rtx6000-96gb | 7/24 | $9,250 |
| qwen38_a95b_udiq1s_10800s | macstudio-512gb | 5/6 | $7,000 |
| k27_q2_2bit | macstudio-512gb | 3/24 | $2,000 |
| qwen38_reap256_iq1s_10800s | macstudio-512gb | 3/8 | $2,000 |

## macstudio-512gb

| task | set | $ | k27_q2_2bit | reap640_iq1s | reap576_iq2xxs | streamed896_iq2xxs_18000s | streamed896_iq2xxs_18000s_attempt2 | qwen38_a95b_udiq1s_10800s | qwen38_reap256_iq1s_10800s |
|---|---|---:|---|---|---|---|---|---|---|
| 28096_836 | probe | 500 | ✅ | ✅ | ✅ | ✅ | · | ❌ | ✅ |
| 18827_741 | probe | 1,000 | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ |
| 29618_781 | probe | 500 | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ |
| 14294 | differential | 4,000 | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| 24508_791 | differential | 1,000 | ❌ | ✅ | ✅ | ✅ | · | ✅ | ❌ |
| 15815_1 | differential | 4,000 | ❌ | ❌ | ✅ | ❌ | ✅ | pending | ❌ |
| 27353_776 | differential | 500 | ❌ | ✅ | ❌ | ✅ | · | ✅ | ❌ |
| 15925 | differential | 2,000 | ❌ | ❌ | ✅ | ❌ | ✅ | pending | ❌ |
| 29916_609 | battle16 | 500 | ❌ | ❌ | ❌ | ❌ | · | · | · |
| 6883 | battle16 | 32,000 | ❌ | ✅ | ❌ | ✅ | · | · | · |
| 43395_530 | battle16 | 250 | ❌ | 🔄 | ✅ | ✅ | · | · | · |
| 25901_945 | battle16 | 2,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 40259_1089 | battle16 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 18746_833 | battle16 | 1,000 | ❌ | 🔄 | ❌ | — | · | · | · |
| 4324 | battle16 | 2,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 44429_1100 | battle16 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 40208_1108 | battle16 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 44618_1007 | battle16 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 19132_872 | battle16 | 1,000 | ❌ | 🔄 | ✅ | — | · | · | · |
| 41885_1134 | battle16 | 500 | ❌ | 🔄 | ✅ | — | · | · | · |
| 50064_846 | battle16 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 50314_790 | battle16 | 250 | ❌ | 🔄 | ❌ | — | · | · | · |
| 37688_441 | battle16 | 500 | ❌ | 🔄 | ❌ | — | · | · | · |
| 44040_470 | battle16 | 250 | ❌ | 🔄 | ✅ | — | · | · | · |
| **pass** | | | **3/24** | **6/10** | **13/24** | **7/11** | **3/3** | **5/6** | **3/8** |
| **earned** | | | $2,000 | $35,500 | $19,000 | $35,750 | $10,000 | $7,000 | $2,000 |
| **timeouts** | | | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## rtx6000-96gb

| task | set | $ | gemma4_31b_nvfp4_pi_promptv1 | qwen38_27b_bf16_pi_promptv1 |
|---|---|---:|---|---|
| 28096_836 | probe | 500 | ✅ | ✅ |
| 18827_741 | probe | 1,000 | ❌ | ✅ |
| 29618_781 | probe | 500 | ✅ | ✅ |
| 14294 | differential | 4,000 | ✅ | ✅ |
| 24508_791 | differential | 1,000 | ✅ | ✅ |
| 15815_1 | differential | 4,000 | ❌ | ✅ |
| 27353_776 | differential | 500 | ❌ | ❌ |
| 15925 | differential | 2,000 | ✅ | ❌ |
| 29916_609 | battle16 | 500 | ❌ | ✅ |
| 6883 | battle16 | 32,000 | ❌ | ✅ |
| 43395_530 | battle16 | 250 | ❌ | ❌ |
| 25901_945 | battle16 | 2,000 | ❌ | ❌ |
| 40259_1089 | battle16 | 500 | ❌ | ✅ |
| 18746_833 | battle16 | 1,000 | ❌ | ✅ |
| 4324 | battle16 | 2,000 | ❌ | ❌ |
| 44429_1100 | battle16 | 250 | ❌ | ✅ |
| 40208_1108 | battle16 | 500 | ❌ | ✅ |
| 44618_1007 | battle16 | 250 | ✅ | ❌ |
| 19132_872 | battle16 | 1,000 | ✅ | ✅ |
| 41885_1134 | battle16 | 500 | ❌ | ❌ |
| 50064_846 | battle16 | 250 | ❌ | ✅ |
| 50314_790 | battle16 | 250 | ❌ | ✅ |
| 37688_441 | battle16 | 500 | ❌ | ✅ |
| 44040_470 | battle16 | 250 | ❌ | ✅ |
| **pass** | | | **7/24** | **17/24** |
| **earned** | | | $9,250 | $48,000 |
| **timeouts** | | | 0 | 0 |

