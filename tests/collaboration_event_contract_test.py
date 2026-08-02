import asyncio

from app.core.collaboration.event_bus.event_bus import event_bus
from app.core.collaboration.event_bus.publisher import publisher
from app.core.collaboration.dispatcher.event_dispatcher import event_dispatcher


CHAIN = [
    ("research_completed", "research_agent"),
    ("script_completed", "script_agent"),
    ("seo_completed", "seo_agent"),
    ("thumbnail_completed", "thumbnail_agent"),
    ("voice_completed", "voice_agent"),
    ("video_completed", "video_agent"),
    ("qa_completed", "qa_agent"),
]


async def main():

    print("=== Collaboration Event Contract Test ===")


    await event_bus.clear()


    agents = []


    for event_type, expected_agent in CHAIN:


        await publisher.publish(
            event_type,
            expected_agent,
            {
                "goal": "AI Automation"
            }
        )


        result = await event_dispatcher.dispatch()


        assert result["status"] == "dispatched"


        agents.append(
            result["agent"]
        )


    expected = [
        "research_agent",
        "script_agent",
        "seo_agent",
        "thumbnail_agent",
        "voice_agent",
        "video_agent",
        "qa_agent",
    ]


    print("CHAIN:", agents)


    assert agents == expected


    print("PASS | Event Contract Stable")


if __name__ == "__main__":
    asyncio.run(main())
