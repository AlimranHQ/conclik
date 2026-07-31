import asyncio

from app.core.kernel.base_engine import BaseEngine

print("=== Kernel ABI Test ===")


class DummyEngine(BaseEngine):

    async def run(self, goal):
        return {
            "goal": goal,
            "status": "ok"
        }


async def main():

    engine = DummyEngine()

    result = await engine.run("Kernel")

    print(result)

    assert result["status"] == "ok"

    print("PASS | Kernel ABI working")


asyncio.run(main())
