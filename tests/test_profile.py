"""Positive and deliberate-fault tests for the profile checker, using no network."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from scripts.check_profile import ROOT, external_destinations, inspect, validate_page, validate_repository
from scripts.check_architecture_profile import validate_architecture


class ParserTests(unittest.TestCase):
    def test_linked_badge_keeps_image_and_destination(self):
        text = "[![Status](https://example.com/badge.svg)](https://example.com/checks)"
        self.assertEqual(external_destinations(text), {
            "https://example.com/badge.svg", "https://example.com/checks"})

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


class ArchitectureTests(unittest.TestCase):
    def test_diagram_choice_does_not_change_content_requirements(self):
        text = (ROOT / "README_EN.md").read_text()
        text = re.sub(r"```mermaid\nsequenceDiagram.*?```", "", text, flags=re.S)
        self.assertEqual(validate_architecture(text), [])

    def test_invalid_outcome_cannot_disappear(self):
        text = (ROOT / "README_EN.md").read_text().replace("INVALID", "")
        self.assertIn("missing architecture term 'INVALID'", validate_architecture(text))


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for filename in ('README.md', 'README_EN.md', 'docs/PROFILE_NOTES.md'):
            target = self.root / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / filename, target)
        shutil.copytree(ROOT / 'assets', self.root / 'assets')

    def change(self, before, after, filename='README.md'):
        path = self.root / filename
        original = path.read_text()
        self.assertIn(before, original)
        path.write_text(original.replace(before, after))

    def errors(self):
        return '\n'.join(validate_repository(self.root))

    def test_current_repository_passes(self):
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_local_file_fails(self):
        (self.root / 'docs/PROFILE_NOTES.md').unlink()
        self.assertIn('missing local target', self.errors())

    def test_broken_anchor_fails(self):
        self.change('id="how-i-work"', 'id="broken"')
        self.assertIn('missing explicit anchor', self.errors())

    def test_lost_achievement_fails(self):
        self.change('83/83', '83')
        self.assertIn('missing retained fact/project: 83/83', self.errors())

    def test_language_destination_drift_fails(self):
        self.change('https://rooftopsnow.tistory.com', 'https://example.com', 'README_EN.md')
        self.assertIn('bilingual destination mismatch', self.errors())

    def test_insecure_link_fails(self):
        self.change('https://rooftopsnow.tistory.com', 'http://rooftopsnow.tistory.com')
        self.assertIn('unsupported URL scheme', self.errors())

    def test_extra_heading_fails(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\n# Another heading\n')
        self.assertIn('level-one heading', self.errors())

    def test_repository_escape_fails(self):
        path = self.root / 'docs/PROFILE_NOTES.md'
        path.write_text(path.read_text() + '\n[Escape](../../outside.md)\n')
        self.assertIn('local link escapes repository', self.errors())

    def test_unbalanced_fence_fails(self):
        path = self.root / 'docs/PROFILE_NOTES.md'
        path.write_text(path.read_text() + '\n```text\n')
        self.assertIn('unbalanced code fences', self.errors())


if __name__ == '__main__':
    unittest.main()
