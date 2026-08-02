"""
Master State V1
"""


class MasterState:

    def __init__(self):

        self.status = "idle"
        self.current_task = None
        self.completed_tasks = []
        self.failed_tasks = []


    def start(self, task=None):

        self.status = "running"
        self.current_task = task


    def complete(self, task):

        self.status = "completed"
        self.completed_tasks.append(task)
        self.current_task = None


    def fail(self, task):

        self.status = "failed"
        self.failed_tasks.append(task)
        self.current_task = None


    def snapshot(self):

        return {
            "status": self.status,
            "current_task": self.current_task,
            "completed_tasks": self.completed_tasks,
            "failed_tasks": self.failed_tasks,
        }


master_state = MasterState()
