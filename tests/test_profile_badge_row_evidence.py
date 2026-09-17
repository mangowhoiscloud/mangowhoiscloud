from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeRowEvidenceTests(unittest.TestCase):
    def test_evidence(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("Evidence-open%20records"), 1)

if __name__ == "__main__":
    unittest.main()
