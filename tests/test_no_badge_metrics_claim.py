"""Keep domain badges categorical rather than fabricated numeric metrics."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeMetricClaimTests(unittest.TestCase):
    def test_static_domain_badges_have_no_percent_scores(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            static_badges = re.findall(r"img\.shields\.io/badge/[^\"']+", text)
            for badge in static_badges:
                self.assertNotIn("%25", badge)


if __name__ == "__main__":
    unittest.main()
