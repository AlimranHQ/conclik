import asyncio

from app.core.brain.assignment.assignment_engine import assignment_engine

print("=== Assignment Engine Test ===")


async def main():

    result = await assignment_engine.assign(
        "Build AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "assignment_ready"
    assert result["total_assignments"] == 6

    assert result["assignments"][0]["agent"] == "research_agent"
    assert result["assignments"][-1]["agent"] == "seo_agent"

    print("PASS | Assignment Engine working")


asyncio.run(main())
