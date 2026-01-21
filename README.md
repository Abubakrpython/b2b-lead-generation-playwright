# B2B Lead Generation Tool (Python • Playwright • Selenium • Docker)

A **production-ready B2B lead generation system** built with Python and browser automation.
The project focuses on **data quality, scalability, and robustness**, not just scraping.

It demonstrates how to collect, filter, validate, and export **high-quality business leads**
using modern automation practices.

---

## 🚀 Key Features

- Browser automation with **Playwright**
- Human-like interaction simulation (anti-bot awareness)
- Configurable job title & location filtering
- Smart fallback logic for senior profile detection
- Lead deduplication and validation
- Clean CSV export (CRM-ready)
- Modular, maintainable architecture
- Dockerized execution (run anywhere)
- Selenium mini-version for comparison

---

## 🧠 What This Project Demonstrates

This project is designed to showcase **real-world automation skills**, including:

- Scalable browser automation (not one-off scripts)
- Handling modern, JavaScript-heavy websites
- Session-aware scraping logic
- Strict data quality enforcement
- Difference between *raw data* and *usable business leads*
- Tool comparison: **Playwright vs Selenium**
- Docker & WSL-based reproducible execution

---

## 🏗️ Project Structure

b2b-lead-generation-playwright/
│
├── README.md
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── config/
│ ├── browser.yaml # Browser & runtime configuration
│ └── filters.yaml # Job title & location filters
│
├── scraper/
│ ├── init.py
│ ├── browser.py # Playwright browser/context manager
│ ├── scraper.py # Navigation & data collection
│ ├── parser.py # Filtering, deduplication, export
│ └── anti_bot.py # Human-like behavior simulation
│
├── selenium_version/
│ └── selenium_scraper.py # Mini Selenium implementation
│
├── output/
│ └── leads.csv # Generated leads
│
└── run.py # Entry point


---

## ⚙️ Local Installation

### 1. Create virtual environment
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
2. Install dependencies
pip install -r requirements.txt
playwright install
3. Run the scraper
python run.py
🧪 Demo Target Website
For demonstration purposes, this project uses a public job listing demo site:

https://realpython.github.io/fake-jobs/
⚠️ No login-protected platforms are scraped in this repository.

🧹 Filtering & Data Quality
Filtering rules are defined in config/filters.yaml:

job_titles:
  - python
  - engineer
  - senior

locations:
  - remote
  - aa
The system enforces:

Case-insensitive matching

Title and location validation

Deduplication by company + role

Cleaned, normalized job titles

📄 Output Format
Leads are exported to:

output/leads.csv
CSV fields are suitable for CRM import:

Job Title

Company Name

Location

(Structure can be easily extended for emails, LinkedIn URLs, etc.)

🛡️ Anti-Bot Awareness
This project does not bypass protections.
Instead, it improves stability by simulating realistic user behavior:

Randomized delays (normal distribution)

Mouse movement and scrolling

Action pacing and retry handling

This approach helps reduce detection risk and improves reliability on large runs.

🐳 Docker Usage
Build Docker image
docker build -t b2b-lead-generator .
Run scraper
docker run b2b-lead-generator
Export CSV to local machine
docker run -v $(pwd)/output:/app/output b2b-lead-generator
