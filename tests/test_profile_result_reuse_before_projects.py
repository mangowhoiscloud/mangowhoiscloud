from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResultReusePositionTests(unittest.TestCase):
    def test_position(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertLess(ko.index("결과를 다음 탐색의 데이터로 남깁니다"), ko.index("## 대표 작업"))
        self.assertLess(en.index("Preserve results as data for the next search"), en.index("## Selected work"))

if __name__ == "__main__":
    unittest.main()
