from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SearchLoopRecordTests(unittest.TestCase):
    def test_record_stage(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("탐색 루프: 후보 → 평가 → 기록 → 다음 후보와 탐색 전략", ko)
        self.assertIn("search loop:  candidate → evaluation → record → next candidate and search strategy", en)

if __name__ == "__main__":
    unittest.main()
