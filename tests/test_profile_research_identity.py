"""Keep RSI, agents, and cloud as a coherent top-level identity."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResearchIdentityTests(unittest.TestCase):
    def test_identity_terms_appear_before_selected_work(self):
        for filename, marker, terms in (
            ("README.md", "## 대표 작업", ("RSI", "자율 에이전트", "클라우드")),
            ("README_EN.md", "## Selected work", ("RSI", "autonomous agent", "cloud")),
        ):
            text = (ROOT / filename).read_text(encoding="utf-8")
            prefix = text[:text.index(marker)].lower()
            for term in terms:
                self.assertIn(term.lower(), prefix)


if __name__ == "__main__":
    unittest.main()
