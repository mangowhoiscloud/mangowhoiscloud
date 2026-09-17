"""Keep GEODE first among selected work as the current primary project."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SelectedWorkOrderTests(unittest.TestCase):
    def test_geode_before_other_projects(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertLess(text.index("### GEODE"), text.index("### Compiler AX Lab"))
            self.assertLess(text.index("### GEODE"), text.index("### REODE @ pinxlab"))
            self.assertLess(text.index("### GEODE"), text.index("### Eco²"))


if __name__ == "__main__":
    unittest.main()
