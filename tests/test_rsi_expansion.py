"""Keep RSI expanded for readers outside the immediate research niche."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RsiExpansionTests(unittest.TestCase):
    def test_expansion(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("RSI (Recursive Self-Improvement)", text)


if __name__ == "__main__":
    unittest.main()
