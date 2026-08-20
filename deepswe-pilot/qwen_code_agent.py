"""Pier custom agent: Qwen Code CLI against an OpenAI-compatible endpoint.

Modeled on pier's GeminiCli (qwen-code is a gemini-cli fork); differences:
npm package, binary name, OpenAI-compat env config, ~/.qwen session dir.
Use with:  pier run ... --agent-import-path qwen_code_agent:QwenCode
"""
import shlex

from pier.agents.installed.base import with_prompt_template
from pier.agents.installed.gemini_cli import GeminiCli
from pier.agents.network import allowlist_from_urls
from pier.models.agent.install import AgentInstallSpec, InstallStep
from pier.models.agent.network import NetworkAllowlist


class QwenCode(GeminiCli):
    @staticmethod
    def name() -> str:
        return "qwen-code"

    def get_version_command(self) -> str | None:
        return ". ~/.nvm/nvm.sh; qwen --version"

    def install_spec(self) -> AgentInstallSpec:
        version_spec = f"@{self._version}" if self._version else "@latest"
        root_run = "apt-get update && apt-get install -y curl"
        agent_run = (
            "set -euo pipefail; "
            "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash && "
            'export NVM_DIR="$HOME/.nvm" && '
            '\\. "$NVM_DIR/nvm.sh" || true && '
            "command -v nvm &>/dev/null || { echo 'Error: NVM failed to load' >&2; exit 1; } && "
            "nvm install 20 && npm -v && "
            f"npm install -g @qwen-code/qwen-code{version_spec}"
        )
        return AgentInstallSpec(
            agent_name=self.name(),
            version=self._version,
            steps=[
                InstallStep(
                    user="root",
                    env={"DEBIAN_FRONTEND": "noninteractive"},
                    run=root_run,
                ),
                InstallStep(user="agent", run=agent_run),
                InstallStep(user="agent", run=". ~/.nvm/nvm.sh && qwen --version"),
            ],
            verification_command=self.get_version_command(),
        )

    def network_allowlist(self) -> NetworkAllowlist:
        return allowlist_from_urls(
            [self._get_env("OPENAI_BASE_URL"), self._get_env("OPENAI_API_BASE")]
        )

    @with_prompt_template
    async def run(self, instruction, environment, context) -> None:
        escaped_instruction = shlex.quote(instruction)

        model = self.model_name or ""
        if "/" in model:
            model = model.split("/")[-1]
        if not model:
            raise ValueError("Model name required (e.g. openai/qwen3.8-27b-nvfp4)")

        env = self.build_process_env(
            {
                "OPENAI_MODEL": model,

                "QWEN_CODE_SUPPRESS_YOLO_WARNING": "1",
            }
        )
        for var in ("OPENAI_BASE_URL", "OPENAI_API_BASE", "OPENAI_API_KEY"):
            if value := self._get_env(var):
                env[var] = value

        cli_flags = self.build_cli_flags()
        extra_flags = (cli_flags + " ") if cli_flags else ""
        try:
            await self.exec_as_agent(
                environment,
                command=(
                    ". ~/.nvm/nvm.sh; "
                    "echo Ly8gTWluaW1hbCBIVFRQIGZvcndhcmRlcjogbG9jYWxob3N0OjkwMDAgLT4gdXBzdHJlYW0gdmlhIEhUVFAgcHJveHkKLy8gKGFic29sdXRlLVVSSSBwcm94eWluZyB3aXRoIFByb3h5LUF1dGhvcml6YXRpb24pLCBzbyBjbGllbnRzIHdpdGggYnJva2VuCi8vIHByb3h5IHN1cHBvcnQgY2FuIHRhbGsgcGxhaW4gSFRUUCB0byBsb2NhbGhvc3QuCmNvbnN0IGh0dHAgPSByZXF1aXJlKCJodHRwIik7Cgpjb25zdCBUQVJHRVRfSE9TVCA9IHByb2Nlc3MuZW52LlNISU1fVEFSR0VUX0hPU1Q7IC8vIGUuZy4gMTcyLjE3LjAuMS5zc2xpcC5pbwpjb25zdCBUQVJHRVRfUE9SVCA9IHByb2Nlc3MuZW52LlNISU1fVEFSR0VUX1BPUlQgfHwgIjgwIjsKY29uc3QgcHJveHlVcmwgPSBuZXcgVVJMKHByb2Nlc3MuZW52LlNISU1fUFJPWFkpOyAvLyBlLmcuIGh0dHA6Ly9hZ2VudDp0b2tAZWdyZXNzLXByb3h5OjgwODAKCmNvbnN0IGF1dGggPQogIHByb3h5VXJsLnVzZXJuYW1lIHx8IHByb3h5VXJsLnBhc3N3b3JkCiAgICA/ICJCYXNpYyAiICsKICAgICAgQnVmZmVyLmZyb20oCiAgICAgICAgYCR7ZGVjb2RlVVJJQ29tcG9uZW50KHByb3h5VXJsLnVzZXJuYW1lKX06JHtkZWNvZGVVUklDb21wb25lbnQocHJveHlVcmwucGFzc3dvcmQpfWAKICAgICAgKS50b1N0cmluZygiYmFzZTY0IikKICAgIDogbnVsbDsKCmNvbnN0IHNlcnZlciA9IGh0dHAuY3JlYXRlU2VydmVyKChyZXEsIHJlcykgPT4gewogIGNvbnN0IGhlYWRlcnMgPSB7IC4uLnJlcS5oZWFkZXJzLCBob3N0OiBgJHtUQVJHRVRfSE9TVH06JHtUQVJHRVRfUE9SVH1gIH07CiAgaWYgKGF1dGgpIGhlYWRlcnNbInByb3h5LWF1dGhvcml6YXRpb24iXSA9IGF1dGg7CiAgY29uc3QgdXBzdHJlYW0gPSBodHRwLnJlcXVlc3QoCiAgICB7CiAgICAgIGhvc3Q6IHByb3h5VXJsLmhvc3RuYW1lLAogICAgICBwb3J0OiBwcm94eVVybC5wb3J0IHx8IDgwODAsCiAgICAgIG1ldGhvZDogcmVxLm1ldGhvZCwKICAgICAgcGF0aDogYGh0dHA6Ly8ke1RBUkdFVF9IT1NUfToke1RBUkdFVF9QT1JUfSR7cmVxLnVybH1gLAogICAgICBoZWFkZXJzLAogICAgfSwKICAgICh1cCkgPT4gewogICAgICByZXMud3JpdGVIZWFkKHVwLnN0YXR1c0NvZGUsIHVwLmhlYWRlcnMpOwogICAgICB1cC5waXBlKHJlcyk7CiAgICB9CiAgKTsKICB1cHN0cmVhbS5vbigiZXJyb3IiLCAoZSkgPT4gewogICAgcmVzLndyaXRlSGVhZCg1MDIsIHsgImNvbnRlbnQtdHlwZSI6ICJ0ZXh0L3BsYWluIiB9KTsKICAgIHJlcy5lbmQoInNoaW0gdXBzdHJlYW0gZXJyb3I6ICIgKyBlLm1lc3NhZ2UpOwogIH0pOwogIHJlcS5waXBlKHVwc3RyZWFtKTsKfSk7CgpzZXJ2ZXIubGlzdGVuKDkwMDAsICIxMjcuMC4wLjEiLCAoKSA9PiBjb25zb2xlLmxvZygic2hpbSBsaXN0ZW5pbmcgb24gOTAwMCIpKTsK | base64 -d > /tmp/proxy_shim.js && "
                    "SHIM_PROXY=\"${HTTPS_PROXY:-$HTTP_PROXY}\" "
                    "SHIM_TARGET_HOST=172.17.0.1.sslip.io SHIM_TARGET_PORT=80 "
                    "node /tmp/proxy_shim.js > /logs/agent/shim.log 2>&1 & "
                    "sleep 1; "
                    "unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy; export NO_PROXY=127.0.0.1; "
                    "export OPENAI_BASE_URL=http://127.0.0.1:9000/v1; "
                    f"qwen -y {extra_flags}{escaped_instruction} "
                    f"2>&1 </dev/null | stdbuf -oL tee /logs/agent/qwen-code.txt"
                ),
                env=env,
            )
        finally:
            try:
                await self.exec_as_agent(
                    environment,
                    command=(
                        "src=$(find ~/.qwen/tmp -type f "
                        "\\( -name '*.jsonl' -o -name '*.json' \\) "
                        "-printf '%T@ %p\\n' 2>/dev/null | sort -nr | head -n1 "
                        "| awk '{print $2}'); "
                        'if [ -n "$src" ]; then '
                        'cp "$src" "/logs/agent/qwen-code.trajectory.${src##*.}"; '
                        "fi"
                    ),
                )
            except Exception:
                pass

    def populate_context_post_run(self, context) -> None:
        # qwen-code's session format differs from gemini-cli's; skip the
        # gemini trajectory parsing rather than mis-parse.
        try:
            super().populate_context_post_run(context)
        except Exception:
            pass
