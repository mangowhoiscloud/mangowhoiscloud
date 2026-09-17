from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiBadgePublicTests(unittest.TestCase):
    def test_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('<a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/RSI-', text)

if __name__ == "__main__":
    unittest.main()
