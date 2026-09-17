from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeIconTests(unittest.TestCase):
    def test_static_badges_no_logos(self):
        for filename in ("README.md", "README_EN.md"):
            for line in (ROOT / filename).read_text(encoding="utf-8").splitlines():
                if "img.shields.io/badge/" in line:
                    self.assertNotIn("logo=", line)

if __name__ == "__main__":
    unittest.main()
