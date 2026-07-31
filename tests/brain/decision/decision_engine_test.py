import asyncio

from app.core.brain.decision.decision_engine import decision_engine

print("=== Decision Engine Test ===")


async def main():

    result = await decision_engine.decide(
        "Build AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "decision_ready"
    assert result["mode"] == "content_pipeline"
    assert result["total_agents"] == 7

    print("PASS | Decision Engine working")


asyncio.run(main())
