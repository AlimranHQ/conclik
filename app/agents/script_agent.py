import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class ScriptAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = (
            "You are an expert Script Agent in the Conclik AI multi-agent system. "
            "Your job is to write engaging, high-retention scripts, blog posts, or copy "
            "based on the provided research data and topic."
        )

    async def generate_script(self, topic: str, research_data: str = "", tone: str = "Engaging") -> Dict[str, Any]:
        """
        Generates a professional script or content based on research data.
        """
        try:
            prompt = (
                f"Topic: {topic}\n"
                f"Tone: {tone}\n"
                f"Research Insights: {research_data}\n\n"
                "Please write a comprehensive, well-structured script or content piece with a strong hook, "
                "informative body sections, and a clear call-to-action (CTA)."
            )

            response = await self.client.generate_content(
                prompt=prompt,
                system_instruction=self.system_prompt
            )

            return {
                "status": "success",
                "topic": topic,
                "script": response
            }
        except Exception as e:
            logger.error(f"Error in ScriptAgent: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }
