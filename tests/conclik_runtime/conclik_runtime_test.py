import asyncio

from app.core.ai_runtime import ai_runtime

print("=== AI Runtime Test ===")


async def main():
    result = await ai_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result["status"])

    assert result["status"] == "runtime_ready"

    print("PASS | AI Runtime")


asyncio.run(main())
