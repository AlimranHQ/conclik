import asyncio

from app.core.collaboration.event_state.event_state import (
    event_state_tracker,
    EventStatus,
)

from app.core.collaboration.failure_handler.failure_handler import (
    failure_handler,
    FailureType,
)

from app.core.collaboration.retry_engine.retry_engine import (
    retry_engine,
)

from app.core.collaboration.recovery.recovery_manager import (
    recovery_manager,
)



async def main():

    print("=== Reliability Integration Test ===")


    await event_state_tracker.clear()
    await failure_handler.clear()
    await retry_engine.clear()
    await recovery_manager.clear()



    # 1. Create Task State

    await event_state_tracker.create(
        "TASK-001"
    )

    print("PASS | State Initialized")



    # 2. Failure Capture

    failure = await failure_handler.capture(
        "TASK-001",
        "network timeout",
        FailureType.TRANSIENT,
    )

    assert failure["type"] == "transient"

    print("PASS | Failure Captured")



    # 3. Retry Decision

    retry_allowed = await failure_handler.should_retry(
        FailureType.TRANSIENT
    )

    assert retry_allowed is True

    print("PASS | Retry Approved")



    # 4. Retry Execution

    retry = await retry_engine.retry(
        "TASK-001",
        "network timeout"
    )

    assert retry["status"] == "retrying"

    print("PASS | Retry Executed")



    # 5. Update State

    state = await event_state_tracker.update(
        "TASK-001",
        EventStatus.RETRYING
    )

    assert state["status"] == "retrying"

    print("PASS | State Updated")



    # 6. Create Recovery Checkpoint

    checkpoint = await recovery_manager.create_checkpoint(
        "TASK-001",
        "retrying"
    )

    assert checkpoint["task_id"] == "TASK-001"

    print("PASS | Recovery Checkpoint")



    # 7. Recover

    recovered = await recovery_manager.recover(
        "TASK-001"
    )

    assert recovered["status"] == "recoverable"

    print("PASS | Recovery Successful")



    print("PASS | Reliability Integration Runtime")



if __name__ == "__main__":

    asyncio.run(main())
