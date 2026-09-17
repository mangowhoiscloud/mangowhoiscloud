from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class DetailsSummaryTests(unittest.TestCase):
    def test_details_summaries(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("<summary><strong>그 밖의 작업</strong></summary>", ko)
        self.assertIn("<summary><strong>검증과 탐색에 사용하는 개념</strong></summary>", ko)
        self.assertIn("<summary><strong>Other work</strong></summary>", en)
        self.assertIn("<summary><strong>Concepts used for verification and search</strong></summary>", en)

if __name__ == "__main__":
    unittest.main()
