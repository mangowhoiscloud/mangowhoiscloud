"""Keep the top of the profile free of playful greeting treatment."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoPlayfulIntroTests(unittest.TestCase):
    def test_no_greeting_emoji_or_exclamation(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")[:500]
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")[:500]
        self.assertNotIn("👋", ko + en)
        self.assertNotIn("Hi, I'm", en)


if __name__ == "__main__":
    unittest.main()
