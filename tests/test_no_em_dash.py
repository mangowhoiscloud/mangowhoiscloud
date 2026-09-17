"""Keep the public profile free of em dash punctuation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoEmDashTests(unittest.TestCase):
    def test_public_profile_has_no_em_dash(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("—", text, filename)


if __name__ == "__main__":
    unittest.main()
