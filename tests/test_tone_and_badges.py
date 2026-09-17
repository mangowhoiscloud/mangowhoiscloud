"""Regression checks for profile tone, RSI framing, and top badge choices."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ToneAndBadgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ko = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "README_EN.md").read_text(encoding="utf-8")

    def test_compiler_ax_is_not_a_badge(self):
        for text in (self.ko, self.en):
            self.assertNotIn("img.shields.io/badge/Compiler%20AX", text)

    def test_compiler_ax_project_is_preserved(self):
        for text in (self.ko, self.en):
            self.assertIn("### Compiler AX Lab", text)

    def test_domain_badges_are_present(self):
        for text in (self.ko, self.en):
            self.assertIn("img.shields.io/badge/RSI-scaffold%20search", text)
            self.assertIn("img.shields.io/badge/Autonomous%20Agents-runtime", text)
            self.assertIn("img.shields.io/badge/Cloud-Kubernetes%20%7C%20IaC", text)

    def test_search_space_principle_is_explicit(self):
        self.assertIn("탐색 공간은 닫지 않습니다", self.ko)
        self.assertIn("without closing the search space", self.en)

    def test_results_feed_next_search(self):
        self.assertIn("결과를 다음 탐색의 데이터로 남깁니다", self.ko)
        self.assertIn("Preserve results as data for the next search", self.en)

    def test_no_heading_emoji(self):
        for text in (self.ko, self.en):
            for line in text.splitlines():
                if line.startswith("#"):
                    self.assertNotRegex(line, r"[👋🪨🔬🛠️🌱]")


if __name__ == "__main__":
    unittest.main()
