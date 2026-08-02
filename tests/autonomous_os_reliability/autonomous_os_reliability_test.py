import asyncio


from app.core.master_orchestrator.master_runtime import (
    master_runtime,
)

from app.core.brain.runtime.brain_runtime import (
    brain_runtime,
)

from app.core.master_orchestrator.master_pipeline import (
    master_pipeline,
)

from app.core.master_orchestrator.reliability.master_reliability import (
    master_reliability,
)



GOAL = "Build AI YouTube Automation"



async def main():

    print("=== Autonomous OS Reliability Test ===")


    await master_reliability.clear()



    # Stage 1: Master Runtime

    master = await master_runtime.run(
        GOAL
    )


    assert master["status"] == "accepted"

    print("PASS | Master Runtime")



    # Stage 2: Brain Runtime

    brain = await brain_runtime.run(
        GOAL
    )


    assert brain["status"] == "brain_ready"

    print("PASS | Brain Runtime")



    # Stage 3: Pipeline Execution

    pipeline = await master_pipeline.execute(
        GOAL
    )


    assert pipeline["status"] == "pipeline_completed"

    assert pipeline["execution"]["status"] == "team_completed"

    print("PASS | Autonomous Pipeline")



    # Stage 4: Reliability Checkpoint

    checkpoint = await master_reliability.start_task(
        "AUTONOMOUS-001"
    )


    assert checkpoint["status"] == "started"

    print("PASS | Reliability Checkpoint")



    # Stage 5: Failure Simulation

    failure = await master_reliability.handle_failure(
        "AUTONOMOUS-001",
        "network timeout"
    )


    assert failure["status"] == "retrying"

    print("PASS | Failure Recovery")



    # Stage 6: Recovery

    recovery = await master_reliability.recover_task(
        "AUTONOMOUS-001"
    )


    assert recovery["status"] == "recoverable"

    print("PASS | Recovery Resume")



    print(
        {
            "master": master["status"],
            "brain": brain["status"],
            "pipeline": pipeline["status"],
            "team": pipeline["execution"]["status"],
            "recovery": recovery["status"],
        }
    )


    print("PASS | Autonomous OS Reliability Runtime")



if __name__ == "__main__":

    asyncio.run(main())
