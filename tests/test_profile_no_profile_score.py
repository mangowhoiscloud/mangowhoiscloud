"""Avoid aggregate profile scores that obscure evidence scope."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoProfileScoreTests(unittest.TestCase):
    def test_no_profile_score(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("profile score", "developer score", "github score"):
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
