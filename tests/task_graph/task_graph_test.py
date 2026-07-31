import asyncio

from app.core.task_graph.task_graph_registry import task_graph_registry
from app.core.task_graph.task_graph_runtime import task_graph_runtime

print("=== Task Graph Test ===")


class DemoGraph:

    async def run(self, topic):
        return f"Task Graph executed: {topic}"


task_graph_registry.register(
    "demo",
    DemoGraph(),
)

result = asyncio.run(
    task_graph_runtime.run(
        "demo",
        "Conclik DAG"
    )
)

print(result)

assert result == "Task Graph executed: Conclik DAG"

print("PASS | Task Graph Runtime working")
