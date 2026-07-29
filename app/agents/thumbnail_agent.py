"""
Conclik Pilot AI
Thumbnail Agent
Version : 6.0.0
Architecture : Base Agent
Description : Generates high-CTR thumbnail concepts.
"""

from app.core.agents.base_agent import BaseAgent


class ThumbnailAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def design_concept(
        self,
        topic: str,
        research_data: str,
        script_data: str,
    ) -> str:

        prompt = f"""
You are an expert YouTube Thumbnail Designer and Visual Strategist.

Topic:
{topic}

Research Summary:
{research_data}

Script Content:
{script_data}

Please provide:

1. 2–3 Thumbnail Concepts

2. Short On-Image Text

3. Color Palette

4. AI Image Prompt

Keep the output creative,
structured,
and production ready.
"""

        try:
            return await self.ask_ai(
                prompt=prompt,
                category="thumbnail",
            )

        except Exception as e:
            raise Exception(f"Thumbnail Agent Error: {e}")

    async def run(
        self,
        topic: str,
        research_data: str,
        script_data: str,
    ):
        return await self.design_concept(
            topic,
            research_data,
            script_data,
        )


thumbnail_agent = ThumbnailAgent()

