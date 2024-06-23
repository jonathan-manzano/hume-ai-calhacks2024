# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class Settings:
    HUME_API_URL = "https://api.hume.ai/v1/analyze"
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    HUME_SECRET_KEY = os.getenv("HUME_SECRET_KEY")


settings = Settings()
