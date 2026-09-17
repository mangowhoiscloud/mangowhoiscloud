from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReodeScopeTests(unittest.TestCase):
    def test_zero_intervention_scope(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("해당 실행 중 사람 개입은 0회", ko)
        self.assertIn("zero human intervention during that run", en)
        self.assertIn("준비, 설계, 최종 검토", ko)
        self.assertIn("preparation, design, or final review", en)

if __name__ == "__main__":
    unittest.main()
