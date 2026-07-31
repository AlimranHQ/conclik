import asyncio

from app.core.orchestrator.orchestrator_registry import orchestrator_registry
from app.core.orchestrator.orchestrator_gateway import orchestrator_gateway

print("=== Orchestrator Test ===")


class DemoRuntime:

    async def run(self, value):
        return f"Orchestrator executed: {value}"


orchestrator_registry.register(
    "demo",
    DemoRuntime(),
)

result = asyncio.run(
    orchestrator_gateway.run(
        "demo",
        "Conclik Core"
    )
)

print(result)

assert result == "Orchestrator executed: Conclik Core"

print("PASS | Orchestrator working")
