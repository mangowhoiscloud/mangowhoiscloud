from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoPlayfulEnglishTests(unittest.TestCase):
    def test_words_absent(self):
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for phrase in ("favorite follow-up", "Always happy", "no prerequisites", "Let the work"):
            self.assertNotIn(phrase, en)

if __name__ == "__main__":
    unittest.main()
