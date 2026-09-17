# Profile notes · 출처, 범위, 업데이트 원칙

Reviewed: **2026-09-17**. This document supports both [한국어](../README.md) and [English](../README_EN.md).

The profile is an introduction, not a benchmark report. Published project records support the technical claims; the previous public profile supports retained career and client-delivery statements. A public statement is not the same as independently reproduced evidence.

## Source map

| Source | Used for | Boundary |
| --- | --- | --- |
| [Previous Korean profile](https://github.com/mangowhoiscloud/mangowhoiscloud/blob/fcfa534c1062c6c8a9ac7e06ebb5789c7841eb8e/README.md) / [English](https://github.com/mangowhoiscloud/mangowhoiscloud/blob/fcfa534c1062c6c8a9ac7e06ebb5789c7841eb8e/README_EN.md) | Career dates, award placement, REODE, Kiki, Cotton, Crumb, DREAM, Aimo | Public self-reported history, preserved rather than independently audited. The pre-refresh commit remains in Git history. |
| [GEODE README](https://github.com/mangowhoiscloud/geode/blob/main/README.md) | Runtime / evaluation / experimental-evolution boundaries | Current architecture and experimental status, not proof of sustained improvement. |
| [GEODE evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) | Original evidence versus derived summaries; incomplete runs; tied results | Run-local claims retain their task, model, harness, and execution conditions. |
| [Compiler AX Lab](https://github.com/mangowhoiscloud/compiler-ax-lab/blob/main/README.md) | CPU verification and A/B pilot boundaries, recorded 2026-09-16 | Independent work; no NPU, throughput, procedure-superiority, or employer-approval claim. |
| [Eco² portfolio](https://mangowhoiscloud.github.io/eco2/) / [landing repository](https://github.com/mangowhoiscloud/eco2) | Current portfolio address, service closure, 24-node cluster, API-specific load results | Virtual-user load tests, not real user counts. Separate workloads are not one combined result. |

Only previously public information is included. Client code, private repositories, protected evaluation inputs, account data, and unpublished application material are not publication sources for this refresh.

<a id="reode"></a>
## REODE: retained delivery record

Source: the previous public profile linked above. These are **March 2026 delivery records**, not a new rerun performed for the profile update.

| Item | Retained record | How to read it |
| --- | --- | --- |
| Target | 5,523 files; Java 1.8→22; Spring 4→6 | The separately listed 241 Java, 355 JSP, and 47 XML files are subsets, not an exhaustive breakdown of 5,523. |
| Verification | 83/83 tests plus frontend/backend end-to-end checks passed | No universal migration-success or all-path correctness claim. |
| Execution | 33 autonomous sessions; 1,133 rounds; 5h 48m; zero human intervention | Applies to the recorded execution, not project setup, requirements, engineering, or final acceptance. |
| Approach | OpenRewrite 70% / LLM 30%; 5-Gate Scorecard | Retained architectural description, not a newly measured automation-coverage statistic. |
| Failure recovery | Same error repeated 40 times; `explore_before_fix` introduced | A reported incident and response, not a controlled estimate of procedure effectiveness. |

The old profile also mentions Spring Boot 2→3. That label and Spring Framework 4→6 describe different version axes; the refresh does not conflate them or claim independent version verification of the private codebase.

## Eco²: preserve the achievement, separate the workloads

The award remains **2025 AI 새싹톤 우수상 / AI SeSACTHON Excellence Award (4th/181)**, as previously published. The project began with a five-person MVP and continued with solo development and operation. Its service is now marked **Closed** in the public portfolio.

| Item | Previous profile | Current presentation |
| --- | --- | --- |
| Infrastructure | 14 EC2 nodes → 24-node Kubernetes; Terraform, Ansible, ArgoCD | Keep the 24-node operated cluster; preserve the starting point here. |
| Scan load | 0→1,000 VU, 97.8% | Name the Scan API, 1,000 virtual users and 97.8%; the portfolio also reports 373 RPM. Not 1,000 real simultaneous customers. |
| Authentication | 48→1,500 RPS | Keep this historical shorthand here. The currently published ext-authz result is 1,477 RPS at 2,500 VU; do not silently equate distinct runs or use a rounded endpoint as a new measurement. |
| Quality | 69.4→99.8/100; Swiss Cheese 3-Layer | Retained historical project-evaluation figure. The task set, rubric, judge, and repeatability must accompany any renewed headline use; this is not a general model-quality score. |
| Architecture | Tool calling, LangGraph parallelism, SSE, Agent SDK | Retain the chatbot-to-workflow engineering story rather than an undated claim that the service is currently running. |

## GEODE: historical figures are not live counters

The refresh follows GEODE's current separation of runtime, evaluation, and experimental scaffold optimization. It removes the subjective four-quadrant comparison with unrelated tools; that diagram was not a benchmark.

| Historical item from the previous profile | Preserved interpretation |
| --- | --- |
| 5-tier memory; 2-phase compaction; 200K guard; zero long-session overflow | Version- and observation-bound engineering report. Not a guarantee across current models, limits, or workloads. |
| Approximately 80% multi-turn input-token reduction via prompt-cache alignment | Previous wording retained for traceability, not promoted to a current claim. Total input tokens, cached tokens, billed tokens, and price are different quantities; a reproducible baseline is needed. |
| Multi-provider gateway; 4-stage failover; 4-layer tool dispatch | Historical implementation descriptions; current details belong in the GEODE repository. |
| 408 published Petri audit logs | Earlier published snapshot. Not the current total, and not interchangeable with archive or scenario counts. |
| Crucible: 35 mutation attempts, zero core promotions | Earlier cycle result showing recorded rejection reasons, not proof of a capability gain. |

SIL evaluates safety-related behavior; Crucible experiments with capability gates. Neither repeated attempts nor a promoted configuration alone establishes sustained self-improvement. Model weights are not updated by these scaffold experiments.

The newer public evaluation repository also preserves negative results: a skill-attribution pilot's observed gain did not reproduce in its repeated diagnostic. A local comparison must not become a blanket claim that a workflow is superior.

## Compiler AX Lab: keep the units separate

The 2026-09-16 public record distinguishes these executions:

| Execution | Record | Boundary |
| --- | --- | --- |
| Double-buffering examples | 3 SDK tests; 18 input executions; 46,080 matching values; 2 helper tests; a compiled public fault failed as intended | Fixed shapes and exactly representable bf16 inputs. |
| Mapping parser | Baseline 6/6; candidate 12/12; intended fault assertion failed | ASTs and diagnostic locations. |
| Workspace integration | 720 regular tests and 55 doctests passed; 17 ignored tests excluded; 44 doctests are `compile_fail`; all-target release Clippy passed | CPU, default features; not NPU or full non-default-feature coverage. |
| Python runner | 16 regression tests passed | Demo execution and evidence handling, not compiler correctness. |
| A/B pilot | Each arm passed 3 normal controls and detected 1 qualified fault; controls tied | One pair on one task. B was selected for bounded local CPU-test adoption; human active time and procedure superiority were not established. |

The lab's repository CI is narrower than these recorded SDK experiments. A green profile badge does not run the SDK, the NPU, the private A/B pilot, or any client tests.

## Editorial decisions

**Lead with the person, then the system.** A conversational introduction and observable working habits come before technical classification. Each selected project explains what it does, what was built, and what the result supports.

**Explain the vocabulary at the point of need.** The main page briefly explains agent and harness; optional details explain Skill, regression test, ratchet, evaluation gate, and self-improvement. These are working definitions for this profile, not a universal taxonomy.

**Use badges as navigation, not decoration.** The GEODE release badge points to live release metadata. The evidence and CPU-test badges point to records. Profile CI has its own badge and is explicitly not project-performance certification. No visitor counters, contribution-score cards, tracking pixels, animated banners, or secrets are needed.

**Keep both languages aligned.** Titles, dates, results, evidence boundaries, project coverage, and destinations should change together. CI catches structural mistakes and selected fact/link drift, not translation quality or truthfulness.

### Reference profiles and documentation

[Simon Willison's profile](https://github.com/simonw/simonw) informed the direct route from current work to releases and writing. [Anthony Fu's profile](https://github.com/antfu/antfu) informed compact navigation. Their content and assets are not copied; these are design references, not endorsements or a ranked survey.

[GitHub profile README documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) defines profile publication. [Shields static-badge documentation](https://shields.io/badges/static-badge) informs badge formatting. This repository needs no separate Pages site: merging the root README into the default branch updates the profile.

## Maintenance and next improvements

**After a meaningful release or published experiment:** review both README files and the source map together. Keep volatile versions in the release badge, not a hard-coded heading. A review date changes only after an actual content review.

**Next content improvement:** publish one permission-cleared REODE case study with the problem, minimal change, checks, and acceptance scope. Do not expose client code or describe private records as publicly reproducible.

**Next navigation improvement:** curate profile pins around GEODE, Compiler AX Lab, Eco², and the evaluation-record repository. Pinning is a separate profile-setting action; this README change does not modify it.

**Optional later automation:** a small feed of releases or selected writing could be generated from public data after editorial review. Do not automatically rewrite career claims, infer achievements from commit counts, or mark content reviewed merely because a bot ran.

### Local checks and release procedure

```bash
python3 scripts/check_profile.py
python3 -m unittest discover -s tests -v
```

No additional packages or network access are needed. The checker's supported authoring subset is inline Markdown links/images, HTML links/images, and explicit HTML anchor IDs. Reference-style links are rejected rather than silently ignored.

Use a feature branch, review the diff, run profile CI, then merge the PR. After merging, verify the default-branch content and actual profile rendering, including the English switch, expanded sections, and badge destinations. Do not force-push or relax a failing check to publish.

Checks validate local targets, explicit anchors, image alt text, selected preserved facts, bilingual destination parity, and basic document structure. **They do not validate external HTTP availability, metric truth, employment history, browser layout, or the correctness of linked projects.** Those require source review and a publication check.
