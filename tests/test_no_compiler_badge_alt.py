"""Ensure Compiler AX remains content, not a top visual badge."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoCompilerBadgeAltTests(unittest.TestCase):
    def test_no_compiler_ax_inside_badge_block(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            start = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", start)
            self.assertNotIn("Compiler AX", text[start:end])


if __name__ == "__main__":
    unittest.main()
