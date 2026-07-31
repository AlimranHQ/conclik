import asyncio

from app.core.result_aggregator.result_runtime import result_runtime

print("=== Result Aggregator Test ===")

executed = [
    {"task": "Research", "agent": "research_agent", "status": "completed"},
    {"task": "Script", "agent": "script_agent", "status": "completed"},
    {"task": "SEO", "agent": "seo_agent", "status": "completed"},
]

result = asyncio.run(
    result_runtime.run(executed)
)

print(result["summary"])

assert result["total"] == 3

print("PASS | Result Aggregator working")
