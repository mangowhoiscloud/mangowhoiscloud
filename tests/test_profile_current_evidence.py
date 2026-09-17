from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CurrentEvidenceTests(unittest.TestCase):
    def test_evidence_and_rsi_adjacent(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            evidence = text.index("Evidence-open%20records")
            rsi = text.index("RSI-scaffold%20search")
            self.assertLess(abs(rsi - evidence), 1000)

if __name__ == "__main__":
    unittest.main()
