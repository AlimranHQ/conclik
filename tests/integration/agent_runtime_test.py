import asyncio

from app.core.agent_runtime.agent_manager import agent_manager
from app.core.agent_runtime.agent_runtime import agent_runtime


class DemoAgent:

    async def run(self):
        return "hello conclik"


print("=== Agent Runtime Test ===")

agent_manager.register("demo", DemoAgent())

result = asyncio.run(agent_runtime.run("demo"))

assert result == "hello conclik"

print("PASS | Agent Runtime working")
