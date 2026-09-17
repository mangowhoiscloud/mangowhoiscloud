"""Keep the compact loop visibly feeding back into the next search."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FeedbackArrowTests(unittest.TestCase):
    def test_feedback_arrow(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("└", text)
            self.assertIn("←", text)


if __name__ == "__main__":
    unittest.main()
