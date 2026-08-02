import asyncio

from app.core.collaboration.retry_engine.retry_engine import retry_engine


async def main():

    print("=== Retry Engine Test ===")


    await retry_engine.clear()


    registered = await retry_engine.register(
        "TASK-001"
    )

    assert registered["status"] == "registered"

    print("PASS | Retry Register")


    retry1 = await retry_engine.retry(
        "TASK-001",
        "network_error"
    )

    assert retry1["attempt"] == 1

    assert retry1["status"] == "retrying"

    print("PASS | Retry Attempt 1")


    retry2 = await retry_engine.retry(
        "TASK-001",
        "timeout"
    )

    assert retry2["attempt"] == 2

    print("PASS | Retry Attempt 2")


    retry3 = await retry_engine.retry(
        "TASK-001",
        "provider_error"
    )

    assert retry3["attempt"] == 3

    print("PASS | Retry Attempt 3")


    retry4 = await retry_engine.retry(
        "TASK-001",
        "final_failure"
    )

    assert retry4["status"] == "failed"

    print("PASS | Max Retry Protection")


    attempt = await retry_engine.get_attempt(
        "TASK-001"
    )

    assert attempt == 3

    print("PASS | Attempt Tracking")


    history = await retry_engine.get_history()

    assert len(history) == 4

    print("PASS | Retry History")


    print("PASS | Retry Engine Runtime")


if __name__ == "__main__":
    asyncio.run(main())
