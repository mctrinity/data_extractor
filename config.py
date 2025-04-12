import os
from dotenv import load_dotenv

load_dotenv()

USE_API = os.getenv("USE_API", "true").lower() == "true"
API_URL = os.getenv("API_URL")
SCRAPE_URL = os.getenv("SCRAPE_URL")
EXPORT_CSV = os.getenv("EXPORT_CSV")
EXPORT_EXCEL = os.getenv("EXPORT_EXCEL")
DB_PATH = os.getenv("DB_PATH")
TABLE_NAME = os.getenv("TABLE_NAME", "data")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
