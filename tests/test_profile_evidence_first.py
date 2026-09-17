"""Keep public evidence visually adjacent to the live release before categorical domains."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceFirstTests(unittest.TestCase):
    def test_evidence_precedes_domains(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            evidence = text.index("badge/Evidence-open%20records")
            self.assertLess(evidence, text.index("badge/RSI-scaffold%20search"))
            self.assertLess(evidence, text.index("badge/Autonomous%20Agents-runtime"))
            self.assertLess(evidence, text.index("badge/Cloud-Kubernetes%20%7C%20IaC"))


if __name__ == "__main__":
    unittest.main()
