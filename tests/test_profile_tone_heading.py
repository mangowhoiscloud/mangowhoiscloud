from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NameHeadingTests(unittest.TestCase):
    def test_exact_heading(self):
        self.assertEqual(next(line for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines() if line.startswith("# ")), "# 류지환")
        self.assertEqual(next(line for line in (ROOT / "README_EN.md").read_text(encoding="utf-8").splitlines() if line.startswith("# ")), "# Jihwan Ryu")

if __name__ == "__main__":
    unittest.main()
