"""Keep public evaluation records reachable from both profile languages."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceDestinationTests(unittest.TestCase):
    def test_evidence_repo(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertGreaterEqual(text.count("https://github.com/mangowhoiscloud/geode-eval-artifacts"), 2)


if __name__ == "__main__":
    unittest.main()
