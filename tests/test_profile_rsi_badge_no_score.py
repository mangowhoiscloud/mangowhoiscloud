from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiBadgeNoScoreTests(unittest.TestCase):
    def test_no_numeric_rsi_badge(self):
        for filename in ("README.md", "README_EN.md"):
            line = next(line for line in (ROOT / filename).read_text(encoding="utf-8").splitlines() if "RSI-scaffold%20search" in line)
            self.assertNotIn("%25", line)
            self.assertNotIn("score", line.lower())

if __name__ == "__main__":
    unittest.main()
