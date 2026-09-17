"""Keep the top visualization compact rather than turning it into a badge wall."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeCountTests(unittest.TestCase):
    def test_five_top_badges_plus_profile_check(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("img.shields.io/"), 5, filename)
            self.assertEqual(text.count("actions/workflows/profile.yml/badge.svg"), 1, filename)


if __name__ == "__main__":
    unittest.main()
