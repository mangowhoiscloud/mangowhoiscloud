"""Keep static domain badges in one restrained neutral treatment."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeColorTests(unittest.TestCase):
    def test_neutral_domain_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count("-555555?style=flat-square"), 4, filename)


if __name__ == "__main__":
    unittest.main()
