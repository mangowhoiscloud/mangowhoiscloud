"""Keep primary project and contact navigation present."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProfileLinkTests(unittest.TestCase):
    def test_primary_links(self):
        for filename in ("README.md", "README_EN.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            for url in (
                "https://mangowhoiscloud.github.io/geode/",
                "https://rooftopsnow.tistory.com",
                "https://www.youtube.com/@mango_fr",
                "https://linkedin.com/in/jihwan-ryu-b6b04a202",
            ):
                self.assertIn(url, text)


if __name__ == "__main__":
    unittest.main()
