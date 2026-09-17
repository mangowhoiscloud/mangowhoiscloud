from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IntroCloudHistoryTests(unittest.TestCase):
    def test_cloud_background(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")[:1000]
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")[:1000]
        self.assertIn("분산 스토리지와 백엔드, 클라우드 인프라", ko)
        self.assertIn("distributed storage, backend engineering, and cloud infrastructure", en)

if __name__ == "__main__":
    unittest.main()
