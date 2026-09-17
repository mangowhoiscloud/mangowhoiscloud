"""Keep the profile focused on owned work rather than ranking external tools."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoComparisonRankTests(unittest.TestCase):
    def test_no_old_landscape_tools(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for term in ("Devin", "Manus", "OpenHands", "Cursor", "Copilot"):
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
