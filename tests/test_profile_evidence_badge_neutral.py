from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EvidenceBadgeNeutralTests(unittest.TestCase):
    def test_neutral_evidence_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("Evidence-open%20records-555555?style=flat-square", text)

if __name__ == "__main__":
    unittest.main()
