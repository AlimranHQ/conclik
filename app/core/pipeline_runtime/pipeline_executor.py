class PipelineExecutor:

    async def execute(self, topic: str):
        results = []

        from app.core.pipeline_runtime.pipeline_registry import pipeline_registry

        for step in pipeline_registry.all():
            output = await step.run(topic)
            results.append(output)

        return results


pipeline_executor = PipelineExecutor()
