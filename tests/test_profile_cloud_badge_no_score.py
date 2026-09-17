from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CloudBadgeNoScoreTests(unittest.TestCase):
    def test_no_numeric_cloud_badge(self):
        for filename in ("README.md", "README_EN.md"):
            lines = [line for line in (ROOT / filename).read_text(encoding="utf-8").splitlines() if "Cloud-Kubernetes" in line]
            self.assertEqual(len(lines), 1)
            self.assertNotIn("RPS", lines[0])
            self.assertNotIn("VU", lines[0])

if __name__ == "__main__":
    unittest.main()
