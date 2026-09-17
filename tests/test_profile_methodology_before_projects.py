from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class MethodologyPositionTests(unittest.TestCase):
    def test_position(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertLess(ko.index("방법론 자체를 탐색 공간으로 둡니다"), ko.index("## 대표 작업"))
        self.assertLess(en.index("Treat methodology itself as a search space"), en.index("## Selected work"))

if __name__ == "__main__":
    unittest.main()
