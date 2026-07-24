class WorkflowEngine:

    def __init__(self):
        self.steps = []

    def add_step(self, name: str):
        self.steps.append(name)

    def clear(self):
        self.steps.clear()

    def run(self):
        return {
            "success": True,
            "workflow": self.steps,
            "total_steps": len(self.steps)
        }


workflow_engine = WorkflowEngine()
