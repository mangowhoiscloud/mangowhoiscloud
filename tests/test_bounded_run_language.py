"""Keep the distinction between bounded executions and open-ended search."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BoundedRunLanguageTests(unittest.TestCase):
    def test_korean(self):
        self.assertIn("개별 실행은 유한하게 닫고 탐색 공간은 닫지 않습니다", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_english(self):
        self.assertIn("Bound individual runs without closing the search space", (ROOT / "README_EN.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
