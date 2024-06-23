# app/services/hume_ai.py
import requests
from SpartanHealth.core.config import settings

def analyze_text(text: str):
    headers = {
        "Authorization": f"Bearer {settings.SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "texts": [text],
        "models": ["emotion"]
    }

    response = requests.post(settings.HUME_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
