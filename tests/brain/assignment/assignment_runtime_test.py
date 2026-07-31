import asyncio

from app.core.brain.assignment.assignment_runtime import assignment_runtime

print("=== Assignment Runtime Test ===")


async def main():

    result = await assignment_runtime.run(
        "Build AI YouTube Automation"
    )

    print(result["status"])

    assert result["status"] == "assignment_completed"

    print("PASS | Assignment Runtime")


asyncio.run(main())
