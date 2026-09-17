from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SearchNotClosedTests(unittest.TestCase):
    def test_search_not_closed(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(ko.count("탐색 공간은 닫지 않습니다"), 2)
        self.assertGreaterEqual(en.lower().count("search space"), 5)

if __name__ == "__main__":
    unittest.main()
