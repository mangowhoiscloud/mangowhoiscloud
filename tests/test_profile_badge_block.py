"""Keep one compact Shields block near the top of each profile language."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeBlockTests(unittest.TestCase):
    def test_badges_before_navigation(self):
        for filename, nav in (("README.md", "[작업 방식]"), ("README_EN.md", "[How I work]")):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertLess(text.index("img.shields.io/"), text.index(nav))


if __name__ == "__main__":
    unittest.main()
