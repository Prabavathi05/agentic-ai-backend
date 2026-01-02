import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# force load .env from project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str, day: str):
    if not API_KEY:
        return "Weather API key not found ❌"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Weather API error ❌ (status code: {response.status_code})"

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The weather in {city} today is {description} with temperature {temp}°C 🌤️"
