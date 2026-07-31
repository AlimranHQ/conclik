import asyncio

from app.core.reflection_engine.reflection_runtime import reflection_runtime

print("=== Reflection Engine Test ===")


async def main():

    result = await reflection_runtime.run(
        {"status": "completed"}
    )

    print(result)

    assert result["score"] == 100
    assert result["reflection"] == "Execution successful."

    print("PASS | Reflection Engine working")


asyncio.run(main())
