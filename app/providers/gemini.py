class GeminiProvider:
    def generate(self, prompt: str):
        return {
            "provider": "Gemini",
            "status": "Not Connected Yet",
            "result": f"Prompt received: {prompt}"
        }

gemini = GeminiProvider()
