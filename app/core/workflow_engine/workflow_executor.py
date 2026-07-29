"""
Workflow Executor
"""

from app.core.execution.task_manager import task_manager


class WorkflowExecutor:

    def execute(self, workflow):

        for task in workflow.tasks:
            task_manager.submit(task)


workflow_executor = WorkflowExecutor()

