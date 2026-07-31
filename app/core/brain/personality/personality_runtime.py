from app.core.kernel.base_engine import BaseEngine
from app.core.brain.personality.personality_engine import personality_engine
from app.core.brain.emotion.emotion_engine import emotion_engine


class PersonalityRuntime(BaseEngine):

    async def load(self, goal):

        personality = await personality_engine.run()

        emotion = await emotion_engine.run(goal)

        return {
            "status": "personality_ready",
            "personality": personality["profile"],
            "emotion": emotion["mode"],
        }

    async def run(self, goal):
        return await self.load(goal)


personality_runtime = PersonalityRuntime()
