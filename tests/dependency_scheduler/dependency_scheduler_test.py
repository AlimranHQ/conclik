import asyncio

from app.core.dependency_scheduler.dependency_runtime import dependency_runtime

print("=== Dependency Scheduler Test ===")

tasks = [
    "Research",
    "Planning",
    "Script",
    "SEO",
    "Thumbnail",
    "Voice",
    "Video",
    "QA",
    "Publish",
]

result = asyncio.run(
    dependency_runtime.run(tasks)
)

print(result)

assert result["groups"] == 7
assert "SEO" in result["parallel_groups"][3]
assert "Thumbnail" in result["parallel_groups"][3]
assert "Voice" in result["parallel_groups"][3]

print("PASS | Dependency Scheduler working")
