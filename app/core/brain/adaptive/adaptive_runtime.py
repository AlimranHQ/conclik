from app.core.kernel.base_engine import BaseEngine
from app.core.brain.adaptive.adaptive_engine import adaptive_engine


class AdaptiveRuntime(BaseEngine):

    async def process(self, learning):

        adaptive = await adaptive_engine.run(learning)

        return {
            "status": "adaptive_completed",
            "adaptive": adaptive,
        }

    async def run(self, learning):
        return await self.process(learning)


adaptive_runtime = AdaptiveRuntime()
