"""Keep the profile heading simple and professional."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProfileHeadingTests(unittest.TestCase):
    def test_headings(self):
        self.assertIn("\n# 류지환\n", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("\n# Jihwan Ryu\n", (ROOT / "README_EN.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
