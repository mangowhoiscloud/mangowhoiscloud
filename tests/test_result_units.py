"""Keep key public results attached to their units."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResultUnitTests(unittest.TestCase):
    def test_korean_units(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in ("46,080개 출력값", "720개 일반 테스트", "5,523개 파일", "1,000 VU", "1,477 RPS"):
            self.assertIn(phrase, text)

    def test_english_units(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for phrase in ("46,080 matching output values", "720 regular tests", "5,523 file", "1,000 VU", "1,477 RPS"):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
