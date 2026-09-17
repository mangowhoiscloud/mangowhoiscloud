"""Keep the compact feedback loop in causal order."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LoopOrderTests(unittest.TestCase):
    def test_korean_order(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        line = next(line for line in text.splitlines() if "가설 → 실행 → 관찰" in line)
        self.assertEqual(line, "가설 → 실행 → 관찰 → 검증 → 기록")

    def test_english_order(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        line = next(line for line in text.splitlines() if "hypothesis → execution" in line)
        self.assertEqual(line, "hypothesis → execution → observation → verification → record")


if __name__ == "__main__":
    unittest.main()
