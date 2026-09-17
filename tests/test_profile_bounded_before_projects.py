from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BoundedPositionTests(unittest.TestCase):
    def test_position(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertLess(ko.index("개별 실행은 유한하게 닫고 탐색 공간은 닫지 않습니다"), ko.index("## 대표 작업"))
        self.assertLess(en.index("Bound individual runs without closing the search space"), en.index("## Selected work"))

if __name__ == "__main__":
    unittest.main()
