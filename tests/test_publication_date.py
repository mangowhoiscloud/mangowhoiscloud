"""Keep the content review date explicit."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicationDateTests(unittest.TestCase):
    def test_review_date(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertIn("2026-09-17", (ROOT / filename).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
