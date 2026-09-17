"""Keep model-weight training separate from GEODE scaffold experiments."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoWeightsClaimTests(unittest.TestCase):
    def test_weight_boundary(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("모델 가중치가 아니라", ko)
        self.assertIn("rather than model weights", en)


if __name__ == "__main__":
    unittest.main()
