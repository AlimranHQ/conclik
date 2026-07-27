"""
Conclik Pilot AI - Thumbnail Agent
Version: 5.0.0
Description: Generates high-CTR thumbnail concepts, visual ideas, and image prompts.
"""

from app.providers.gemini_client import gemini_client

class ThumbnailAgent:
    async def design_concept(self, topic: str, research_data: str, script_data: str) -> str:
        prompt = f"""
        You are an expert YouTube Thumbnail Designer and Visual Strategist. Your task is to design high-CTR thumbnail concepts based on the provided topic, research, and script.
        
        Topic: {topic}
        
        Research Summary:
        {research_data}

        Script Content:
        {script_data}

        Please provide:
        1. Thumbnail Visual Concepts (Provide 2-3 distinct design ideas with descriptions of imagery, background, and focal points).
        2. Catchy On-Image Text / Overlay (Short, punchy 2-4 words text to grab attention).
        3. Color Palette Suggestions (High contrast colors to stand out).
        4. AI Image Generation Prompt (A detailed descriptive prompt if someone wants to generate it via DALL-E or Midjourney).

        Keep the output creative, structured, and practical.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"Thumbnail Agent Error: {str(e)}")

thumbnail_agent = ThumbnailAgent()
