from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BangTests(unittest.TestCase):
    def test_no_bang(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn("!", (ROOT / filename).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
