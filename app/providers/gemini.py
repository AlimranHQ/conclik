import google.generativeai as genai

from app.config import settings


class GeminiProvider:

    def __init__(self):
        self.model = None

        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate(self, prompt: str):

        if not self.model:
            return {
                "success": False,
                "provider": "Gemini",
                "error": "Gemini API Key Missing"
            }

        try:

            response = self.model.generate_content(prompt)

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
