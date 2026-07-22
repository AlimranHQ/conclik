import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "ContentPilot AI"
    APP_VERSION = "2.1.0"

    SECRET_KEY = os.getenv("SECRET_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()
