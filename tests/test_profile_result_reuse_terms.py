"""Keep successful and unsuccessful result types explicit as future inputs."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResultReuseTermTests(unittest.TestCase):
    def test_korean_types(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for term in ("성공한 변경", "실패한 시도", "기각된 가설", "실행 궤적", "평가 결과"):
            self.assertIn(term, text)

    def test_english_types(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("Successful changes", "failed attempts", "rejected hypotheses", "execution trajectories", "evaluation results"):
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
