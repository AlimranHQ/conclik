"""
Master Executor V1
"""

from app.core.master_orchestrator.master_pipeline import master_pipeline


class MasterExecutor:

    async def execute(self, goal):

        result = await master_pipeline.execute(goal)

        return {
            "status": "master_execution_completed",
            "result": result,
        }


master_executor = MasterExecutor()
