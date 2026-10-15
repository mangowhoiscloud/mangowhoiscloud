#!/usr/bin/env python3
"""Offline checks for profile structure, retained facts, and the editorial rules in docs/PROFILE_NOTES.md."""
from __future__ import annotations
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("README.md", "README_EN.md", "docs/PROFILE_NOTES.md")
# The portfolio's Kiki page links to https://github.com/mangowhoiscloud#이력, so the Korean heading is a public anchor.
HEADINGS = {
    "README.md": ("## 작업", "## 이력", "## 보고서"),
    "README_EN.md": ("## Work", "## Experience", "## Reports"),
}
RETAINED = (
    "GEODE", "Eco²", "Railshot", "REODE", "Kiki", "Cotton", "CRUMB",
    "@LILT", "@pinxlab", "@Rakuten Symphony Korea",
    "2026.10.16", "2026.03.16 – 2026.05.26", "2024.12.09 – 2025.08.31",
    "https://mangowhois.ai", "jihwan.ryu@mangowhois.ai", "https://www.linkedin.com/in/mangowhois/",
    "arXiv 2608.28641",
)
PINXLAB_WORK = ("REODE", "Kiki", "Cotton")
# Owner rules for the READMEs: no disclosure triangles, arrow chains, em dashes, emoji, pay or retired wording.
FORBIDDEN = (
    (re.compile(r"<details|<summary", re.I), "disclosure element (<details>/<summary>)"),
    (re.compile(r"[→←↔⇒➜➔]"), "arrow character"),
    (re.compile(r"—"), "em dash (use an en dash for ranges)"),
    (re.compile(r"[\U0001F000-\U0001FAFF☀-➿️]"), "emoji"),
    (re.compile(r"\$\s?\d|₩|/hr\b|/yr\b"), "pay or salary"),
    (re.compile(r"업무 프로젝트"), "retired wording '업무 프로젝트'"),
    (re.compile(r"Compiler AX|compiler-ax-lab|FuriosaAI"), "removed Compiler AX reference"),
)
# Localized portfolio pages are the same destination in both languages.
LOCALIZED = re.compile(r"^https://mangowhois\.ai/en/")

class Markup(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.errors: list[str] = []
        self.details = 0
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        anchor = values.get("id")
        if anchor:
            if anchor in self.ids:
                self.errors.append(f"duplicate anchor: {anchor}")
            self.ids.add(anchor)
        if tag in {"script", "iframe", "object"}:
            self.errors.append(f"unsupported embedded element: {tag}")
        if tag == "details":
            self.details += 1
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if tag == "img":
            if not (values.get("alt") or "").strip():
                self.errors.append("image needs descriptive alt text")
            if not values.get("src"):
                self.errors.append("image needs a source")
            else:
                self.links.append(values["src"] or "")
    def handle_endtag(self, tag: str) -> None:
        if tag == "details":
            self.details -= 1
            if self.details < 0:
                self.errors.append("closing details without an opener")

def inspect(text: str) -> Markup:
    parser = Markup()
    prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
    parser.feed(prose)
    parser.close()
    parser.links.extend(unescape(url) for url in re.findall(r"\]\(([^\s)]+)\)", prose))
    for alt in re.findall(r"!\[([^\]\n]*)\]\([^\s)]+\)", prose):
        if not alt.strip():
            parser.errors.append("Markdown image needs descriptive alt text")
    if parser.details:
        parser.errors.append("unclosed details element")
    if re.search(r"(?m)^\s*\[[^\]]+\]:|\[[^\]\n]+\]\[[^\]\n]*\]", prose):
        parser.errors.append("reference-style links are unsupported; use inline links")
    return parser

def editorial_errors(name: str, text: str) -> list[str]:
    errors = []
    for heading in HEADINGS[name]:
        if not re.search(rf"(?m)^{re.escape(heading)}\s*$", text):
            errors.append(f"missing section heading: {heading}")
    for fact in RETAINED:
        if fact not in text:
            errors.append(f"missing retained fact/project: {fact}")
    for project in PINXLAB_WORK:
        rows = [line for line in text.splitlines() if line.startswith(f"| **{project}**")]
        if not rows or not all("@pinxlab" in row for row in rows):
            errors.append(f"work row must name its company: {project} @pinxlab")
    for pattern, label in FORBIDDEN:
        if pattern.search(text):
            errors.append(f"forbidden {label}")
    return errors

def validate_page(path: Path, root: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    parsed = inspect(text)
    errors = list(parsed.errors)
    if not text.endswith("\n"):
        errors.append("missing final newline")
    if len(re.findall(r"(?m)^# ", text)) != 1:
        errors.append("expected exactly one level-one heading")
    if len(re.findall(r"(?m)^```", text)) % 2:
        errors.append("unbalanced code fences")
    if re.search(r"(?m)^(<<<<<<< |=======\s*$|>>>>>>> )", text):
        errors.append("unresolved merge conflict")
    if path.name in HEADINGS:
        errors.extend(editorial_errors(path.name, text))
        alternate = "README_EN.md" if path.name == "README.md" else "README.md"
        if alternate not in parsed.links:
            errors.append("missing language switch")
    for link in parsed.links:
        target = urlsplit(link)
        if target.scheme:
            if target.scheme not in {"https", "mailto"}:
                errors.append(f"unsupported URL scheme: {link}")
            elif target.scheme == "https" and not target.netloc:
                errors.append(f"invalid HTTPS URL: {link}")
            continue
        if target.netloc:
            errors.append(f"protocol-relative URL is unsupported: {link}")
            continue
        dest = (path.parent / unquote(target.path)).resolve() if target.path else path.resolve()
        if not dest.is_relative_to(root.resolve()):
            errors.append(f"local link escapes repository: {link}")
        elif not dest.is_file():
            errors.append(f"missing local target: {link}")
        elif target.fragment and dest.suffix == ".md":
            if unquote(target.fragment) not in inspect(dest.read_text(encoding="utf-8")).ids:
                errors.append(f"missing explicit anchor: {link}")
    return errors

def external_destinations(text: str) -> set[str]:
    return {LOCALIZED.sub("https://mangowhois.ai/", link)
            for link in inspect(text).links if urlsplit(link).scheme in {"https", "mailto"}}

def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for name in PAGES:
        path = root / name
        if not path.is_file():
            errors.append(f"missing page: {name}")
            continue
        errors.extend(f"{name}: {error}" for error in validate_page(path, root))
    ko, en = root / PAGES[0], root / PAGES[1]
    if ko.is_file() and en.is_file():
        difference = external_destinations(ko.read_text()) ^ external_destinations(en.read_text())
        errors.extend(f"bilingual destination mismatch: {link}" for link in sorted(difference))
    return errors

def main() -> int:
    errors = validate_repository(ROOT)
    if errors:
        print("Profile checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Profile checks passed: structure, retained facts, editorial rules, local links, and bilingual destinations.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
