from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Eco2ClosureTests(unittest.TestCase):
    def test_service_closed(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("서비스 운영은 종료됐고", ko)
        self.assertIn("The service has closed", en)

if __name__ == "__main__":
    unittest.main()
