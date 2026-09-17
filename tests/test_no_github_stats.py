"""Avoid account-level GitHub stats as a substitute for engineering evidence."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoGithubStatsTests(unittest.TestCase):
    def test_no_account_stat_labels(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for phrase in ("total commits", "contribution streak", "top languages", "profile views"):
                self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
