from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoTrainingBadgeTests(unittest.TestCase):
    def test_no_training_badge(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("badge/training", "badge/fine--tuning", "badge/weight%20training"):
                self.assertNotIn(term, text)

if __name__ == "__main__":
    unittest.main()
