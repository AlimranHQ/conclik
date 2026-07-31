import asyncio

from app.core.reasoning_engine.reasoning_registry import reasoning_registry
from app.core.reasoning_engine.reasoning_gateway import reasoning_gateway

print("=== Reasoning Engine Test ===")


class DemoReasoning:

    async def run(self, goal):
        return f"Reasoning completed: {goal}"


reasoning_registry.register(
    "demo",
    DemoReasoning(),
)

result = asyncio.run(
    reasoning_gateway.run(
        "demo",
        "Build Conclik AI Brain"
    )
)

print(result)

assert result == "Reasoning completed: Build Conclik AI Brain"

print("PASS | Reasoning Engine working")
