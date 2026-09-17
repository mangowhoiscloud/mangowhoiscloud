"""Keep section labels concise and professional."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SectionTitleTests(unittest.TestCase):
    def test_korean_titles(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for heading in ("## 작업 방식", "## 대표 작업", "## 개념", "## 이력", "## 기록"):
            self.assertIn(heading, text)

    def test_english_titles(self):
        text = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for heading in ("## How I work", "## Selected work", "## Concepts", "## Experience", "## Notes"):
            self.assertIn(heading, text)


if __name__ == "__main__":
    unittest.main()
