import asyncio

from app.core.autonomous.supervisor.supervisor import (
    supervisor,
)



async def main():

    print("=== Supervisor Test ===")


    await supervisor.clear()



    # Test 1: Register Component

    registered = await supervisor.register_component(
        "master_runtime"
    )


    assert registered["status"] == "registered"

    print("PASS | Component Supervision")



    # Test 2: Health Inspection

    inspection = await supervisor.inspect()


    assert inspection["health"] == "healthy"

    print("PASS | Health Inspection")



    # Test 3: Healing Trigger

    healing = await supervisor.supervise_failure(
        "SUPERVISOR-TASK-001",
        "network timeout"
    )


    assert healing["status"] == "retrying"

    print("PASS | Failure Healing Trigger")



    # Test 4: Decision Engine

    decision = await supervisor.decision()


    assert decision["decision"] in [
        "continue",
        "heal",
        "recovery_required",
    ]

    print("PASS | Decision Engine")



    # Test 5: History

    history = await supervisor.history()


    assert len(history) > 0

    print("PASS | Supervisor History")



    # Test 6: Reset

    cleared = await supervisor.clear()


    assert cleared["status"] == "cleared"

    print("PASS | Supervisor Reset")



    print("PASS | Autonomous Supervisor Runtime")



if __name__ == "__main__":

    asyncio.run(main())
