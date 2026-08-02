import asyncio

from app.core.collaboration.event_state.event_state import (
    event_state_tracker,
    EventStatus,
)


async def main():

    print("=== Event State Tracker Test ===")


    await event_state_tracker.clear()


    created = await event_state_tracker.create(
        "EVENT-001"
    )

    assert created["status"] == "pending"

    print("PASS | Event Create")


    running = await event_state_tracker.update(
        "EVENT-001",
        EventStatus.RUNNING
    )

    assert running["status"] == "running"

    print("PASS | State Running")


    completed = await event_state_tracker.update(
        "EVENT-001",
        EventStatus.COMPLETED
    )

    assert completed["status"] == "completed"

    print("PASS | State Complete")


    current = await event_state_tracker.get(
        "EVENT-001"
    )

    assert current["status"] == "completed"

    print("PASS | State Retrieve")


    history = await event_state_tracker.get_history()

    assert len(history) == 3

    print("PASS | State History")


    try:

        await event_state_tracker.update(
            "UNKNOWN",
            EventStatus.FAILED
        )

        assert False

    except ValueError:

        print("PASS | Invalid Event Protection")


    print("PASS | Event State Tracker Runtime")


if __name__ == "__main__":

    asyncio.run(main())
