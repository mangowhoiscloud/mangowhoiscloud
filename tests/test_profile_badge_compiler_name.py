from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CompilerNameBadgeTests(unittest.TestCase):
    def test_name_not_in_badge_markup(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for line in text.splitlines():
                if "img.shields.io" in line:
                    self.assertNotIn("Compiler AX", line)

if __name__ == "__main__":
    unittest.main()
