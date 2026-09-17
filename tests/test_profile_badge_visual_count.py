from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualCountTests(unittest.TestCase):
    def test_six_total_images(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("<img ") + text.count("![Profile checks]"), 6)

if __name__ == "__main__":
    unittest.main()
