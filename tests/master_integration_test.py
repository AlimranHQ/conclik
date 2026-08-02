import asyncio

from app.core.master_orchestrator.master_bootstrap import master_bootstrap
from app.core.master_orchestrator.master_registry import master_registry
import app.core.agents

print("=== Master Integration Test ===")

boot = master_bootstrap.boot()

assert boot["status"] == "boot_completed"

runtime = master_registry.get("master_runtime")

assert runtime is not None

result = asyncio.run(
    runtime.run("Build AI YouTube Automation")
)

print(result)

assert result["status"] == "accepted"
assert result["goal"]["status"] == "accepted"
assert result["plan"]["total_phases"] == 6
assert result["graph"]["total_nodes"] == 6

print("PASS | Master Integration")
