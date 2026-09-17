"""Keep the profile free of the earlier playful rhetorical style."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CalmCopyTests(unittest.TestCase):
    def test_no_rhetorical_questions(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("?", text)
            self.assertNotIn("？", text)


if __name__ == "__main__":
    unittest.main()
