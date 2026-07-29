"""
Conclik Pilot AI
Video Agent
Version : 6.0.0
Architecture : Base Agent
Description : Generates storyboards and editing blueprints.
"""

from app.core.agents.base_agent import BaseAgent


class VideoAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def create_storyboard(
        self,
        topic: str,
        script_data: str,
        voice_data: str,
    ) -> str:

        prompt = f"""
You are an expert Video Director and Professional Editor.

Topic:
{topic}

Script Content:
{script_data}

Voice Guidelines:
{voice_data}

Please provide:

1. Scene-by-Scene Breakdown

2. B-Roll Suggestions

3. Editing & Transition Styles

4. Visual FX / Graphics Recommendations

Keep the output highly structured,
practical,
and production ready.
"""

        try:

            return await self.ask_ai(
                prompt=prompt,
                category="video",
            )

        except Exception as e:

            raise Exception(
                f"Video Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
        script_data: str,
        voice_data: str,
    ):

        return await self.create_storyboard(
            topic,
            script_data,
            voice_data,
        )


video_agent = VideoAgent()

