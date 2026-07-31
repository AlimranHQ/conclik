import asyncio

from app.core.brain.adaptive.adaptive_engine import adaptive_engine

print("=== Adaptive Engine Test ===")


async def main():

    learning = {
        "action": "keep_strategy"
    }

    result = await adaptive_engine.evolve(
        learning
    )

    print(result)

    assert result["status"] == "adaptive_ready"
    assert result["mode"] == "stable"

    print("PASS | Adaptive Engine working")


asyncio.run(main())
