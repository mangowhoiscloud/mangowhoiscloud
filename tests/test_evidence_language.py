"""Keep evidence reuse, not just evidence preservation, explicit."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceLanguageTests(unittest.TestCase):
    def test_korean(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("다음 실험 설계의 입력", text)
        self.assertIn("다음 후보를 만들고 탐색 공간을 조정하는 입력", text)

    def test_english(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("inputs to later analysis, learning views, and experiment design", text)
        self.assertIn("inform the next candidate and the shape of the search space", text)


if __name__ == "__main__":
    unittest.main()
