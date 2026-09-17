from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CloudBadgePublicTests(unittest.TestCase):
    def test_link(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('<a href="https://mangowhoiscloud.github.io/eco2/"><img src="https://img.shields.io/badge/Cloud-', text)

if __name__ == "__main__":
    unittest.main()
