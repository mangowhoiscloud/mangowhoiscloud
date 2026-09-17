"""Keep the cloud badge scoped to concrete technologies rather than a proficiency score."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudBadgeScopeTests(unittest.TestCase):
    def test_cloud_badge_scope(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("Cloud-Kubernetes%20%7C%20IaC", text)
            self.assertNotIn("Cloud-expert", text)
            self.assertNotIn("Cloud-senior", text)


if __name__ == "__main__":
    unittest.main()
