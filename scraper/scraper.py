from playwright.sync_api import Page
from typing import List, Dict
from scraper.anti_bot import HumanBehavior


class JobScraper:
    def __init__(self, page: Page):
        self.page = page
        self.human = HumanBehavior()

    def open(self, url: str):
        print(f"[INFO] Opening target: {url}")
        self.page.goto(url, timeout=60000)
        self.page.wait_for_load_state("domcontentloaded")

        self.human.scroll_page(self.page)

    def get_job_cards(self):
        return self.page.locator(".card-content")

    def scrape_current_page(self) -> List[Dict]:
        print("[INFO] Scraping current page...")
        jobs = []

        self.human.before_action(self.page)

        cards = self.get_job_cards()
        count = cards.count()
        print(f"[INFO] Found {count} job cards")

        for i in range(count):
            card = cards.nth(i)

            title = card.locator("h2.title").inner_text()
            company = card.locator("h3.company").inner_text()
            location = card.locator("p.location").inner_text()

            jobs.append({
                "title": title.strip(),
                "company": company.strip(),
                "location": location.strip(),
            })

            self.human.wait(self.page)

        return jobs
