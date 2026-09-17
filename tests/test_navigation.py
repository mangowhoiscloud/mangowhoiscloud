"""Keep the top navigation aligned to the restrained section names."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NavigationTests(unittest.TestCase):
    def test_korean_nav(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[작업 방식](#how-i-work) · [대표 작업](#selected-work) · [개념](#concepts) · [이력](#experience) · [기록](#more)", text)

    def test_english_nav(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("[How I work](#how-i-work) · [Selected work](#selected-work) · [Concepts](#concepts) · [Experience](#experience) · [Notes](#more)", text)


if __name__ == "__main__":
    unittest.main()
