import asyncio

from app.core.master_orchestrator.master_runtime import master_runtime

print("=== Master Orchestrator Test ===")

result = asyncio.run(
    master_runtime.run(
        "Build Conclik AI OS"
    )
)

print(result)

assert result["status"] == "accepted"

print("PASS | Master Orchestrator working")
