# Profile visualization choices

Reviewed: 2026-09-17.

The profile uses a restrained set of Shields.io badges as navigation rather than a decorative developer dashboard.

## Current signals

| Signal | Destination | Reason |
| --- | --- | --- |
| GEODE release | GEODE latest release | Live project version is useful operational metadata and does not require hard coding a version into prose. |
| Evidence | GEODE evaluation artifacts | The profile emphasizes evidence preservation and reuse, so the badge routes directly to public records. |
| RSI | GEODE self improving hub | Signals the current research direction. The label says scaffold search to distinguish the work from model weight training. |
| Autonomous Agents | GEODE repository | Signals the primary runtime domain without inventing an autonomy score. |
| Cloud | Eco² technical portfolio | Connects Kubernetes and IaC experience to a public architecture and load testing record. |

Compiler AX Lab remains a selected project in the README but deliberately has no top badge.

## Why not common profile metrics

Contribution streaks, total commits, language percentages, visitor counters, star totals, and generic profile scores are intentionally omitted. They are easy to display but weak proxies for the work described here. Language share in particular is heavily affected by generated, vendored, experimental, and documentation files.

The profile favors operational or evidence bearing signals that map to the work itself: release state, public evaluation records, RSI scaffold search, autonomous agent runtime, and cloud infrastructure.

## Tools

[Shields.io](https://shields.io/) provides the compact badges. GitHub Actions provides the profile content check badge at the bottom of the README. No third party contribution analytics, tracking pixels, visitor counters, or opaque score services are required.

If a new metric is added later, it should satisfy three conditions:

1. It has a stable and inspectable source.
2. Its unit and scope are understandable without implying a broader result.
3. It helps a reader understand RSI, autonomous agents, cloud systems, or evidence driven engineering better than a static label would.
