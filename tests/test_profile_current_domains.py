from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CurrentDomainTests(unittest.TestCase):
    def test_domains_in_badge_row(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            first_p = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", first_p)
            block = text[first_p:end]
            self.assertIn("RSI", block)
            self.assertIn("Autonomous%20Agents", block)
            self.assertIn("Cloud", block)

if __name__ == "__main__":
    unittest.main()
