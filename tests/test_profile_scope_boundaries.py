"""Keep important result boundaries explicit in both languages."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ScopeBoundaryTests(unittest.TestCase):
    def test_cpu_boundary(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("CPU 값 검증은 NPU", ko)
        self.assertIn("CPU value checks do not establish NPU", en)

    def test_rsi_boundary(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("지속적인 자기개선이 입증됐다고 전제하지 않습니다", ko)
        self.assertIn("sustained self improvement has already been established", en)


if __name__ == "__main__":
    unittest.main()
