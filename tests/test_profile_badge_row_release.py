from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeRowReleaseTests(unittest.TestCase):
    def test_release(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("github/v/release/mangowhoiscloud/geode"), 1)

if __name__ == "__main__":
    unittest.main()
