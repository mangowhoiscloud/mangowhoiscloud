from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeRowNoCompilerTests(unittest.TestCase):
    def test_badge_row(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            start = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", start)
            block = text[start:end]
            self.assertNotIn("Compiler", block)
            self.assertNotIn("CPU", block)

if __name__ == "__main__":
    unittest.main()
