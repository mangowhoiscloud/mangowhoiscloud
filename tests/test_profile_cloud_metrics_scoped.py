from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CloudMetricScopeTests(unittest.TestCase):
    def test_load_scope(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("별도의 ext-authz 인증 경로", ko)
        self.assertIn("separate ext authz path", en)
        self.assertIn("실제 이용자 수가 아닙니다", ko)
        self.assertIn("not actual users", en)

if __name__ == "__main__":
    unittest.main()
