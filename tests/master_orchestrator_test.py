import asyncio

from app.core.master_orchestrator.master_executor import master_executor


print("=== Master Orchestrator Test ===")


result = asyncio.run(
    master_executor.execute(
        "Build AI YouTube Automation"
    )
)


print(result)


assert result["status"] == "master_execution_completed"

execution = result["result"]["execution"]

assert execution["status"] == "team_completed"

assert execution["total_agents"] == 7

assert len(execution["completed_agents"]) == 7


print("PASS | Master Orchestrator")
