"""
Conclik Pilot AI - Video Agent
Version: 5.0.0
Description: Generates scene-by-scene storyboards, B-Roll ideas, and video editing guidelines.
"""

from app.providers.gemini_client import gemini_client

class VideoAgent:
    async def create_storyboard(self, topic: str, script_data: str, voice_data: str) -> str:
        prompt = f"""
        You are an expert Video Director and Professional Editor. Your task is to create a comprehensive scene-by-scene video storyboard and editing blueprint based on the provided script and voice guidelines.
        
        Topic: {topic}

        Script Content:
        {script_data}

        Voice Guidelines:
        {voice_data}

        Please provide:
        1. Scene-by-Scene Breakdown (Scene number, visual description, on-screen text/captions).
        2. B-Roll & Footage Suggestions (What visual clips or animations should appear).
        3. Editing & Transition Styles (Cuts, zoom-ins, transitions, and pacing effects).
        4. Visual FX / Graphics recommendations to boost viewer retention.

        Keep the output highly structured, practical, and production-ready.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"Video Agent Error: {str(e)}")

video_agent = VideoAgent()
