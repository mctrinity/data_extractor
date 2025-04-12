# 🧰 Data Extractor – API & Web Scraping Tool

This project is a modular Python application that extracts data from either a **REST API** or a **webpage**, and exports it into structured formats like **CSV**, **Excel**, or a **SQLite database**.

It features both:

- ✅ A **command-line interface (CLI)** for automated/scheduled runs
- 🌐 A **Streamlit web UI** for easy, user-friendly interaction

---

## 🚀 Features

- Extract from:
  - RESTful API endpoints (JSON responses)
  - Static HTML web pages (using BeautifulSoup)
- Export to:
  - CSV
  - Excel (.xlsx)
  - SQLite Database
- Streamlit web UI with form-based inputs
- CLI support via `main.py`
- Modular codebase for easy extension
- Optional `.env` file support for API keys and config

---

## 📂 Project Structure

```
data_extractor/
├── config.py
├── main.py
├── .env
├── README.md
├── extractor/
│   ├── api_extractor.py
│   └── web_scraper.py
├── exporter/
│   ├── to_csv.py
│   ├── to_excel.py
│   └── to_sqlite.py
├── ui/
│   └── streamlit_app.py
├── data/
│   └── (output files go here)
```

---

## 🧪 Running the Project

### 📌 Prerequisites

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
streamlit
pandas
requests
beautifulsoup4
openpyxl
python-dotenv
```

---

### 🛠️ Configuration via `.env`

Create a `.env` file in your project root to securely manage config and API keys:

```
USE_API=true
API_URL=https://jsonplaceholder.typicode.com/posts
SCRAPE_URL=https://quotes.toscrape.com/
EXPORT_CSV=data/output.csv
EXPORT_EXCEL=data/output.xlsx
DB_PATH=data/output.db
TABLE_NAME=data
OPENWEATHER_API_KEY=your_api_key_here
```

These values are automatically loaded in `config.py` using `python-dotenv`. The file starts with:

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

This allows all environment variables from the `.env` file to be accessed using `os.getenv()`.

---

### 🖥 CLI Mode

Run the extractor directly via terminal:

```bash
python main.py
```

Make sure your `.env` file is set up. Alternatively, you can edit `config.py` directly if not using environment variables.

---

### 🌐 Streamlit Web UI

### 🔗 Live Demo

You can try the app instantly here: [Launch Streamlit App](https://mctrinity-data-extractor-uistreamlit-app-e2zp8b.streamlit.app/)

```bash
streamlit run ui/streamlit_app.py
```

This will launch a local web interface where you can:

- Choose source type (API or website)
- Input a URL and optional API key
- Select export formats
- Preview extracted data

---

## 📁 Output

All exported files are saved to the `/data/` directory.

---

## 📬 Contact

Built by an experienced Python developer for data automation and extraction tasks. Feel free to reach out for enhancements or integrations.

---

## 🛡 License

MIT License – free to use and modify.
