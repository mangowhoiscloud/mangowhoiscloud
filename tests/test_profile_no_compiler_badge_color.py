from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CompilerBadgeColorTests(unittest.TestCase):
    def test_old_color_absent(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn("327A52", (ROOT / filename).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
