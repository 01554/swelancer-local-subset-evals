# DeepSWE 1.1 pilot (2026-08) — plumbing validation & qwen-code custom agent

Pilot for migrating this observatory to [DeepSWE 1.1](https://github.com/datacurve-ai/deep-swe)
after SWE-Lancer saturation. Everything ran on the same rig (RTX PRO 6000,
local vLLM serving Qwen3.8-27B-NVFP4, screening config: temp 0.6 / MTP / prefix cache).

## Pilot results

| task | language | agent | f2p | p2p |
|---|---|---|---|---|
| abs-stepped-slices | Go | oracle | 6/6 | 6/6 |
| abs-stepped-slices | Go | mini-swe-agent | 2/6 | 6/6 |
| adaptix-name-mapping-aliases | Python | mini-swe-agent | 43/44 | all |
| awilix-async-container-initialization | TS | mini-swe-agent | 23/24 | all |
| **abs-stepped-slices** | Go | **qwen-code (custom agent)** | **6/6** | **6/6** |

The harness effect carries over to DeepSWE from the very first datapoint:
same model, same task — mini-swe-agent 2/6 vs Qwen Code 6/6.

## Files

- `qwen_code_agent.py` — Pier custom agent (`--agent-import-path qwen_code_agent:QwenCode`),
  subclassing pier's GeminiCli (qwen-code is a gemini-cli fork)
- `proxy_shim.js` — required workaround: qwen-code's proxy client crashes with
  `[API Error: Value of "this" must be of DOMException]` against Pier's squid
  egress proxy (reproduced on node 20/22 and qwen-code 0.21.11/latest, with
  env-proxy and `--proxy` alike). The shim listens on `127.0.0.1:9000` inside
  the sandbox and re-issues requests as absolute-URI HTTP through the proxy
  with `Proxy-Authorization` — the same wire path mini-swe-agent uses
- `pier.env` needs `OPENAI_BASE_URL=http://<host>.sslip.io/v1` — Pier's squid
  only allows ports 80/443 (`Safe_ports`) and matches `dstdomain` (not raw
  IPs), so the LLM server must be exposed on port 80 under a DNS-resolvable
  name; `<bridge-ip>.sslip.io` does the trick

## Not yet done

- pi as a Pier custom agent: same pattern should work (BaseInstalledAgent +
  npm install + models.json write + the shim); untested
- Full 113-task runs / quantization matrix on DeepSWE: pending a decision on
  where results live (this repo is SWE-Lancer-named)
