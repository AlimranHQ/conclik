import asyncio

from app.core.brain.learning.learning_runtime import learning_runtime

print("=== Learning Runtime Test ===")


async def main():

    reflection = {
        "score": 100,
        "reflection": "Execution successful."
    }

    result = await learning_runtime.process(reflection)

    print(result)

    assert result["status"] == "learning_completed"
    assert result["memory_updated"] is True

    print("PASS | Learning Runtime working")


asyncio.run(main())
