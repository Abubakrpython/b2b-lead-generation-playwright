from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


URL = "https://realpython.github.io/fake-jobs/"


def main():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    time.sleep(3)  # manual wait (anti-pattern)

    cards = driver.find_elements(By.CLASS_NAME, "card-content")
    print(f"Found {len(cards)} job cards")

    jobs = []
    for card in cards:
        title = card.find_element(By.CLASS_NAME, "title").text
        company = card.find_element(By.CLASS_NAME, "company").text
        location = card.find_element(By.CLASS_NAME, "location").text

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    print(jobs[:3])
    driver.quit()


if __name__ == "__main__":
    main()
