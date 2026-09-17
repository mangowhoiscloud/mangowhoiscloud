from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IacTests(unittest.TestCase):
    def test_iac(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("Terraform", text)
            self.assertIn("Ansible", text)
            self.assertIn("ArgoCD", text)
            self.assertIn("IaC", text)

if __name__ == "__main__":
    unittest.main()
