"""Keep negative and tied results visible in the public profile."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FailurePreservationTests(unittest.TestCase):
    def test_negative_results_visible(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("실패한 시도", ko)
        self.assertIn("동률", ko)
        self.assertIn("failed attempts", en)
        self.assertIn("tied", en)


if __name__ == "__main__":
    unittest.main()
