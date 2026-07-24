"""
Conclik Pilot AI
Version : 4.2.0
Module  : Job Scheduler
"""

from app.core.workflow_queue import workflow_queue


class JobScheduler:

    def schedule(self, job):
        workflow_queue.add(job)

    def pending(self):
        return workflow_queue.size()


scheduler = JobScheduler()
