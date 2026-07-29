from app.core.pipeline_runtime.pipeline_runtime import pipeline_runtime
from app.core.project_runtime.project_result import ProjectResult

class ProjectExecutor:

    async def execute(self, topic: str):

        output = await pipeline_runtime.run(topic)

        return ProjectResult(
            success=True,
            data=output,
            message="Project completed successfully"
        )

project_executor = ProjectExecutor()
