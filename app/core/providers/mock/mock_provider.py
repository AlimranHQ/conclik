"""
Base Mock Provider
"""

class MockProvider:

    async def generate(self, prompt: str, **kwargs):
        return {
            "success": True,
            "provider": "mock",
            "output": "Mock response generated successfully."
        }

    async def health(self):
        return True
