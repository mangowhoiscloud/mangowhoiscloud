"""Check that top badges route to evidence-bearing project surfaces."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BadgeDestinationTests(unittest.TestCase):
    def test_korean_destinations(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for url in (
            "https://github.com/mangowhoiscloud/geode/releases/latest",
            "https://github.com/mangowhoiscloud/geode-eval-artifacts",
            "https://mangowhoiscloud.github.io/geode/self-improving/",
            "https://github.com/mangowhoiscloud/geode",
            "https://mangowhoiscloud.github.io/eco2/",
        ):
            self.assertIn(url, text)

    def test_english_destinations_match_korean(self):
        ko = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for url in (
            "https://github.com/mangowhoiscloud/geode/releases/latest",
            "https://github.com/mangowhoiscloud/geode-eval-artifacts",
            "https://mangowhoiscloud.github.io/geode/self-improving/",
            "https://github.com/mangowhoiscloud/geode",
            "https://mangowhoiscloud.github.io/eco2/",
        ):
            self.assertEqual(url in ko, url in en)


if __name__ == "__main__":
    unittest.main()
