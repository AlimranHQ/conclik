"""
Conclik Pilot AI
QA Agent
Version : 6.0.0
Architecture : Base Agent
Description : Reviews the complete multi-agent pipeline.
"""

from app.core.agents.base_agent import BaseAgent


class QAAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def review_quality(
        self,
        topic: str,
        all_outputs: dict,
    ) -> str:

        prompt = f"""
You are an expert Content Quality Assurance Director
and Senior Editor.

Topic:
{topic}

Pipeline Outputs:

Research:
{all_outputs.get('research', {}).get('output', 'N/A')}

Script:
{all_outputs.get('script', {}).get('output', 'N/A')}

SEO:
{all_outputs.get('seo', {}).get('output', 'N/A')}

Thumbnail:
{all_outputs.get('thumbnail', {}).get('output', 'N/A')}

Voice:
{all_outputs.get('voice', {}).get('output', 'N/A')}

Video:
{all_outputs.get('video', {}).get('output', 'N/A')}

Please provide:

1. Overall Quality Score (/10)

2. Consistency Check

3. Improvement Suggestions

4. Final Production Approval

Keep the review objective,
professional,
and production ready.
"""

        try:

            return await self.ask_ai(
                prompt=prompt,
                category="qa",
            )

        except Exception as e:

            raise Exception(
                f"QA Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
        all_outputs: dict,
    ):

        return await self.review_quality(
            topic,
            all_outputs,
        )


qa_agent = QAAgent()

