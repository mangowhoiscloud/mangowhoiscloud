"""Keep execution, evaluation, and experimental search separated in GEODE."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GeodeBoundaryTests(unittest.TestCase):
    def test_boundaries(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for boundary in ("`core`", "`evals`", "`evolve`"):
                self.assertIn(boundary, text)


if __name__ == "__main__":
    unittest.main()
