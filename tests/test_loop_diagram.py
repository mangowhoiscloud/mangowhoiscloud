"""Keep the compact feedback loop visible in both languages."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LoopDiagramTests(unittest.TestCase):
    def test_korean_loop(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for term in ("가설", "실행", "관찰", "검증", "기록", "다음 후보와 방법론"):
            self.assertIn(term, text)

    def test_english_loop(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for term in ("hypothesis", "execution", "observation", "verification", "record", "next candidate and methodology"):
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
