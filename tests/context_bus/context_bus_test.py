import asyncio

from app.core.context_bus.context_runtime import context_runtime

print("=== Context Bus Test ===")


async def main():

    await context_runtime.set(
        "goal",
        "Build Conclik AI OS",
    )

    value = await context_runtime.get(
        "goal",
    )

    print(value)

    assert value == "Build Conclik AI OS"

    print("PASS | Context Bus working")


asyncio.run(main())
