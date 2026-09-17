"""Keep the working-style section descriptive rather than slogan-heavy."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoSloganBlockquoteTests(unittest.TestCase):
    def test_no_blockquote(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertFalse(any(line.startswith("> ") for line in text.splitlines()))


if __name__ == "__main__":
    unittest.main()
