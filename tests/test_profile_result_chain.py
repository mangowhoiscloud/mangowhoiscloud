from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResultChainTests(unittest.TestCase):
    def test_chain(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("회귀 테스트", ko)
        self.assertIn("Skill", ko)
        self.assertIn("다음 후보", ko)
        self.assertIn("regression test", en)
        self.assertIn("Skill", en)
        self.assertIn("next candidate", en)

if __name__ == "__main__":
    unittest.main()
