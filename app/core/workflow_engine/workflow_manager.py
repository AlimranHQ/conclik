"""
Workflow Manager
"""

from app.core.workflow_engine.workflow_registry import workflow_registry


class WorkflowManager:

    def register(self, workflow):
        workflow_registry.register(workflow)

    def load(self, name):
        return workflow_registry.get(name)


workflow_manager = WorkflowManager()

