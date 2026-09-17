"""Keep repeated measurement under comparable conditions explicit."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MeasureAgainTests(unittest.TestCase):
    def test_measure_again(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("같은 조건에서 다시 측정", ko)
        self.assertIn("measure again under comparable conditions", en)


if __name__ == "__main__":
    unittest.main()
