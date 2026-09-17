from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CategoricalSignalCountTests(unittest.TestCase):
    def test_four_static_signals(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("https://img.shields.io/badge/"), 4)

if __name__ == "__main__":
    unittest.main()
