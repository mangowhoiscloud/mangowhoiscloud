from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SelectedProjectLinkTests(unittest.TestCase):
    def test_links(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for url in ("https://github.com/mangowhoiscloud/geode", "https://github.com/mangowhoiscloud/compiler-ax-lab", "https://mangowhoiscloud.github.io/eco2/"):
                self.assertIn(url, text)

if __name__ == "__main__":
    unittest.main()
