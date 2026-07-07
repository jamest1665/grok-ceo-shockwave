import os
import subprocess
from typing import Any

import docker

from config import config


class ZeroTrustPolicy:
    """Zero-trust security policy for all agent actions.
    
    Enforces DRY_RUN, cost limits, and sandboxing.
    Production critical component.
    """

    def check(self, action: str, context: dict[str, Any] | None = None) -> bool:
        """Return True if action is allowed."""
        ctx = context or {}
        if config.DRY_RUN and any(
            keyword in action.lower() for keyword in ["git:write", "exec", "file:write", "deploy"]
        ):
            print(f"🚨 ZERO-TRUST BLOCKED (DRY_RUN): {action}")
            return False

        cost_estimate = ctx.get("cost_estimate", 0)
        if cost_estimate > config.MAX_USD_PER_CYCLE:
            print(f"⛔ Cost throttle: {cost_estimate} > {config.MAX_USD_PER_CYCLE}")
            return False

        return True

    def run_in_sandbox(self, command: str, workspace: str = ".") -> str:
        """Execute command in isolated environment.
        
        Prefers Docker with strict limits. Falls back to subprocess (warns).
        """
        if not config.SANDBOX:
            print("⚠️  WARNING: SANDBOX disabled — running on host (development only)")
            try:
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=30
                )
                return result.stdout + "\n" + result.stderr
            except Exception as e:
                return f"Host execution error: {e}"

        print("🐳 Executing in Docker sandbox (network_disabled, mem_limit)...")
        try:
            client = docker.from_env()
            container = client.containers.run(
                image="python:3.11-slim",
                command=command,
                volumes={os.path.abspath(workspace): {"bind": "/workspace", "mode": "rw"}},
                working_dir="/workspace",
                network_disabled=True,
                mem_limit="256m",
                cpu_quota=25000,  # ~25% CPU
                remove=True,
                detach=False,
            )
            if isinstance(container, (bytes, bytearray)):
                return container.decode("utf-8", errors="replace")
            return str(container)
        except Exception as e:
            return f"Docker sandbox error (is Docker daemon running?): {e}"


policy = ZeroTrustPolicy()