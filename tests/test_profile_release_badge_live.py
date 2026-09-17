from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReleaseBadgeLiveTests(unittest.TestCase):
    def test_dynamic_release_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("https://img.shields.io/github/v/release/mangowhoiscloud/geode", text)
            self.assertNotIn("badge/GEODE-v1", text)

if __name__ == "__main__":
    unittest.main()
