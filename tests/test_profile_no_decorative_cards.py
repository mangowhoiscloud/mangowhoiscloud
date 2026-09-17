from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoDecorativeCardTests(unittest.TestCase):
    def test_no_external_card_images(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("vercel.app/api", "activity-graph", "readme-stats", "trophy"):
                self.assertNotIn(term, text)

if __name__ == "__main__":
    unittest.main()
