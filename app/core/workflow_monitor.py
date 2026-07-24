"""
Conclik Pilot AI
Version : 4.2.0
Module  : Workflow Monitor
"""

from app.core.workflow_queue import workflow_queue


class WorkflowMonitor:

    def status(self):

        return {
            "pending_jobs": workflow_queue.size(),
            "queue_empty": workflow_queue.empty()
        }


monitor = WorkflowMonitor()
