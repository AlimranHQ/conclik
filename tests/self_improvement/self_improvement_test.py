import asyncio

from app.core.self_improvement.self_runtime import self_runtime

print("=== Self Improvement Test ===")


async def main():

    result = await self_runtime.run(
        {
            "score": 100,
            "reflection": "Execution successful.",
        }
    )

    print(result)

    assert result["improved"] is True
    assert result["action"] == "Keep current strategy"

    print("PASS | Self Improvement Engine working")


asyncio.run(main())
