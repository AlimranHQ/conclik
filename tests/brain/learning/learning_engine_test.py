import asyncio

from app.core.brain.learning.learning_engine import learning_engine

print("=== Learning Engine Test ===")


async def main():

    reflection = {
        "score": 100,
        "reflection": "Execution successful."
    }

    result = await learning_engine.learn(reflection)

    print(result)

    assert result["status"] == "learning_ready"
    assert result["action"] == "keep_strategy"

    print("PASS | Learning Engine working")


asyncio.run(main())
