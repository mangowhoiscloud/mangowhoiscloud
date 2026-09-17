"""Keep scaffold search explicit in both languages and the badge."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ScaffoldTermTests(unittest.TestCase):
    def test_scaffold_search(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("비파라메트릭 scaffold 탐색", ko)
        self.assertIn("non parametric form of RSI scaffold search", en)
        for text in (ko, en):
            self.assertIn("RSI-scaffold%20search", text)


if __name__ == "__main__":
    unittest.main()
