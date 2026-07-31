import asyncio

from app.core.task_planner.task_runtime import task_runtime

print("=== Task Planner Test ===")

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
    task_runtime.run(tasks)
)

print(result)

assert result["total_nodes"] == 9
assert result["graph"][0]["task"] == "Research"
assert result["graph"][-1]["task"] == "Publish"

print("PASS | Task Planner working")
