import asyncio

from app.core.autonomous.control_loop.control_loop import (
    control_loop,
)

from app.core.autonomous.supervisor.supervisor import (
    supervisor,
)



async def main():

    print("=== Control Loop Test ===")


    await control_loop.clear()

    await supervisor.clear()



    # Register system component

    await supervisor.register_component(
        "master_runtime"
    )



    # Test 1: Observe

    observation = await control_loop.observe()


    assert observation["health"] == "healthy"

    print("PASS | Observation")



    # Test 2: Decision

    decision = await control_loop.decide()


    assert decision["decision"] == "continue"

    print("PASS | Decision Flow")



    # Test 3: Action

    action = await control_loop.act(
        decision
    )


    assert action["action"] == "continue"

    print("PASS | Action Execution")



    # Test 4: Cycle Run

    result = await control_loop.start(
        count=3
    )


    assert result["status"] == "completed"

    assert result["cycles"] == 3

    print("PASS | Autonomous Cycles")



    # Test 5: History

    history = await control_loop.history()


    assert len(history) == 3

    print("PASS | Cycle History")



    # Test 6: Stop

    stopped = await control_loop.stop()


    assert stopped["status"] == "stopped"

    print("PASS | Loop Stop")



    print("PASS | Autonomous Control Loop Runtime")



if __name__ == "__main__":

    asyncio.run(main())
