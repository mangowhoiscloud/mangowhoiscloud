from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class DistinctExecutionTests(unittest.TestCase):
    def test_distinct_execution_language(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("서로 다른 실행의 수치를 하나의 점수로 합치지 않습니다", ko)
        self.assertIn("separate executions and are not combined into one score", en)

if __name__ == "__main__":
    unittest.main()
