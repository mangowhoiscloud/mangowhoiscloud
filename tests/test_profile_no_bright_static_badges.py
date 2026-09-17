from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StaticBadgeNeutralTests(unittest.TestCase):
    def test_neutral_suffix(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            static = re.findall(r"https://img\.shields\.io/badge/[^\"]+", text)
            self.assertEqual(len(static), 4)
            for url in static:
                self.assertIn("-555555?style=flat-square", url)

if __name__ == "__main__":
    unittest.main()
