from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NeutralBadgeTests(unittest.TestCase):
    def test_static_badges_neutral(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for old_color in ("5865F2", "327A52", "FF0000", "0A66C2", "FF5722"):
                self.assertNotIn(old_color, text)

if __name__ == "__main__":
    unittest.main()
