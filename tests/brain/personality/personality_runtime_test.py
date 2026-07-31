import asyncio

from app.core.brain.personality.personality_runtime import personality_runtime

print("=== Personality Runtime Test ===")


async def main():

    result = await personality_runtime.load(
        "Optimize AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "ready"
    assert result["emotion"] == "OPTIMIZATION"
    assert result["personality"]["identity"] == "AI Operating System"

    print("PASS | Personality Runtime working")


asyncio.run(main())
