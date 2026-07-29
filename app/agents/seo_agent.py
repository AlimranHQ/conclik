"""
Conclik Pilot AI
SEO Agent
Version : 6.0.0
Architecture : Base Agent
Description : Generates optimized SEO metadata.
"""

from app.core.agents.base_agent import BaseAgent


class SEOAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def optimize(
        self,
        topic: str,
        research_data: str,
        script_data: str,
    ) -> str:

        prompt = f"""
You are an expert YouTube and Content SEO Specialist.

Generate high-performing SEO metadata.

Topic:

{topic}

Research Summary:

{research_data}

Script Content:

{script_data}

Please provide:

1. Three High-CTR Titles

2. SEO Description

3. Relevant Tags

4. Trending Hashtags

Keep everything structured,
clean,
and production ready.
"""

        try:

            return await self.ask_ai(
                prompt=prompt,
                category="seo",
            )

        except Exception as e:

            raise Exception(
                f"SEO Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
        research_data: str,
        script_data: str,
    ):

        return await self.optimize(
            topic,
            research_data,
            script_data,
        )


seo_agent = SEOAgent()

