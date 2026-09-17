from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeRowPositionTests(unittest.TestCase):
    def test_badge_row_near_top(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertLess(text.index("img.shields.io/"), 3000)

if __name__ == "__main__":
    unittest.main()
