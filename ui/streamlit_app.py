import streamlit as st
import pandas as pd

import sys
import os

# ✅ Make the parent directory visible to Streamlit for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from extractor.api_extractor import extract_from_api
from extractor.web_scraper import extract_from_website
from exporter.to_csv import export_to_csv
from exporter.to_excel import export_to_excel
from exporter.to_sqlite import export_to_sqlite

st.set_page_config(page_title="Data Extractor", layout="centered")

st.title("🧰 Data Extractor")
st.markdown(
    "Extract data from an API or a website and export it to your preferred format."
)

with st.form("extract_form"):
    source_type = st.selectbox("Select Data Source Type", ["API", "Web Scraping"])
    url = st.text_input(
        "Enter the URL", placeholder="https://example.com or API endpoint"
    )
    export_formats = st.multiselect(
        "Select Export Format(s)", ["CSV", "Excel", "SQLite"], default=["CSV"]
    )
    table_name = None
    if "SQLite" in export_formats:
        table_name = st.text_input("SQLite Table Name", value="data")

    submitted = st.form_submit_button("Extract and Export")

if submitted:
    if not url:
        st.error("Please enter a URL.")
    else:
        try:
            # Extract data
            if source_type == "API":
                df = extract_from_api(url)
            else:
                df = extract_from_website(url)

            st.success("✅ Data extracted successfully!")
            st.dataframe(df.head())

            # Export
            if "CSV" in export_formats:
                export_to_csv(df, "data/output.csv")
                st.download_button(
                    "Download CSV",
                    data=df.to_csv(index=False),
                    file_name="output.csv",
                    mime="text/csv",
                )

            if "Excel" in export_formats:
                export_to_excel(df, "data/output.xlsx")
                excel_buffer = df.to_excel(index=False, engine="openpyxl")
                st.download_button(
                    "Download Excel",
                    data=excel_buffer,
                    file_name="output.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

            if "SQLite" in export_formats and table_name:
                export_to_sqlite(df, "data/output.db", table_name)
                st.success(f"🗄 Data saved to SQLite table `{table_name}`.")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
