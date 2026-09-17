from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoAnimatedAssetsTests(unittest.TestCase):
    def test_no_gif(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn(".gif", (ROOT / filename).read_text(encoding="utf-8").lower())

if __name__ == "__main__":
    unittest.main()
