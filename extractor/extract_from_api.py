import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Or name it specific like OPENWEATHER_API_KEY


def extract_from_api(url, headers=None, params=None):
    # Add API key to params if needed
    if API_KEY:
        if params is None:
            params = {}
        params["appid"] = API_KEY  # Change key name if your API uses a different name

    print(f"Fetching data from API: {url}")
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    # Handle single-object or list JSON responses
    if isinstance(data, dict):
        return pd.DataFrame([data])
    else:
        return pd.DataFrame(data)
