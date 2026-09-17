from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BadgeRowDomainTests(unittest.TestCase):
    def test_domains(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for label in ("RSI-scaffold%20search", "Autonomous%20Agents-runtime", "Cloud-Kubernetes%20%7C%20IaC"):
                self.assertEqual(text.count(label), 1, f"{filename}: {label}")

if __name__ == "__main__":
    unittest.main()
