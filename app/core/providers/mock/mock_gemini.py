"""
Mock Gemini Provider
"""

class MockGemini:

    @property
    def name(self):
        return "gemini"

    async def generate_content(
        self,
        prompt: str,
        category: str = "general",
        **kwargs,
    ):
        return f"""
[MOCK GEMINI]

Category: {category}

Prompt:
{prompt}

Mock response generated successfully.
"""

    async def health(self):
        return True


mock_gemini = MockGemini()
