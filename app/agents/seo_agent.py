import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class SEOAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = (
            "You are an expert SEO Agent in the Conclik AI multi-agent system. "
            "Your job is to optimize content for search engines, generate high-ranking keywords, "
            "compelling meta titles, and meta descriptions."
        )

    async def optimize_content(self, title: str, content: str) -> Dict[str, Any]:
        """
        Optimizes content for SEO and generates metadata.
        """
        try:
            prompt = (
                f"Content Title: {title}\n"
                f"Content Body: {content[:1000]}...\n\n"
                "Please provide:\n"
                "1. SEO Optimized Meta Title\n"
                "2. Catchy Meta Description\n"
                "3. Primary and Secondary Keywords\n"
                "4. SEO Recommendations"
            )

            response = await self.client.generate_content(
                prompt=prompt,
                system_instruction=self.system_prompt
            )

            return {
                "status": "success",
                "title": title,
                "seo_data": response
            }
        except Exception as e:
            logger.error(f"Error in SEOAgent: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }
