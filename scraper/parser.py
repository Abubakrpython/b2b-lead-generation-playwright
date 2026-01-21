from typing import List, Dict
import csv
from pathlib import Path


class LeadParser:
    def __init__(self, filters: dict):
        self.filters = filters

    def filter_jobs(self, jobs: List[Dict]) -> List[Dict]:
        filtered = []

        for job in jobs:
            title = job["title"].lower()
            location = job["location"].lower()

            if not self._match_title(title):
                continue

            if not self._match_location(location):
                continue

            filtered.append(job)

        return self._deduplicate(filtered)

    def _match_title(self, title: str) -> bool:
        return any(keyword in title for keyword in self.filters["job_titles"])

    def _match_location(self, location: str) -> bool:
        return any(loc in location for loc in self.filters["locations"])

    def _deduplicate(self, jobs: List[Dict]) -> List[Dict]:
        seen = set()
        unique = []

        for job in jobs:
            key = (job["title"], job["company"])
            if key in seen:
                continue
            seen.add(key)
            unique.append(job)

        return unique

    def export_csv(self, jobs: List[Dict], path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["title", "company", "location"]
            )
            writer.writeheader()
            writer.writerows(jobs)
