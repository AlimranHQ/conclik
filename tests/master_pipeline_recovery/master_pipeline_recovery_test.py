import asyncio

from app.core.master_orchestrator.master_pipeline import (
    master_pipeline,
)

from app.core.master_orchestrator.reliability.master_reliability import (
    master_reliability,
)



GOAL = "Build AI YouTube Automation"



async def main():

    print("=== Master Pipeline Recovery Test ===")


    await master_reliability.clear()



    # Stage 1: Start Master Task

    started = await master_reliability.start_task(
        "PIPELINE-001"
    )


    assert started["status"] == "started"

    print("PASS | Pipeline Task Started")



    # Stage 2: Execute Pipeline

    result = await master_pipeline.execute(
        GOAL
    )


    assert result["status"] == "pipeline_completed"

    print("PASS | Pipeline Execution")



    # Stage 3: Simulate Failure

    failure = await master_reliability.handle_failure(
        "PIPELINE-001",
        "network timeout"
    )


    assert failure["status"] == "retrying"

    print("PASS | Pipeline Failure Recovery")



    # Stage 4: Check Recovery Point

    recovery = await master_reliability.recover_task(
        "PIPELINE-001"
    )


    assert recovery["status"] == "recoverable"

    print("PASS | Pipeline Recovery Point")



    print(
        {
            "pipeline": result["status"],
            "recovery": recovery["status"],
            "retry": failure["status"],
        }
    )


    print("PASS | Master Pipeline Recovery Runtime")



if __name__ == "__main__":

    asyncio.run(main())
