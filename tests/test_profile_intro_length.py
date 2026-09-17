"""Keep the intro focused before navigation and selected work."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class IntroLengthTests(unittest.TestCase):
    def test_intro_not_excessive(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            marker = "[작업 방식]" if filename == "README.md" else "[How I work]"
            self.assertLess(len(text[:text.index(marker)]), 3500)


if __name__ == "__main__":
    unittest.main()
