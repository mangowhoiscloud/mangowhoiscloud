"""Keep the profile's own validation status visible and separate from project claims."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProfileCiBadgeTests(unittest.TestCase):
    def test_ci_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("actions/workflows/profile.yml/badge.svg?branch=main", text)
            self.assertIn("actions/workflows/profile.yml", text)


if __name__ == "__main__":
    unittest.main()
