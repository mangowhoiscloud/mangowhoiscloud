from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoLanguagePercentTests(unittest.TestCase):
    def test_no_language_stats(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            self.assertNotIn("languages?", text)
            self.assertNotIn("top-langs", text)

if __name__ == "__main__":
    unittest.main()
