"""
Conclik Workflow Rules V4
"""

from app.core.workflow_engine.workflow import (
    Workflow,
    WorkflowTask,
)


class WorkflowRules:


    def apply(self, assignments):

        workflow = Workflow(
            name="Conclik Workflow",
            mode="sequential",
            metadata={
                "version": "V4"
            }
        )


        for index, item in enumerate(assignments, start=1):

            task_mode = (
                "sequential"
                if item.get("depends_on")
                else "parallel"
            )


            task = WorkflowTask(

                id=index,

                name=item.get(
                    "task",
                    "unknown"
                ),

                agent=item.get(
                    "agent"
                ),

                mode=task_mode,

                depends_on=item.get(
                    "depends_on",
                    []
                )

            )


            workflow.add_task(task)


        return workflow



workflow_rules = WorkflowRules()
