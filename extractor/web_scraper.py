import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_from_website(url):
    print(f"Scraping data from website: {url}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")
    data = []
    for quote in quotes:
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        data.append({"quote": text, "author": author})
    return pd.DataFrame(data)
