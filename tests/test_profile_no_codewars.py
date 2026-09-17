from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoSkillScoreWidgetTests(unittest.TestCase):
    def test_no_unrelated_scores(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("codewars", "leetcode", "hackerrank"):
                self.assertNotIn(term, text)

if __name__ == "__main__":
    unittest.main()
