import google.generativeai as genai
import httpx

from app.config import settings


class AIEng ine:

    def __init__(self):

        self.gemini = None

        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.gemini = genai.GenerativeModel("gemini-2.0-flash")

    def _gemini(self, prompt):

        if not self.gemini:
            return None

        try:

<<<<<<< HEAD
            response = self.gemini.generate_content(prompt)
=======
            response = self.gemini.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
>>>>>>> b7d3ff9 (Fix Gemini SDK and add httpx)

            return {
                "success": True,
                "provider": "Gemini",
                "content": response.text
            }

        except Exception:
            return None

    def _openrouter(self, prompt):

        if not settings.OPENROUTER_API_KEY:
            return None

        try:

            headers = {
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }

            body = {
                "model": "openai/gpt-4.1-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = httpx.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=body,
                timeout=60
            )

            data = response.json()

            return {
                "success": True,
                "provider": "OpenRouter",
                "content": data["choices"][0]["message"]["content"]
            }

        except Exception:
            return None

    def _groq(self, prompt):

        if not settings.GROQ_API_KEY:
            return None

        try:

            headers = {
                "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            body = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = httpx.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=body,
                timeout=60
            )

            data = response.json()

            return {
                "success": True,
                "provider": "Groq",
                "content": data["choices"][0]["message"]["content"]
            }

        except Exception:
            return None

    def generate_content(self, prompt, category="general"):

        result = self._openrouter(prompt)

        if result:
            result["category"] = category
            return result

        result = self._groq(prompt)

        if result:
            result["category"] = category
            return result

        result = self._gemini(prompt)

        if result:
            result["category"] = category
            return result

        return {
            "success": False,
            "error": "No AI Provider Available"
        }


ai_engine = AIEngine()
