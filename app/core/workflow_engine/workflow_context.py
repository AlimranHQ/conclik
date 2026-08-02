"""
Conclik Workflow Context V4
"""


class WorkflowContext:

    def __init__(self):

        self.workflow_id = None

        self.state = {}

        self.results = []

    def update(self, key, value):

        self.state[key] = value

    def get(self, key, default=None):

        return self.state.get(key, default)


workflow_context = WorkflowContext()
