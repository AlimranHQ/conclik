"""
Conclik Pilot AI
Script Agent
Version : 6.0.0
Architecture : Base Agent
"""

from app.core.agents.base_agent import BaseAgent


class ScriptAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def generate_script(
        self,
        topic: str,
        research_data: str,
    ) -> str:

        prompt = f"""
You are an expert Video Script Writer.

Your task is to write an engaging, high-retention script based on the provided research.

Topic:
{topic}

Research Insights:

{research_data}

Please structure the script with:

1. Hook (0–5 seconds)

2. Introduction

3. Body Content

4. Call To Action (CTA)

5. Outro

Keep the tone natural,
professional,
and conversational.
"""

        try:

            return await self.ask_ai(
                prompt=prompt,
                category="script",
            )

        except Exception as e:

            raise Exception(
                f"Script Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
        research_data: str,
    ):

        return await self.generate_script(
            topic,
            research_data,
        )


script_agent = ScriptAgent()

