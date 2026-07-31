import asyncio

from app.core.dependency_graph.dependency_registry import dependency_registry
from app.core.dependency_graph.dependency_runtime import dependency_runtime

print("=== Dependency Graph Test ===")


class DemoDependency:

    async def run(self, topic):
        return f"Dependency Graph executed: {topic}"


dependency_registry.register(
    "demo",
    DemoDependency(),
)

result = asyncio.run(
    dependency_runtime.run(
        "demo",
        "Conclik Dependency Engine"
    )
)

print(result)

assert result == "Dependency Graph executed: Conclik Dependency Engine"

print("PASS | Dependency Graph Runtime working")
