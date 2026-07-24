"""
Conclik Pilot AI
Version : 4.2.0
Module  : Workflow Service
"""

from app.core.job_scheduler import scheduler
from app.core.workflow_executor import executor


class WorkflowService:

    def create(self, job):
        scheduler.schedule(job)

    def run(self):
        return executor.execute()


workflow_service = WorkflowService()
