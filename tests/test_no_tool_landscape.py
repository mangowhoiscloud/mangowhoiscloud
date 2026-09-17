"""Do not reintroduce the old subjective tool quadrant into the profile."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoToolLandscapeTests(unittest.TestCase):
    def test_no_quadrant(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("Q1", text)
            self.assertNotIn("4-Quadrant", text)
            self.assertNotIn("4분면", text)


if __name__ == "__main__":
    unittest.main()
