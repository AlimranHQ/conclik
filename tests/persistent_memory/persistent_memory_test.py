import asyncio

from app.core.persistent_memory.memory_runtime import memory_runtime

print("=== Persistent Memory Test ===")


async def main():

    await memory_runtime.remember(
        "project",
        "Conclik AI Operating System",
    )

    value = await memory_runtime.recall(
        "project",
    )

    print(value)

    assert value == "Conclik AI Operating System"

    print("PASS | Persistent Memory working")


asyncio.run(main())
