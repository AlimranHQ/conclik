import asyncio

from app.core.runtime_tools.terminal_runtime import terminal_runtime

print("=== Terminal Runtime Test ===")


async def main():

    result = await terminal_runtime.run("echo Conclik Runtime")

    print(result)

    assert result["status"] == "completed"

    print("PASS | Terminal Runtime")


asyncio.run(main())
