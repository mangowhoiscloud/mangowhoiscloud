"""Keep the methodology search space broader than prompts alone."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SearchSpaceTermTests(unittest.TestCase):
    def test_korean_terms(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for term in ("문제 분해", "컨텍스트", "도구", "Skill", "평가", "사람의 개입"):
            self.assertIn(term, text)

    def test_english_terms(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("task decomposition", "context", "tool", "Skills", "evaluation", "human intervention"):
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
