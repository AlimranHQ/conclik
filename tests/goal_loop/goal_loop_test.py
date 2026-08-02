import asyncio

from app.core.autonomous.goal_loop.goal_loop import (
    goal_loop,
    GoalStatus,
)



async def main():

    print("=== Goal Loop Test ===")


    await goal_loop.clear()



    # Test 1: Goal Create

    created = await goal_loop.create_goal(
        "GOAL-001",
        "Build AI YouTube Automation"
    )


    assert created["status"] == GoalStatus.CREATED

    assert created["progress"] == 0

    print("PASS | Goal Create")



    # Test 2: Goal Start

    started = await goal_loop.start(
        "GOAL-001"
    )


    assert started["status"] == GoalStatus.RUNNING

    print("PASS | Goal Start")



    # Test 3: Progress Tracking

    progress = await goal_loop.progress(
        "GOAL-001",
        50
    )


    assert progress["progress"] == 50

    assert progress["status"] == GoalStatus.RUNNING

    print("PASS | Progress Tracking")



    # Test 4: Completion

    completed = await goal_loop.complete(
        "GOAL-001"
    )


    assert completed["status"] == GoalStatus.COMPLETED

    assert completed["progress"] == 100

    print("PASS | Goal Completion")



    # Test 5: Status Retrieve

    status = await goal_loop.status(
        "GOAL-001"
    )


    assert status["status"] == GoalStatus.COMPLETED

    print("PASS | Goal Status Retrieve")



    # Test 6: History

    history = await goal_loop.all_history()


    assert len(history) >= 2

    print("PASS | Goal History")



    # Test 7: Reset

    cleared = await goal_loop.clear()


    assert cleared["status"] == "cleared"

    print("PASS | Goal Reset")



    print("PASS | Autonomous Goal Loop Runtime")



if __name__ == "__main__":

    asyncio.run(main())
