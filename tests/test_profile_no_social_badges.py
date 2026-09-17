"""Keep social navigation textual instead of adding colorful social badges."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoSocialBadgesTests(unittest.TestCase):
    def test_no_social_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for badge in ("badge/YouTube", "badge/LinkedIn", "badge/Blog"):
                self.assertNotIn(badge, text)


if __name__ == "__main__":
    unittest.main()
