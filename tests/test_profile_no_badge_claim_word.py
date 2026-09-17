from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeClaimWordTests(unittest.TestCase):
    def test_no_superlative_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("badge/best", "badge/expert", "badge/advanced", "badge/leading"):
                self.assertNotIn(term, text)

if __name__ == "__main__":
    unittest.main()
