class WorkflowExecutor:

    async def execute(self, workflow):

        outputs = []

        for step in workflow:
            outputs.append(step)

        return outputs


workflow_executor = WorkflowExecutor()
