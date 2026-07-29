from app.core.pipeline_runtime.pipeline_executor import pipeline_executor

class PipelineRuntime:

    async def run(self, topic: str):
        return await pipeline_executor.execute(topic)


pipeline_runtime = PipelineRuntime()
