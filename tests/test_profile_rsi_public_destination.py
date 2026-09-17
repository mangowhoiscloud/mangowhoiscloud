from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RsiPublicDestinationTests(unittest.TestCase):
    def test_public_hub(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertGreaterEqual(text.count("https://mangowhoiscloud.github.io/geode/self-improving/"), 2)

if __name__ == "__main__":
    unittest.main()
