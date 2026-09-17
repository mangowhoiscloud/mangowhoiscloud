"""Keep evidence as a first-class visual signal."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceBadgeTests(unittest.TestCase):
    def test_evidence_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("img.shields.io/badge/Evidence-open%20records-555555", text)
            self.assertIn("https://github.com/mangowhoiscloud/geode-eval-artifacts", text)


if __name__ == "__main__":
    unittest.main()
