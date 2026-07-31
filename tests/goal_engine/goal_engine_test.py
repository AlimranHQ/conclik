import asyncio

from app.core.goal_engine.goal_runtime import goal_runtime

print("=== Goal Engine Test ===")

result = asyncio.run(
    goal_runtime.run(
        "Build a YouTube automation system"
    )
)

print(result)

assert result["total_tasks"] == 9
assert "Research" in result["tasks"]
assert "Publish" in result["tasks"]

print("PASS | Goal Decomposition working")
