import asyncio

from app.core.brain.runtime.brain_runtime import brain_runtime

print("=== Unified Brain Runtime ABI Test ===")


async def main():

    result = await brain_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "brain_ready"

    print("PASS | Unified Brain Runtime ABI")


asyncio.run(main())
