from app.core.brain.assignment.assignment_engine import assignment_engine
from app.core.workflow_engine.rules.workflow_rules import workflow_rules
from app.core.workflow_engine.workflow_runtime import workflow_runtime


class WorkflowEngine:

    async def execute(self, goal):

        assignment = await assignment_engine.assign(goal)

        workflow = workflow_rules.apply(
            assignment["assignments"]
        )

        execution = await workflow_runtime.run(
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
