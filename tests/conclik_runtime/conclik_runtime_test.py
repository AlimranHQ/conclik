import asyncio

from app.core.conclik_runtime.conclik_runtime import conclik_runtime

print("=== Conclik Runtime Test ===")


async def main():

    result = await conclik_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result["status"])

    assert result["status"] == "conclik_ready"

    print("PASS | Conclik Runtime")


asyncio.run(main())
