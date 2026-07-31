import asyncio

from app.core.result_flow.result_flow_runtime import result_flow_runtime

print("=== Result Flow Test ===")


async def main():

    result = await result_flow_runtime.flow(
        {
            "goal": "Build Conclik AI OS"
        }
    )

    print(result)

    assert result["status"] == "flowed"

    print("PASS | Result Flow working")


asyncio.run(main())
