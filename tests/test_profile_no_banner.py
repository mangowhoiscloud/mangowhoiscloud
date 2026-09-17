"""Keep the profile free of decorative hero banners."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NoBannerTests(unittest.TestCase):
    def test_no_banner_asset(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8").lower()
            self.assertNotIn("banner", text)
            self.assertNotIn("header.svg", text)


if __name__ == "__main__":
    unittest.main()
