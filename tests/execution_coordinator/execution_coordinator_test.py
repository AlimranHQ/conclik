import asyncio

from app.core.execution_coordinator.execution_runtime import execution_runtime

print("=== Execution Coordinator Test ===")

assignments = [
    {"task": "Research", "agent": "research_agent"},
    {"task": "Script", "agent": "script_agent"},
    {"task": "SEO", "agent": "seo_agent"},
    {"task": "Thumbnail", "agent": "thumbnail_agent"},
    {"task": "Voice", "agent": "voice_agent"},
    {"task": "Video", "agent": "video_agent"},
    {"task": "QA", "agent": "qa_agent"},
]

result = asyncio.run(
    execution_runtime.run(assignments)
)

print(result)

assert result["completed"] == 7
assert result["executed"][0]["status"] == "completed"

print("PASS | Execution Coordinator working")
