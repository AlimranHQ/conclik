import asyncio

from app.core.brain.personality.personality_engine import personality_engine

print("=== Personality Engine Test ===")


async def main():

    result = await personality_engine.initialize()

    print(result)

    assert result["status"] == "personality_ready"

    assert result["profile"]["identity"] == "AI Operating System"

    assert result["profile"]["traits"]["logical"]

    print("PASS | Personality Engine working")


asyncio.run(main())
