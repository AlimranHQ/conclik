"""
Event Dispatcher V2
"""

from app.core.collaboration.event_bus.event_bus import event_bus


class EventDispatcher:


    async def dispatch(self):

        event = await event_bus.consume()


        if event is None:

            return {
                "status": "empty"
            }


        if event.processed:

            return {
                "status": "duplicate_event",
                "event_id": event.event_id,
            }


        event.processed = True

        event_bus.history.add(
            event.event_id
        )


        return {

            "status": "dispatched",

            "event": event.name,

            "agent": event.source,

            "event_id": event.event_id,

            "payload": event.payload,

        }



event_dispatcher = EventDispatcher()
