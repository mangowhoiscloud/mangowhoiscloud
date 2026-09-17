from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoActivityScoreTests(unittest.TestCase):
    def test_no_activity_score(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            self.assertNotIn("activity score", text)

if __name__ == "__main__":
    unittest.main()
