import asyncio

from app.core.autonomous_loop.autonomous_runtime import autonomous_runtime

print("=== Autonomous Loop Test ===")

result = asyncio.run(
    autonomous_runtime.run(
        "Build Conclik AI Operating System"
    )
)

print(result)

assert result["steps"] == 6
assert result["cycle"][0] == "Goal Accepted"
assert result["cycle"][-1] == "Completed"

print("PASS | Autonomous Loop working")
