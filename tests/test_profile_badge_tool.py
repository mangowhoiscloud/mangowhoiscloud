from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeToolTests(unittest.TestCase):
    def test_shields(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertEqual((ROOT / filename).read_text(encoding="utf-8").count("https://img.shields.io/"), 5)

if __name__ == "__main__":
    unittest.main()
