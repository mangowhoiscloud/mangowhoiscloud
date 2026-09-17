"""Keep public profile prose free of exclamation-heavy presentation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoExclamationTests(unittest.TestCase):
    def test_no_exclamation_marks(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("!", text)


if __name__ == "__main__":
    unittest.main()
