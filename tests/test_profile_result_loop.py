"""Keep result reuse connected explicitly to future experiments."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResultLoopTests(unittest.TestCase):
    def test_future_experiment_language(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("다음 실험", ko)
        self.assertIn("next experiment", en)
        self.assertIn("다음 후보", ko)
        self.assertIn("next candidate", en)


if __name__ == "__main__":
    unittest.main()
