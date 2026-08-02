import asyncio

from app.core.collaboration.recovery.recovery_manager import (
    recovery_manager,
)


async def main():

    print("=== Recovery Manager Test ===")


    await recovery_manager.clear()


    checkpoint = await recovery_manager.create_checkpoint(
        "TASK-001",
        "completed_research",
        {
            "agent": "research_agent"
        }
    )


    assert checkpoint["task_id"] == "TASK-001"

    assert checkpoint["state"] == "completed_research"

    print("PASS | Checkpoint Create")


    failure = await recovery_manager.record_failure(
        "TASK-002",
        "agent_timeout"
    )


    assert failure["status"] == "failed"

    print("PASS | Failure Record")


    recovery = await recovery_manager.recover(
        "TASK-001"
    )


    assert recovery["status"] == "recoverable"

    assert recovery["checkpoint"]["task_id"] == "TASK-001"

    print("PASS | Recovery Lookup")


    missing = await recovery_manager.recover(
        "UNKNOWN"
    )


    assert missing["status"] == "not_found"

    print("PASS | Missing Task Protection")


    failures = await recovery_manager.get_failures()

    assert len(failures) == 1

    print("PASS | Failure History")


    print("PASS | Recovery Manager Runtime")


if __name__ == "__main__":

    asyncio.run(main())
