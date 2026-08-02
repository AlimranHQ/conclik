import asyncio

from app.core.autonomous.self_healing.self_healing_engine import (
    self_healing_engine,
)



async def main():

    print("=== Self Healing Engine Test ===")


    await self_healing_engine.clear()



    # Test 1: Transient Failure

    result = await self_healing_engine.heal(
        "TASK-SELF-001",
        "network timeout"
    )


    assert result["status"] == "retrying"

    assert result["analysis"]["type"] == "transient"

    print("PASS | Transient Failure Healing")



    # Test 2: Permanent Failure

    result = await self_healing_engine.heal(
        "TASK-SELF-002",
        "permission denied"
    )


    assert result["status"] == "recovery_required"

    assert result["analysis"]["type"] == "permanent"

    print("PASS | Permanent Failure Handling")



    # Test 3: Health Status

    status = await self_healing_engine.status()


    assert status["events"] == 2

    assert status["health"] == "degraded"

    print("PASS | Health Tracking")



    # Test 4: Clear Protection

    cleared = await self_healing_engine.clear()


    assert cleared["status"] == "cleared"


    print("PASS | Engine Reset")



    print("PASS | Self Healing Engine Runtime")



if __name__ == "__main__":

    asyncio.run(main())
