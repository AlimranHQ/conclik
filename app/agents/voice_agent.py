"""
Conclik Pilot AI
Voice Agent
Version : 6.0.0
Architecture : Base Agent
Description : Generates professional voice guidelines.
"""

from app.core.agents.base_agent import BaseAgent


class VoiceAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def create_voice_guideline(
        self,
        topic: str,
        script_data: str,
    ) -> str:

        prompt = f"""
You are an expert Voiceover Director and Audio Content Producer.

Topic:
{topic}

Script Content:
{script_data}

Please provide:

1. Recommended Voice Tone & Mood

2. Speaking Pacing & Tempo

3. Pronunciation & Emphasis Cues

4. Background Music & SFX Suggestions

Keep the output structured,
professional,
and production ready.
"""

        try:

            return await self.ask_ai(
                prompt=prompt,
                category="voice",
            )

        except Exception as e:

            raise Exception(
                f"Voice Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
        script_data: str,
    ):

        return await self.create_voice_guideline(
            topic,
            script_data,
        )


voice_agent = VoiceAgent()

