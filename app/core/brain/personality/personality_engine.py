from app.core.kernel.base_engine import BaseEngine
from app.core.brain.personality.personality_profile import personality_profile


class PersonalityEngine(BaseEngine):

    async def initialize(self):

        profile = personality_profile.load()

        return {
            "status": "personality_ready",
            "profile": profile,
        }

    async def run(self):
        return await self.initialize()


personality_engine = PersonalityEngine()
