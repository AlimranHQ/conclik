from app.core.brain.assignment.assignment_engine import assignment_engine
from app.core.parallel_executor.parallel_executor import parallel_executor


class WorkflowEngine:

    async def execute(self, goal):

        assignment = await assignment_engine.assign(goal)

        execution = await parallel_executor.execute(
            assignment["assignments"]
        )

        return {
            "status": "workflow_completed",
            "assignment": assignment,
            "execution": execution,
            "results": execution["results"],
        }


workflow_engine = WorkflowEngine()
