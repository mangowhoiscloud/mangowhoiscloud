from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EvidenceTermTests(unittest.TestCase):
    def test_concrete_evidence_terms(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("테스트 결과", "원본 로그", "실행 궤적", "평가 결과"):
            self.assertIn(term, ko)
        for term in ("test results", "original logs", "execution trajectories", "evaluation results"):
            self.assertIn(term, en)

if __name__ == "__main__":
    unittest.main()
