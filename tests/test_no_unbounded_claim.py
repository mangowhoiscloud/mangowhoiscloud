"""Avoid presenting open-ended search as proven perpetual improvement."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoUnboundedClaimTests(unittest.TestCase):
    def test_no_perpetual_improvement_claim(self):
        forbidden = ("끝없이 개선됩니다", "무한히 개선", "proven perpetual improvement", "improves forever")
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for phrase in forbidden:
                self.assertNotIn(phrase.lower(), text)


if __name__ == "__main__":
    unittest.main()
