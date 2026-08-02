import asyncio

from app.core.autonomous.goal_orchestrator.goal_orchestrator import (
    goal_orchestrator,
)



async def main():

    print("=== Goal Orchestrator Test ===")


    await goal_orchestrator.clear()



    # Test 1: Full Goal Execution

    result = await goal_orchestrator.execute(
        "GOAL-001",
        "Build AI YouTube Automation"
    )


    assert result["status"] == "completed"

    assert result["goal_id"] == "GOAL-001"

    print("PASS | Goal Execution")



    # Test 2: Goal Completion State

    assert (
        result["goal_state"]["status"]
        == "completed"
    )


    assert (
        result["goal_state"]["progress"]
        == 100
    )


    print("PASS | Goal Completion State")



    # Test 3: Control Loop Integration

    assert result["cycles"] == 1

    print("PASS | Control Loop Integration")



    # Test 4: Supervisor Integration

    assert result["health"] == "healthy"

    print("PASS | Supervisor Integration")



    # Test 5: History

    history = await goal_orchestrator.history()


    assert len(history) == 1

    print("PASS | Execution History")



    # Test 6: Reset

    cleared = await goal_orchestrator.clear()


    assert cleared["status"] == "cleared"

    print("PASS | Orchestrator Reset")



    print("PASS | Autonomous Goal Orchestrator Runtime")



if __name__ == "__main__":

    asyncio.run(main())
