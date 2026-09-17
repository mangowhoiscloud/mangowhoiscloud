from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SearchDirectionTests(unittest.TestCase):
    def test_result_determines_direction(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("결과에 따라 다음 탐색 방향을 정합니다", ko)
        self.assertIn("let the result determine the next direction of search", en)

if __name__ == "__main__":
    unittest.main()
