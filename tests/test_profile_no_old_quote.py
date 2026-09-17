from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OldQuoteTests(unittest.TestCase):
    def test_old_quote_absent(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertNotIn("사람이 어디를 봐야 할지 분명한 자동화", ko)
        self.assertNotIn("what a person should review", en)

if __name__ == "__main__":
    unittest.main()
