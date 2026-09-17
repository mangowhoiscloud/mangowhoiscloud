from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EmDashTests(unittest.TestCase):
    def test_no_em_dash(self):
        for filename in ("README.md", "README_EN.md"):
            self.assertNotIn("\u2014", (ROOT / filename).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
