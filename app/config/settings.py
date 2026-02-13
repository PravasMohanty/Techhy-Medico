import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    ENV = os.getenv("ENV")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME")

    AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", 0.4))
    AI_TOP_P = float(os.getenv("AI_TOP_P", 1))
    AI_TOP_K = int(os.getenv("AI_TOP_K", 32))
    AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", 4096))

settings = Settings()
