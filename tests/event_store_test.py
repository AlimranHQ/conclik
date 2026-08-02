import asyncio
from datetime import datetime, timezone

from app.core.collaboration.event_store.event_record import EventRecord
from app.core.collaboration.event_store.event_store import event_store


async def main():

    print("=== Event Store Test ===")


    await event_store.clear()


    event = EventRecord(
        event_id="EVENT-001",
        event_type="research_completed",
        source="research_agent",
        payload={
            "goal": "AI Automation"
        },
        status="completed",
        created_at=datetime.now(timezone.utc),
    )


    result = await event_store.save(event)

    assert result["status"] == "stored"

    print("PASS | Event Save")


    stored = await event_store.get(
        "EVENT-001"
    )

    assert stored is not None

    assert stored.event_type == "research_completed"

    print("PASS | Event Retrieve")


    history = await event_store.all()

    assert len(history) == 1

    print("PASS | Event History")


    cleared = await event_store.clear()

    assert cleared["status"] == "cleared"

    print("PASS | Event Clear")


    print("PASS | Event Store Runtime")


if __name__ == "__main__":
    asyncio.run(main())
