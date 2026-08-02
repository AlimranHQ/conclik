import asyncio

from app.core.master_orchestrator.reliability.master_reliability import (
    master_reliability,
)


async def main():

    print("=== Master Reliability Test ===")


    await master_reliability.clear()


    started = await master_reliability.start_task(
        "MASTER-TASK-001"
    )


    assert started["status"] == "started"

    print("PASS | Master Task Start")



    failure = await master_reliability.handle_failure(
        "MASTER-TASK-001",
        "network timeout"
    )


    assert failure["status"] == "retrying"

    assert failure["retry"]["status"] == "retrying"

    print("PASS | Failure Retry Flow")



    recovered = await master_reliability.recover_task(
        "MASTER-TASK-001"
    )


    assert recovered["status"] == "recoverable"

    print("PASS | Recovery Lookup")



    second_failure = await master_reliability.handle_failure(
        "MASTER-TASK-002",
        "permission denied"
    )


    assert second_failure["status"] == "failed"

    print("PASS | Permanent Failure Handling")



    print("PASS | Master Reliability Runtime")



if __name__ == "__main__":

    asyncio.run(main())
