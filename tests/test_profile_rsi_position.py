"""Keep RSI visible before readers reach the project list."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RsiPositionTests(unittest.TestCase):
    def test_rsi_before_projects(self):
        for filename, marker in (("README.md", "## 대표 작업"), ("README_EN.md", "## Selected work")):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertLess(text.index("RSI (Recursive Self-Improvement)"), text.index(marker))


if __name__ == "__main__":
    unittest.main()
