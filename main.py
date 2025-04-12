from config import (
    USE_API,
    API_URL,
    SCRAPE_URL,
    EXPORT_CSV,
    EXPORT_EXCEL,
    DB_PATH,
    TABLE_NAME,
)
from extractor.api_extractor import extract_from_api
from extractor.web_scraper import extract_from_website
from exporter.to_csv import export_to_csv
from exporter.to_excel import export_to_excel
from exporter.to_sqlite import export_to_sqlite


def main():
    # Step 1: Extract
    if USE_API:
        df = extract_from_api(API_URL)
    else:
        df = extract_from_website(SCRAPE_URL)

    # Step 2: Export
    export_to_csv(df, EXPORT_CSV)
    export_to_excel(df, EXPORT_EXCEL)
    export_to_sqlite(df, DB_PATH, TABLE_NAME)

    print("✅ All tasks completed successfully.")


if __name__ == "__main__":
    main()
