import random
import math
from playwright.sync_api import Page


class HumanBehavior:
    def __init__(
        self,
        min_delay: float = 0.3,
        max_delay: float = 1.5
    ):
        self.min_delay = min_delay
        self.max_delay = max_delay

    def _random_delay(self) -> float:
        """
        Normal distribution delay (more human than uniform)
        """
        mean = (self.min_delay + self.max_delay) / 2
        std_dev = (self.max_delay - self.min_delay) / 4
        delay = random.gauss(mean, std_dev)
        return max(self.min_delay, min(delay, self.max_delay))

    def wait(self, page: Page):
        delay = self._random_delay()
        page.wait_for_timeout(int(delay * 1000))

    def scroll_page(self, page: Page, steps: int = 5):
        """
        Scroll page gradually (human-like)
        """
        for _ in range(steps):
            scroll_by = random.randint(200, 600)
            page.mouse.wheel(0, scroll_by)
            self.wait(page)

    def move_mouse_randomly(self, page: Page):
        """
        Random mouse movement inside viewport
        """
        width = page.viewport_size["width"]
        height = page.viewport_size["height"]

        x = random.randint(0, width)
        y = random.randint(0, height)

        page.mouse.move(x, y, steps=random.randint(5, 15))
        self.wait(page)

    def before_action(self, page: Page):
        """
        Call before important actions (click, scrape, paginate)
        """
        self.move_mouse_randomly(page)
        self.wait(page)
