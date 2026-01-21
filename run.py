from scraper.browser import BrowserManager
from scraper.scraper import JobScraper
from scraper.parser import LeadParser
import yaml


TARGET_URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_PATH = "output/leads.csv"


def load_filters(path="config/filters.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    browser_manager = BrowserManager()
    playwright, browser, context = browser_manager.launch()
    page = context.new_page()

    scraper = JobScraper(page)
    filters = load_filters()
    parser = LeadParser(filters)

    all_jobs = []

    try:
        scraper.open(TARGET_URL)

        jobs = scraper.scrape_current_page()
        all_jobs.extend(jobs)

        print(f"[INFO] Raw jobs: {len(all_jobs)}")

        leads = parser.filter_jobs(all_jobs)
        print(f"[INFO] Filtered leads: {len(leads)}")

        parser.export_csv(leads, OUTPUT_PATH)
        print(f"[DONE] CSV exported → {OUTPUT_PATH}")

    finally:
        browser_manager.close(playwright, browser)


if __name__ == "__main__":
    main()
