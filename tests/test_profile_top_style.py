from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TopStyleTests(unittest.TestCase):
    def test_plain_heading(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")[:1000]
            self.assertNotIn("<h1", text)

if __name__ == "__main__":
    unittest.main()
