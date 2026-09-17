from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Eco2PortfolioUrlTests(unittest.TestCase):
    def test_current_url(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("https://mangowhoiscloud.github.io/eco2/", text)
            self.assertNotIn("https://mangowhoiscloud.github.io/portfolio/eco2", text)

if __name__ == "__main__":
    unittest.main()
