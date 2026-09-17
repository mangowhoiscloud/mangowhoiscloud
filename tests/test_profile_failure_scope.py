"""Keep failure records visible as part of the evidence loop."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FailureScopeTests(unittest.TestCase):
    def test_failure_recording(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("실패와 미완료 호출도 기록", ko)
        self.assertIn("failures and incomplete calls remain visible", en)


if __name__ == "__main__":
    unittest.main()
