from google import genai
from app.config import settings


class GeminiProvider:

    def __init__(self):
        self.client = None

        if settings.GEMINI_API_KEY:
            self.client = genai.Client(
                api_key=settings.GEMINI_API_KEY
            )

    def generate(self, prompt: str):

        if not self.client:
            return {
                "success": False,
                "provider": "Gemini",
                "error": "Gemini API Key Missing"
            }

        try:

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )

            return {
                "success": True,
                "provider": "Gemini",
                "content": response.text
            }

        except Exception as e:

            return {
                "success": False,
                "provider": "Gemini",
                "error": str(e)
            }


gemini = GeminiProvider()
