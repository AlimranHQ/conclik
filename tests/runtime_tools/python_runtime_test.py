import asyncio

from app.core.runtime_tools.python_runtime import python_runtime

print("=== Python Runtime Test ===")


async def main():

    result = await python_runtime.run(
        "print('Conclik Python Runtime')"
    )

    print(result)

    assert result["status"] == "completed"

    print("PASS | Python Runtime")


asyncio.run(main())
