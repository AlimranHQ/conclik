import asyncio

from app.core.conclik_runtime.conclik_runtime import conclik_runtime

print("=== Intelligence Integration Wave-5 ===")


async def main():

    result = await conclik_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result)

    assert result["assignment"]["status"] == "assignment_ready"
    assert result["execution"]["completed"] == 6

    print("PASS | Assignment -> Execution Integration")


asyncio.run(main())
