import asyncio

from app.core.brain.planner_engine import planner_engine

print("=== Brain Planner Test ===")


async def main():

    plan = await planner_engine.create_plan(
        "Build AI YouTube Automation"
    )

    print(plan)

    assert plan["total_phases"] == 6
    assert plan["phases"][0] == "Research"
    assert plan["phases"][-1] == "Optimization"

    print("PASS | Brain Planner working")


asyncio.run(main())
