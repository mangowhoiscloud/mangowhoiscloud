from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoLogoWallTests(unittest.TestCase):
    def test_no_skill_icon_wall(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("skillicons.dev", "simple-icons", "techstack-generator"):
                self.assertNotIn(term, text)

if __name__ == "__main__":
    unittest.main()
