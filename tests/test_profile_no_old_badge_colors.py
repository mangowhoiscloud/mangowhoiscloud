from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OldBadgeColorTests(unittest.TestCase):
    def test_old_colors_absent(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for color in ("5865F2", "327A52"):
                self.assertNotIn(color, text)

if __name__ == "__main__":
    unittest.main()
