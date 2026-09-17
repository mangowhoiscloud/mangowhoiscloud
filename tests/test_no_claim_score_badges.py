"""Avoid badges that imply unsupported quality or autonomy scores."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoClaimScoreBadgeTests(unittest.TestCase):
    def test_no_score_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("autonomy%20score", "rsi%20score", "quality%20score", "agent%20score"):
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
