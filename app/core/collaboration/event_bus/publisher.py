from app.core.collaboration.event_bus.event import Event
from app.core.collaboration.event_bus.event_bus import event_bus


class EventPublisher:

    async def publish(
        self,
        event_type,
        source,
        payload,
    ):

        event = Event(
            type=event_type,
            source=source,
            payload=payload,
        )

        return await event_bus.publish(
            event
        )


publisher = EventPublisher()
