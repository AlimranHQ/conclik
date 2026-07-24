import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class ThumbnailAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = "You are an expert Thumbnail & Visual Agent. You create high-CTR thumbnail concepts and image prompts."

    async def generate_thumbnail_ideas(self, title: str, script_summary: str) -> Dict[str, Any]:
        try:
            prompt = f"Title: {title}\nSummary: {script_summary}\n\nProvide 3 high-CTR YouTube thumbnail concepts, visual elements, text overlays, and AI image generation prompts."
            response = await self.client.generate_content(prompt, system_instruction=self.system_prompt)
            return {"status": "success", "thumbnail_data": response}
        except Exception as e:
            logger.error(f"Error in ThumbnailAgent: {str(e)}")
            return {"status": "error", "message": str(e)}
