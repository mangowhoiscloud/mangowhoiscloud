from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EvidenceBadgePublicTests(unittest.TestCase):
    def test_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('<a href="https://github.com/mangowhoiscloud/geode-eval-artifacts"><img src="https://img.shields.io/badge/Evidence-', text)

if __name__ == "__main__":
    unittest.main()
