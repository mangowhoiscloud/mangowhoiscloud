"""Keep top Shields badges in a compact flat-square treatment."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeStyleTests(unittest.TestCase):
    def test_flat_square(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            badge_lines = [line for line in text.splitlines() if "img.shields.io/" in line]
            self.assertEqual(len(badge_lines), 5)
            for line in badge_lines:
                self.assertIn("style=flat-square", line)


if __name__ == "__main__":
    unittest.main()
