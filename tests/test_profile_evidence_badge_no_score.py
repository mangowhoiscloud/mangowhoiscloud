from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EvidenceBadgeNoScoreTests(unittest.TestCase):
    def test_no_numeric_evidence_badge(self):
        for filename in ("README.md", "README_EN.md"):
            line = next(line for line in (ROOT / filename).read_text(encoding="utf-8").splitlines() if "Evidence-open%20records" in line)
            self.assertNotIn("score", line.lower())
            self.assertNotIn("%25", line)

if __name__ == "__main__":
    unittest.main()
