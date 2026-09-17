"""Avoid visitor counters and tracking-oriented profile visuals."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoVisitorCounterTests(unittest.TestCase):
    def test_no_counter_services(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("ghpvc", "profile-counter", "visitor count", "profile views"):
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
