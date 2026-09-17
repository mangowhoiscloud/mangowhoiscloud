"""Keep LLM judges framed as supporting instruments."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvaluatorBoundaryTests(unittest.TestCase):
    def test_judge_boundary(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("LLM 심판도 보조 수단", ko)
        self.assertIn("LLM judge remains a supporting instrument", en)


if __name__ == "__main__":
    unittest.main()
