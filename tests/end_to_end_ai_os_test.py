import asyncio

from app.core.master_orchestrator.master_runtime import master_runtime
from app.core.master_orchestrator.master_pipeline import master_pipeline
from app.core.brain.runtime.brain_runtime import brain_runtime


GOAL = "Build AI YouTube Automation"


async def main():

    print("=== End-to-End AI OS Pipeline Test ===")

    print("\n[1] Master Runtime")

    master = await master_runtime.run(GOAL)

    assert master["status"] == "accepted"

    print("PASS | Master Runtime")

    print("\n[2] Brain Runtime")

    brain = await brain_runtime.run(GOAL)

    assert brain["status"] == "brain_ready"

    print("PASS | Brain Runtime")

    print("\n[3] Master Pipeline")

    pipeline = await master_pipeline.execute(GOAL)

    execution = pipeline["execution"]

    assert execution["status"] == "team_completed"

    print("PASS | Master Pipeline")

    print("\n========== FINAL RESULT ==========")

    print({
        "master": master["status"],
        "brain": brain["status"],
        "pipeline": pipeline["status"],
        "team": execution["status"],
        "agents": execution["completed_agents"],
        "total_agents": execution["total_agents"],
    })

    print("\nPASS | End-to-End AI OS Pipeline")


if __name__ == "__main__":
    asyncio.run(main())
