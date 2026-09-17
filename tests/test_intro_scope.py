"""Keep the profile's three current domains explicit near the top."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class IntroScopeTests(unittest.TestCase):
    def test_korean_intro(self):
        intro = (ROOT / "README.md").read_text(encoding="utf-8")[:1800]
        for term in ("분산 스토리지", "클라우드 인프라", "자율 에이전트", "Recursive Self-Improvement"):
            self.assertIn(term, intro)

    def test_english_intro(self):
        intro = (ROOT / "README_EN.md").read_text(encoding="utf-8")[:1800]
        for term in ("distributed storage", "cloud infrastructure", "autonomous agent", "Recursive Self-Improvement"):
            self.assertIn(term, intro)


if __name__ == "__main__":
    unittest.main()
