from app.core.kernel.base_engine import BaseEngine
from app.core.brain.emotion.emotion_profile import emotion_profile


class EmotionEngine(BaseEngine):

    async def evaluate(self, goal: str):

        mode = emotion_profile.detect(goal)

        return {
            "status": "emotion_ready",
            "mode": mode,
        }

    async def run(self, goal):
        return await self.evaluate(goal)


emotion_engine = EmotionEngine()
