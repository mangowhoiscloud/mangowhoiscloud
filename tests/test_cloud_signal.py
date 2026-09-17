"""Keep cloud work grounded in concrete infrastructure terms."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudSignalTests(unittest.TestCase):
    def test_cloud_terms(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for term in ("Kubernetes", "Terraform", "Ansible", "ArgoCD", "24"):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
