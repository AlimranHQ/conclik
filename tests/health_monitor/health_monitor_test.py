import asyncio

from app.core.autonomous.health_monitor.health_monitor import (
    health_monitor,
    HealthStatus,
)



async def main():

    print("=== Health Monitor Test ===")


    await health_monitor.clear()



    # Test 1: Register Component

    registered = await health_monitor.register(
        "master_runtime"
    )


    assert registered["status"] == "registered"

    print("PASS | Component Register")



    # Test 2: Heartbeat

    heartbeat = await health_monitor.heartbeat(
        "master_runtime"
    )


    assert heartbeat["status"] == "alive"

    print("PASS | Heartbeat Tracking")



    # Test 3: Failure Tracking

    failure = await health_monitor.report_failure(
        "master_runtime"
    )


    assert failure["status"] == HealthStatus.DEGRADED

    assert failure["failures"] == 1

    print("PASS | Failure Tracking")



    # Test 4: Critical Failure

    await health_monitor.report_failure(
        "master_runtime"
    )

    failed = await health_monitor.report_failure(
        "master_runtime"
    )


    assert failed["status"] == HealthStatus.FAILED

    print("PASS | Critical Failure Detection")



    # Test 5: System Health

    system = await health_monitor.system_health()


    assert system == HealthStatus.FAILED

    print("PASS | System Health Status")



    # Test 6: Reset

    cleared = await health_monitor.clear()


    assert cleared["status"] == "cleared"

    print("PASS | Monitor Reset")



    print("PASS | Health Monitor Runtime")



if __name__ == "__main__":

    asyncio.run(main())
