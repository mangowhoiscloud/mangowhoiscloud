from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IntroMethodologyTests(unittest.TestCase):
    def test_methodology_in_intro(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertLess(ko.index("방법론 자체를 탐색 대상"), ko.index("[GEODE]"))
        self.assertLess(en.index("methodology itself"), en.index("[GEODE]"))

if __name__ == "__main__":
    unittest.main()
