import asyncio

from app.core.agent_runtime.agent_runtime import agent_runtime
from app.core.agent_runtime.agent_registry import agent_registry


class DummyAgent:

    async def run(self, task):
        return "hello runtime"


async def main():

    agent_registry.register(
        "dummy_agent",
        DummyAgent()
    )

    result = await agent_runtime.execute(
        "dummy_agent",
        "AI Automation"
    )

    assert result == "hello runtime"

    print("PASS | Agent Runtime")


asyncio.run(main())
