"""Positive and deliberate-fault tests for the profile checker, using no network."""
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.check_profile import ROOT, external_destinations, inspect, validate_repository


class ParserTests(unittest.TestCase):
    def test_linked_badge_keeps_image_and_destination(self):
        text = "[![Status](https://example.com/badge.svg)](https://example.com/checks)"
        self.assertEqual(external_destinations(text), {
            "https://example.com/badge.svg", "https://example.com/checks"})

    def test_localized_portfolio_pages_share_a_destination(self):
        self.assertEqual(external_destinations("[Case](https://mangowhois.ai/en/geode/)"),
                         external_destinations("[사례](https://mangowhois.ai/geode/)"))

    def test_html_entities_are_decoded(self):
        self.assertIn("https://example.com/?a=1&b=2",
                      inspect('<a href="https://example.com/?a=1&amp;b=2">x</a>').links)

    def test_html_image_requires_alt(self):
        self.assertTrue(inspect('<img src="https://example.com/image.svg">').errors)

    def test_markdown_image_requires_alt(self):
        self.assertTrue(inspect('![](https://example.com/image.svg)').errors)

    def test_details_must_close(self):
        self.assertTrue(inspect('<details><summary>More</summary>').errors)

    def test_details_cannot_close_before_open(self):
        self.assertTrue(inspect('</details><details>').errors)

    def test_duplicate_anchors_fail(self):
        self.assertTrue(inspect('<a id="a"></a><a id="a"></a>').errors)

    def test_reference_links_fail(self):
        self.assertTrue(inspect('[Read][ref]\n\n[ref]: https://example.com').errors)

    def test_code_example_is_not_a_live_link(self):
        self.assertFalse(inspect('```text\n[x](missing.md)\n```\n').links)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for filename in ('README.md', 'README_EN.md', 'docs/PROFILE_NOTES.md'):
            target = self.root / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / filename, target)

    def change(self, before, after, filename='README.md'):
        path = self.root / filename
        original = path.read_text()
        self.assertIn(before, original)
        path.write_text(original.replace(before, after))

    def append(self, text, filename='README.md'):
        path = self.root / filename
        path.write_text(path.read_text() + text)

    def errors(self):
        return '\n'.join(validate_repository(self.root))

    def test_current_repository_passes(self):
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_notes_fail(self):
        (self.root / 'docs/PROFILE_NOTES.md').unlink()
        self.assertIn('missing page: docs/PROFILE_NOTES.md', self.errors())

    def test_public_experience_anchor_is_kept(self):
        self.change('## 이력', '## 경력')
        self.assertIn('missing section heading: ## 이력', self.errors())

    def test_lost_experience_fails(self):
        self.change('**@LILT**', '**LILT**', 'README_EN.md')
        self.assertIn('README_EN.md: missing retained fact/project: @LILT', self.errors())

    def test_company_work_names_its_company(self):
        self.change('**Kiki**<br>@pinxlab', '**Kiki**')
        self.assertIn('work row must name its company: Kiki @pinxlab', self.errors())

    def test_disclosure_fails(self):
        self.append('\n<details><summary>More</summary>\n\nText\n\n</details>\n')
        self.assertIn('forbidden disclosure element', self.errors())

    def test_arrow_chain_fails(self):
        self.append('\nPlan → build → verify\n', 'README_EN.md')
        self.assertIn('forbidden arrow character', self.errors())

    def test_em_dash_fails(self):
        self.change('2026.03.16 – 2026.05.26', '2026.03.16 — 2026.05.26')
        self.assertIn('forbidden em dash', self.errors())

    def test_pay_fails(self):
        self.append('\nRemote · $55/hr\n', 'README_EN.md')
        self.assertIn('forbidden pay or salary', self.errors())

    def test_language_destination_drift_fails(self):
        self.change('https://rooftopsnow.tistory.com', 'https://example.com', 'README_EN.md')
        self.assertIn('bilingual destination mismatch', self.errors())

    def test_localized_case_drift_fails(self):
        self.change('https://mangowhois.ai/en/kiki/', 'https://mangowhois.ai/en/cotton/', 'README_EN.md')
        self.assertIn('bilingual destination mismatch: https://mangowhois.ai/kiki/', self.errors())

    def test_insecure_link_fails(self):
        self.change('https://rooftopsnow.tistory.com', 'http://rooftopsnow.tistory.com')
        self.assertIn('unsupported URL scheme', self.errors())

    def test_extra_heading_fails(self):
        self.append('\n# Another heading\n')
        self.assertIn('level-one heading', self.errors())

    def test_repository_escape_fails(self):
        self.append('\n[Escape](../../outside.md)\n', 'docs/PROFILE_NOTES.md')
        self.assertIn('local link escapes repository', self.errors())

    def test_unbalanced_fence_fails(self):
        self.append('\n```text\n', 'docs/PROFILE_NOTES.md')
        self.assertIn('unbalanced code fences', self.errors())


if __name__ == '__main__':
    unittest.main()
