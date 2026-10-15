# Profile notes · 출처, 범위, 편집 원칙

Reviewed: **2026.10.15**. Maintainer notes for [한국어](../README.md) and [English](../README_EN.md). Visitors do not need this page.

## Source of truth

The profile is an index to [mangowhois.ai](https://mangowhois.ai), the reviewed portfolio. Project descriptions, roles, periods, the award and the report files follow the portfolio's own data (its Korean edition is the factual source; the English edition is its translation). A claim the portfolio does not make is not added here, and a claim the portfolio no longer makes is removed.

- **Projects:** GEODE, Eco², Railshot, REODE, Kiki, Cotton and CRUMB, in the portfolio's order. Each links to its case page (`/<project>/`, English `/en/<project>/`) and to public code where a public repository exists. REODE, Kiki and Cotton have no public code.
- **Experience:** @LILT from 2026.10.16, @pinxlab 2026.03.16 – 2026.05.26, @Rakuten Symphony Korea 2024.12.09 – 2025.08.31, with the portfolio's roles. The LILT title follows the portfolio: AI Benchmark Engineer · freelance (프리랜스).
- **Reports:** the PDFs served from `tech.mangowhois.ai`, with the page counts the portfolio records.
- **Wordmark:** `https://mangowhois.ai/brand/wordmark.png`, ink on a paper plate, served by the portfolio. It appears once the portfolio deploy that adds `/brand/` is live.

## Editorial rules

- Work done for a company is written `@company`: REODE, Kiki and Cotton are pinxlab AI R&D work and carry `@pinxlab`. Do not call them “업무 프로젝트”.
- LILT: the Terminal-Bench-LILT paper (arXiv 2608.28641) predates the start of this contract. It is cited as the benchmark's paper; never state or imply that the owner wrote its tasks.
- Dates are numeric, `YYYY.MM.DD`, with an en dash for ranges. Pay and salary are never shown.
- No disclosure (details) blocks, no arrow chains, no emoji, no em dashes. Tables only where columns are real; secondary facts go in a small caption line.
- The portfolio's Kiki page links to [github.com/mangowhoiscloud#이력](https://github.com/mangowhoiscloud#이력) as a public career record, so the Korean README keeps the `## 이력` heading and names Kiki under @pinxlab.
- Both languages keep the same structure and destinations. Portfolio pages are compared without their `/en/` prefix.

## What moved in the 2026.10.15 redesign

The previous profile carried long collapsed deep dives. The portfolio now holds their reviewed successors, so the README links there instead. The previous version, with its twelve diagrams, renderer and architecture checks, remains at commit [`1661b2b`](https://github.com/mangowhoiscloud/mangowhoiscloud/tree/1661b2b1ce8e2eaa82737cb0c2c16342837aea34).

| Previous section | Now |
| --- | --- |
| GEODE runtime, meta-harness and CI, Harbor paired rollout, Experimental Loop, SIL and Crucible | [GEODE case](https://mangowhois.ai/geode/), the [GEODE repository](https://github.com/mangowhoiscloud/geode) and the GEODE reports |
| Eco² cluster, network, development, Scan, Chat, observability and improvement views | [Eco² case](https://mangowhois.ai/eco2/) and the Eco² report |
| REODE delivery record | [REODE case](https://mangowhois.ai/reode/) |
| Load figures (Scan rate at 1,000 VU, ext-authz throughput), REODE file, test and session counts, Rakuten product versions | Removed: the portfolio does not use them |
| Glossary, working method, evidence table, review-date footer, profile CI badge | Removed |
| DREAM, Aimo and the previous account link | Removed: not on the portfolio |

## Checks

```bash
python3 scripts/check_profile.py
python3 -m unittest discover -s tests -v
```

No packages or network access are needed. The checker validates structure, the retained facts and section headings, the editorial rules above, local links, image alt text and bilingual destination parity. It does not check external HTTP availability, translation quality or the truth of a claim; those need a source review against the portfolio and a look at the rendered profile after merging.
