from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoPlayfulWordsTests(unittest.TestCase):
    def test_words_absent(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        for word in ("반갑지만", "좋아합니다", "삽질", "잠깐"):
            self.assertNotIn(word, ko)

if __name__ == "__main__":
    unittest.main()
