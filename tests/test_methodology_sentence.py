"""Keep methodology explicitly positioned as an object of search."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MethodologySentenceTests(unittest.TestCase):
    def test_methodology(self):
        self.assertIn("방법론 자체를 탐색 공간으로 둡니다", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("Treat methodology itself as a search space", (ROOT / "README_EN.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
