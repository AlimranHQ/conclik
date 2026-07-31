import asyncio

from app.core.workflow_engine.workflow_runtime import workflow_runtime

print("=== Workflow Engine Test ===")

workflow = [
    "Goal",
    "Reasoning",
    "Planning",
    "Task Graph",
    "Dependency",
    "Agent Planner",
    "Execution",
    "Aggregation",
]

result = asyncio.run(
    workflow_runtime.run(workflow)
)

print(result)

assert result["steps"] == 8
assert result["workflow"][0] == "Goal"
assert result["workflow"][-1] == "Aggregation"

print("PASS | Workflow Engine working")
