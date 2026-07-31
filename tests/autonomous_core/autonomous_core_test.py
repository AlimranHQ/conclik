import asyncio

from app.core.autonomous_core.autonomous_registry import autonomous_registry
from app.core.autonomous_core.autonomous_gateway import autonomous_gateway

print("=== Autonomous Core Test ===")


class DemoAutonomousCore:

    async def run(self, goal):
        return f"Autonomous Core executed: {goal}"


autonomous_registry.register(
    "demo",
    DemoAutonomousCore(),
)

result = asyncio.run(
    autonomous_gateway.run(
        "demo",
        "Build Conclik OS"
    )
)

print(result)

assert result == "Autonomous Core executed: Build Conclik OS"

print("PASS | Autonomous Core working")
