import asyncio

from app.core.collaboration.failure_handler.failure_handler import (
    failure_handler,
    FailureType,
    FailureSeverity,
)


async def main():

    print("=== Failure Handler Test ===")


    await failure_handler.clear()


    failure = await failure_handler.capture(
        "TASK-001",
        "network timeout",
        FailureType.TRANSIENT,
        FailureSeverity.HIGH,
    )


    assert failure["task_id"] == "TASK-001"

    assert failure["type"] == "transient"

    assert failure["severity"] == "high"

    print("PASS | Failure Capture")


    classification = await failure_handler.classify(
        "connection timeout"
    )


    assert classification == FailureType.TRANSIENT

    print("PASS | Failure Classification")


    retry = await failure_handler.should_retry(
        FailureType.TRANSIENT
    )


    assert retry is True

    print("PASS | Retry Decision")


    no_retry = await failure_handler.should_retry(
        FailureType.PERMANENT
    )


    assert no_retry is False

    print("PASS | Permanent Failure Protection")


    history = await failure_handler.history()


    assert len(history) == 1

    print("PASS | Failure History")


    print("PASS | Failure Handler Runtime")


if __name__ == "__main__":

    asyncio.run(main())
