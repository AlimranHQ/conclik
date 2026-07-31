import asyncio

from app.core.runtime_tools.file_runtime import file_runtime

print("=== File Runtime Test ===")


async def main():

    await file_runtime.write(
        "runtime_test.txt",
        "Conclik File Runtime"
    )

    result = await file_runtime.read(
        "runtime_test.txt"
    )

    print(result)

    assert result["status"] == "completed"

    print("PASS | File Runtime")


asyncio.run(main())
