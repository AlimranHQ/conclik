from app.core.collaboration.event_bus.event_bus import event_bus


class EventSubscriber:

    async def receive(self):

        return await event_bus.consume()


subscriber = EventSubscriber()
