"""Keep social destinations as plain links rather than colored brand imagery."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class UnderstatedSocialTests(unittest.TestCase):
    def test_no_social_logo_badges(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            for term in ("logo=youtube", "logo=linkedin", "logo=tistory"):
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
