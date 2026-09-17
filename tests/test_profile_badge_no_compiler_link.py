from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CompilerLinkPlacementTests(unittest.TestCase):
    def test_compiler_repo_below_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            badge_end = text.index("</p>", text.index("img.shields.io/"))
            compiler = text.index("https://github.com/mangowhoiscloud/compiler-ax-lab")
            self.assertGreater(compiler, badge_end)

if __name__ == "__main__":
    unittest.main()
