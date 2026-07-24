"""
Conclik Pilot AI
Version : 4.2.0
Module  : Workflow Executor
"""

from app.core.workflow_queue import workflow_queue


class WorkflowExecutor:

    def execute(self):

        job = workflow_queue.next()

        if not job:
            return {
                "success": False,
                "message": "Queue Empty"
            }

        return {
            "success": True,
            "job": job,
            "status": "Executed"
        }


executor = WorkflowExecutor()
