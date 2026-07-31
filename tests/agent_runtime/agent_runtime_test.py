import asyncio

from app.core.agent_runtime.agent_runtime import agent_runtime

print("=== Agent Runtime Test ===")


async def main():

    result = await agent_runtime.execute(
        "research_agent",
        "AI YouTube Automation"
    )

    print(result)

    assert result["status"] == "completed"

    print("PASS | Agent Runtime")


asyncio.run(main())
