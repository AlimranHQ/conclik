from datetime import datetime

from app.core.events.event import Event
from app.core.events.event_bus import event_bus
from app.core.events.event_queue import event_queue

print("=== Event Bus Test ===")

event = Event(
    name="system.start",
    source="test",
    payload={},
    timestamp=datetime.utcnow(),
)

event_bus.publish(event)

assert event_queue.pop() is not None

print("PASS | Event Bus working")
