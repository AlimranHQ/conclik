import asyncio

from datetime import datetime

from app.core.events.event import Event
from app.core.events.event_dispatcher import event_dispatcher


async def main():


    event_dispatcher.register(
        "content_creation",
        [
            "research_agent",
            "script_agent",
            "seo_agent",
            "qa_agent",
        ]
    )


    event = Event(
        name="content_creation",
        source="conclik",
        payload={
            "task": "Create YouTube Automation Strategy"
        },
        timestamp=datetime.now()
    )


    result = await event_dispatcher.dispatch(event)


    print(result)



if __name__ == "__main__":

    asyncio.run(main())
