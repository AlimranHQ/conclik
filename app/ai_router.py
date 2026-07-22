from app.providers.gemini import gemini

class AIRouter:
    def generate(self, prompt: str, provider: str = "gemini"):
        if provider == "gemini":
            return gemini.generate(prompt)

        return {
            "error": "Provider not found"
        }

ai_router = AIRouter()
