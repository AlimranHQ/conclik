import asyncio

from app.core.brain.emotion.emotion_engine import emotion_engine

print("=== Emotion Engine Test ===")


async def main():

    result = await emotion_engine.evaluate(
        "Optimize AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "emotion_ready"
    assert result["mode"] == "OPTIMIZATION"

    print("PASS | Emotion Engine working")


asyncio.run(main())
