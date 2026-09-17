from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AgentPublicDestinationTests(unittest.TestCase):
    def test_public_repo(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertGreaterEqual(text.count("https://github.com/mangowhoiscloud/geode"), 3)

if __name__ == "__main__":
    unittest.main()
