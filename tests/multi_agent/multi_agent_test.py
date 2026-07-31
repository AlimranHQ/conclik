import asyncio

from app.core.multi_agent.multi_agent_runtime import multi_agent_runtime

print("=== Multi-Agent Planner Test ===")

tasks = [
    "Research",
    "Script",
    "SEO",
    "Thumbnail",
    "Voice",
    "Video",
    "QA",
]

result = asyncio.run(
    multi_agent_runtime.run(tasks)
)

print(result)

assignments = result["assignments"]

assert assignments[0]["agent"] == "research_agent"
assert assignments[1]["agent"] == "script_agent"
assert assignments[2]["agent"] == "seo_agent"
assert assignments[3]["agent"] == "thumbnail_agent"
assert assignments[4]["agent"] == "voice_agent"
assert assignments[5]["agent"] == "video_agent"
assert assignments[6]["agent"] == "qa_agent"

print("PASS | Multi-Agent Planner working")
