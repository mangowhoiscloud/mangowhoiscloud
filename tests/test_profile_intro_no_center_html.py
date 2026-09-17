from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IntroAlignmentTests(unittest.TestCase):
    def test_no_center_markup(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")[:2500]
            self.assertNotIn("align=\"center\"", text)

if __name__ == "__main__":
    unittest.main()
