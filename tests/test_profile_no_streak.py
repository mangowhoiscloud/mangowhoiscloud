"""Avoid contribution streak widgets as an engineering signal."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoStreakTests(unittest.TestCase):
    def test_no_streak(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            self.assertNotIn("streak", text)


if __name__ == "__main__":
    unittest.main()
