"""Prevent previously rejected playful profile copy from returning."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TonePhraseTests(unittest.TestCase):
    def test_rejected_korean_phrases_absent(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in ("일단 돌아가네요", "삽질", "작업으로 소개할게요", "낯선 단어는 여기서 잠깐"):
            self.assertNotIn(phrase, text)

    def test_rejected_english_phrases_absent(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for phrase in ("It's working!", "Let the work introduce me", "A small glossary, no prerequisites"):
            self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
