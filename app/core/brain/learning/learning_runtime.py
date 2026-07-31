from app.core.kernel.base_engine import BaseEngine
from app.core.brain.learning.learning_engine import learning_engine


class LearningRuntime(BaseEngine):

    async def process(self, reflection):

        learning = await learning_engine.run(reflection)

        return {
            "status": "learning_completed",
            "learning": learning,
            "memory_updated": learning["memory_update"],
        }

    async def run(self, reflection):
        return await self.process(reflection)


learning_runtime = LearningRuntime()
