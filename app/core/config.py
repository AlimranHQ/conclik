import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "ContentPilot AI"

    VERSION = "4.0.0"

    DEBUG = True

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")


settings = Settings()
