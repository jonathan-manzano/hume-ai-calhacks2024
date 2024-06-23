# app/services/hume_ai.py
import requests
from SpartanHealth.backend.core.config import settings


class HumeAIService:
    def __init__(self):
        self.api_url = settings.HUME_API_URL
        self.api_key = settings.HUME_API_KEY

    def analyze_text(self, text: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "texts": [text],
            "models": ["emotion"]
        }

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


hume_ai_service = HumeAIService()
