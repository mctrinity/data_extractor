import requests
import pandas as pd


def extract_from_api(url):
    print(f"Fetching data from API: {url}")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)
