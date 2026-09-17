"""Keep the live GEODE release badge as operational metadata."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseBadgeTests(unittest.TestCase):
    def test_release_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("img.shields.io/github/v/release/mangowhoiscloud/geode", text)
            self.assertIn("https://github.com/mangowhoiscloud/geode/releases/latest", text)


if __name__ == "__main__":
    unittest.main()
