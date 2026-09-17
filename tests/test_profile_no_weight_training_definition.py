from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiNonparametricTests(unittest.TestCase):
    def test_nonparametric_scope(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("실행 구성을 탐색", ko)
        self.assertIn("searches the execution scaffold", en)

if __name__ == "__main__":
    unittest.main()
