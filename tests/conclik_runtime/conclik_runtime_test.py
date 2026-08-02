import asyncio

from app.core.conclik_runtime.conclik_runtime import conclik_runtime

print("=== AI Runtime Test ===")


async def main():

    result = await conclik_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result["status"])

    assert result["status"] == "runtime_ready"

    print("PASS | AI Runtime")


asyncio.run(main())
