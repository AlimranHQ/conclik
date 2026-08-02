"""
Conclik Workflow Result V4.1
"""


class WorkflowResult:

    def __init__(self):

        self.status = "pending"
        self.completed = []
        self.failed = []
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def add_failure(self, task_id):
        self.failed.append(task_id)

    @property
    def success(self):
        return len(self.failed) == 0


workflow_result = WorkflowResult()
