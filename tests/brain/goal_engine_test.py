import asyncio

from app.core.brain.goal_engine import goal_engine
from app.core.brain.goal_classifier import goal_classifier
from app.core.brain.goal_priority import goal_priority

print("=== Brain Goal Engine Test ===")


async def main():

    goal = "Build AI YouTube Automation"

    result = await goal_engine.analyze(goal)

    result["category"] = await goal_classifier.classify(goal)

    result["priority"] = await goal_priority.detect(goal)

    print(result)

    assert result["status"] == "accepted"
    assert result["category"] == "content"
    assert result["priority"] == "high"

    print("PASS | Brain Goal Engine working")


asyncio.run(main())
