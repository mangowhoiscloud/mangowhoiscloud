"""Keep badges limited to selected operational signals."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeWallTests(unittest.TestCase):
    def test_no_social_follow_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("github/followers", text)
            self.assertNotIn("visitor", text.lower())


if __name__ == "__main__":
    unittest.main()
