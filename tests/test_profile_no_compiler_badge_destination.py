from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoCompilerBadgeDestinationTests(unittest.TestCase):
    def test_destination_not_top(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            start = text.index("<p>\n  <a href=\"https://github.com/mangowhoiscloud/geode/releases/latest\"")
            end = text.index("</p>", start)
            self.assertNotIn("https://github.com/mangowhoiscloud/compiler-ax-lab", text[start:end])

if __name__ == "__main__":
    unittest.main()
