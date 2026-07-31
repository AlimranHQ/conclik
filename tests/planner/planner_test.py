import asyncio

from app.core.planner.planner_registry import planner_registry
from app.core.planner.planner_gateway import planner_gateway

print("=== Planner Test ===")


class DemoPlanner:

    async def run(self, goal):
        return f"Planner created plan for: {goal}"


planner_registry.register(
    "demo",
    DemoPlanner(),
)

result = asyncio.run(
    planner_gateway.run(
        "demo",
        "Build AI Operating System"
    )
)

print(result)

assert result == "Planner created plan for: Build AI Operating System"

print("PASS | Planner working")
