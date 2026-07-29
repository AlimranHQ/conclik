import asyncio

from app.core.runtime_integration.runtime_registry import runtime_registry
from app.core.runtime_integration.runtime_gateway import runtime_gateway


class DemoRuntime:

    async def run(self, value):
        return f"Runtime OK: {value}"


runtime_registry.register(
    "demo",
    DemoRuntime(),
)

print("=== Runtime Integration Test ===")

result = asyncio.run(
    runtime_gateway.run(
        "demo",
        "Conclik"
    )
)

print(result)

assert result == "Runtime OK: Conclik"

print("PASS | Runtime Integration working")
