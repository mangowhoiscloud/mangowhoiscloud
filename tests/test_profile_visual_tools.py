"""Keep the visualization stack minimal and transparent."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualToolTests(unittest.TestCase):
    def test_only_shields_and_github_actions_images(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for line in text.splitlines():
                if "<img " in line or "![" in line:
                    self.assertTrue("img.shields.io" in line or "actions/workflows/profile.yml/badge.svg" in line, line)


if __name__ == "__main__":
    unittest.main()
