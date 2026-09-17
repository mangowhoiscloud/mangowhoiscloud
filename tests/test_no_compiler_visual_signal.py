"""Keep Compiler AX in substantive content but out of the top visual signals."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoCompilerVisualSignalTests(unittest.TestCase):
    def test_no_compiler_in_top_block(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            start = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", start)
            self.assertNotIn("compiler-ax-lab", text[start:end].lower())


if __name__ == "__main__":
    unittest.main()
