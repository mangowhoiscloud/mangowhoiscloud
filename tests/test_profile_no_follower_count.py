from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoFollowerCountTests(unittest.TestCase):
    def test_no_followers(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn("github/followers", (ROOT / filename).read_text(encoding="utf-8").lower())

if __name__ == "__main__":
    unittest.main()
