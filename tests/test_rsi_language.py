"""Keep RSI wording explicit about scaffold search and evidence boundaries."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RsiLanguageTests(unittest.TestCase):
    def test_korean_rsi_scope(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("모델 가중치를 직접 학습시키는 대신 실행 구성을 탐색", text)
        self.assertIn("지속적인 자기개선이 입증됐다고 전제하지 않습니다", text)

    def test_english_rsi_scope(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("execution scaffold rather than directly training model weights", text)
        self.assertIn("without assuming that sustained self improvement has already been established", text)


if __name__ == "__main__":
    unittest.main()
