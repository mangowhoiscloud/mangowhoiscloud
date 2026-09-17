from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResearchLoopLinkTests(unittest.TestCase):
    def test_two_loop_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops", text)

if __name__ == "__main__":
    unittest.main()
