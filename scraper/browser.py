from playwright.sync_api import sync_playwright
from pathlib import Path
import yaml


class BrowserManager:
    def __init__(self, config_path: str = "config/browser.yaml"):
        self.config = self._load_config(config_path)

    def _load_config(self, path: str) -> dict:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def launch(self):
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=self.config.get("headless", True),
            slow_mo=self.config.get("slow_mo", 0)
        )

        context = browser.new_context(
            user_agent=self.config.get("user_agent"),
            viewport=self.config.get("viewport", {"width": 1280, "height": 800}),
            locale="en-US"
        )

        return playwright, browser, context

    def close(self, playwright, browser):
        browser.close()
        playwright.stop()
