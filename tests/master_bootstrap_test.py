import asyncio

from app.core.master_orchestrator.master_bootstrap import master_bootstrap
from app.core.master_orchestrator.master_registry import master_registry

print("=== Master Bootstrap Test ===")

boot = master_bootstrap.boot()

print(boot)

assert boot["status"] == "boot_completed"
assert "master_runtime" in boot["components"]

runtime = master_registry.get("master_runtime")

assert runtime is not None

result = asyncio.run(
    runtime.run("Build AI YouTube Automation")
)

print(result)

assert result["status"] == "accepted"

print("PASS | Master Bootstrap")
