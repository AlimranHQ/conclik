from app.core.project_runtime.project_executor import project_executor

class ProjectRuntime:

    async def run(self, topic: str):
        return await project_executor.execute(topic)

project_runtime = ProjectRuntime()
