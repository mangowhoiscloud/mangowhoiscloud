"""Keep RSI badge descriptive of the actual scaffold-search work."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RsiBadgeScopeTests(unittest.TestCase):
    def test_rsi_badge_scope(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("RSI-scaffold%20search", text)
            self.assertNotIn("RSI-self%20training", text)
            self.assertNotIn("RSI-proven", text)


if __name__ == "__main__":
    unittest.main()
