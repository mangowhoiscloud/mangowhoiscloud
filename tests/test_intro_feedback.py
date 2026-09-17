"""Keep feedback into the next search visible before the project list."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class IntroFeedbackTests(unittest.TestCase):
    def test_intro_feedback(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertLess(ko.index("다음 실험의 재료"), ko.index("## 대표 작업"))
        self.assertLess(en.index("material for the next experiment"), en.index("## Selected work"))


if __name__ == "__main__":
    unittest.main()
