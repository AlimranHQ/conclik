from app.core.brain.assignment.assignment_engine import assignment_engine
from app.core.workflow_engine.rules.workflow_rules import workflow_rules
from app.core.workflow_engine.scheduler.workflow_scheduler import workflow_scheduler


class WorkflowEngine:

    async def execute(self, goal):

        assignment = await assignment_engine.assign(goal)

        workflow = workflow_rules.apply(
            assignment["assignments"]
        )

        execution = await workflow_scheduler.execute(
            workflow
        )

        return {
            "status": "workflow_completed",
            "assignment": assignment,
            "workflow": workflow,
            "execution": execution,
            "results": execution["results"],
        }


workflow_engine = WorkflowEngine()
