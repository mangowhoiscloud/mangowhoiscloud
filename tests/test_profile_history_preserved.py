"""Keep the requested career and project history while changing presentation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HistoryPreservedTests(unittest.TestCase):
    def test_history_names(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for name in ("Rakuten Symphony Korea", "pinxlab", "Kiki", "Cotton", "Crumb", "DREAM", "Aimo", "mng990"):
                self.assertIn(name, text, f"{filename}: {name}")


if __name__ == "__main__":
    unittest.main()
