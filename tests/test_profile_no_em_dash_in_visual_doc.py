from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VisualDocPunctuationTests(unittest.TestCase):
    def test_no_em_dash(self):
        self.assertNotIn("—", (ROOT / "docs/VISUALIZATION.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
