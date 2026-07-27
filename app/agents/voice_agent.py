"""
Conclik Pilot AI - Voice Agent
Version: 5.0.0
Description: Generates voiceover guidelines, voice tones, pacing, and audio-friendly script cues.
"""

from app.providers.gemini_client import gemini_client

class VoiceAgent:
    async def create_voice_guideline(self, topic: str, script_data: str) -> str:
        prompt = f"""
        You are an expert Voiceover Director and Audio Content Producer. Your task is to design professional voiceover guidelines and pacing instructions based on the provided script.
        
        Topic: {topic}

        Script Content:
        {script_data}

        Please provide:
        1. Recommended Voice Tone & Mood (e.g., energetic, professional, emotional, authoritative).
        2. Speaking Pacing & Tempo (Where to speed up, slow down, or pause for dramatic effect).
        3. Pronunciation and Emphasis Cues (Keywords or terms that need special vocal stress).
        4. Audio/Sound Effects (SFX) & Background Music suggestions to enhance the listening experience.

        Keep the output structured, clear, and professional.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"Voice Agent Error: {str(e)}")

voice_agent = VoiceAgent()
