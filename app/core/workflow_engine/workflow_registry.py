"""
Workflow Registry
"""

class WorkflowRegistry:

    def __init__(self):
        self._workflows = {}

    def register(self, workflow):
        self._workflows[workflow.name] = workflow

    def get(self, name):
        return self._workflows.get(name)

    def all(self):
        return self._workflows


workflow_registry = WorkflowRegistry()

