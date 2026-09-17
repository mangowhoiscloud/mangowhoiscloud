from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualDocSignalTests(unittest.TestCase):
    def test_signal_rows(self):
        text = (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8")
        for row in ("| GEODE release |", "| Evidence |", "| RSI |", "| Autonomous Agents |", "| Cloud |"):
            self.assertIn(row, text)

if __name__ == "__main__":
    unittest.main()
