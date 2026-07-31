from app.core.kernel.base_engine import BaseEngine
from app.core.reflection_engine.reflection_analyzer import reflection_analyzer


class ReflectionRuntime(BaseEngine):

    async def run(self, result):

        return await reflection_analyzer.analyze(result)


reflection_runtime = ReflectionRuntime()
