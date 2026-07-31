import asyncio

from app.core.runtime_orchestrator.runtime_orchestrator import runtime_orchestrator

print("=== Runtime Orchestrator Test ===")


async def main():

    result = await runtime_orchestrator.run(
        "Build AI YouTube Automation"
    )

    print(result["status"])

    assert result["status"] == "runtime_completed"

    print("PASS | Runtime Orchestrator")


asyncio.run(main())
