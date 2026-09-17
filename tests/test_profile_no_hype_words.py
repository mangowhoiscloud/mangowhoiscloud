from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoHypeWordsTests(unittest.TestCase):
    def test_no_hype_words(self):
        forbidden = ("revolutionary", "cutting-edge", "world-class", "game-changing", "혁신적인", "압도적", "세계 최고")
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for word in forbidden:
                self.assertNotIn(word.lower(), text)

if __name__ == "__main__":
    unittest.main()
