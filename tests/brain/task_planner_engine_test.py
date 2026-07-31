import asyncio

from app.core.brain.task_planner_engine import task_planner_engine

print("=== Brain Task Planner Integration Test ===")


async def main():

    result = await task_planner_engine.create_graph(
        "Build AI YouTube Automation"
    )

    print(result)

    assert result["total_nodes"] == 6
    assert result["graph"][0]["task"] == "Research"
    assert result["graph"][-1]["task"] == "Optimization"

    print("PASS | Brain Task Planner Integration working")


asyncio.run(main())
