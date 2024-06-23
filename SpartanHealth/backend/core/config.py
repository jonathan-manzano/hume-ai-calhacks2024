# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class Settings:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    # PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    # PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
    HUME_API_URL = "https://api.hume.ai/v1/analyze"
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    HUME_SECRET_KEY = os.getenv("HUME_SECRET_KEY")


settings = Settings()
