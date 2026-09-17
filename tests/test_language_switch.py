"""Keep both profile language switches explicit."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LanguageSwitchTests(unittest.TestCase):
    def test_switches(self):
        self.assertIn('href="README_EN.md"', (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn('href="README.md"', (ROOT / "README_EN.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
