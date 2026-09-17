"""Keep project headings text-only."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectHeadingTests(unittest.TestCase):
    def test_project_headings(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for heading in ("### GEODE", "### Compiler AX Lab", "### REODE @ pinxlab", "### Eco²"):
                self.assertIn(heading, text)


if __name__ == "__main__":
    unittest.main()
