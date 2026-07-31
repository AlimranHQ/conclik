import asyncio

from app.core.brain.conversation.conversation_engine import conversation_engine

print("=== Reflection Conversation Test ===")


async def main():

    result = await conversation_engine.respond(
        "Build Conclik AI Operating System"
    )

    print(result)

    assert result["status"] == "response_ready"

    print("PASS | Reflection-aware Conversation working")


asyncio.run(main())
