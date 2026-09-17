"""Keep task execution and methodology search as distinct loops."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SearchLoopTermTests(unittest.TestCase):
    def test_two_loop_labels(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("작업 루프:", ko)
        self.assertIn("탐색 루프:", ko)
        self.assertIn("task loop:", en)
        self.assertIn("search loop:", en)


if __name__ == "__main__":
    unittest.main()
