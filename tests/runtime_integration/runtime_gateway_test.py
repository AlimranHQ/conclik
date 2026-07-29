import asyncio

from app.core.runtime_integration.runtime_registry import runtime_registry
from app.core.runtime_integration.runtime_gateway import runtime_gateway

print("=== Unified Runtime Gateway Test ===")

class DemoRuntime:

    async def run(self, topic):
        return f"Gateway executed: {topic}"

runtime_registry.register(
    "demo",
    DemoRuntime(),
)

result = asyncio.run(
    runtime_gateway.run(
        "demo",
        "Conclik OS"
    )
)

assert result == "Gateway executed: Conclik OS"

print(result)
print("PASS | Unified Runtime Gateway")
