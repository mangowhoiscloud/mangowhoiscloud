# Profile notes · 출처, 범위, 업데이트 원칙

Reviewed: **2026-09-18**. This document supports both [한국어](../README.md) and [English](../README_EN.md).

The profile is an introduction, not a benchmark report. Published project records support the technical claims; the previous public profile supports retained career and client-delivery statements. A public statement is not the same as independently reproduced evidence.

## Source map

| Source | Used for | Boundary |
| --- | --- | --- |
| [Previous Korean profile](https://github.com/mangowhoiscloud/mangowhoiscloud/blob/fcfa534c1062c6c8a9ac7e06ebb5789c7841eb8e/README.md) / [English](https://github.com/mangowhoiscloud/mangowhoiscloud/blob/fcfa534c1062c6c8a9ac7e06ebb5789c7841eb8e/README_EN.md) | Career dates, award placement, REODE, Kiki, Cotton, Crumb, DREAM, Aimo | Public self-reported history, preserved rather than independently audited. The pre-refresh commit remains in Git history. |
| [GEODE README](https://github.com/mangowhoiscloud/geode/blob/main/README.md) | Runtime / evaluation / experimental-evolution boundaries | Current architecture and experimental status, not proof of sustained improvement. |
| [GEODE evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) | Original evidence versus derived summaries; incomplete runs; tied results | Run-local claims retain their task, model, harness, and execution conditions. |
| [Terminal-Bench contract at reviewed GEODE revision](https://github.com/mangowhoiscloud/geode/blob/fd53e0b9c95c1179f8f36ee91a5d3f0b15674af5/docs/eval/terminal-bench-2.md) / [public run at reviewed artifact revision](https://github.com/mangowhoiscloud/geode-eval-artifacts/tree/d277607f3a179f191ad24b1497c0934beb9d2470/terminal-bench/terminalbench21-sol-max-fullsuite-paired-20260827t190300z) | Harbor ownership, paired rollouts, file roles, secondary counts, and replay provenance | Historical one-tool GEODE adapter; 890 planned cells, not 890 valid trials or complete traces. Later full-runtime and Astra runs are separate. |
| [Compiler AX Lab](https://github.com/mangowhoiscloud/compiler-ax-lab/blob/main/README.md) | CPU verification and A/B pilot boundaries, recorded 2026-09-16 | Independent work; no NPU, throughput, procedure-superiority, or employer-approval claim. |
| [Eco² portfolio](https://mangowhoiscloud.github.io/eco2/) / [backend repository](https://github.com/eco2-team/backend) | Portfolio address, service closure, task/event architecture, API-specific load results | Public project reports, not new measurements. Workload denominators and infrastructure snapshots need separate reconciliation, as noted below. |
| [Profile before this revision](https://github.com/mangowhoiscloud/mangowhoiscloud/blob/55bfad72981afb86bb9ecfc693f3afc12601b07c/README.md) | Latest published narrative, architecture descriptions, and metric discrepancies | This refresh changes presentation; it does not rerun experiments or resolve conflicting historical records. |

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

<a id="eco2"></a>
## Eco²: preserve the achievement, separate the workloads

The award remains **2025 AI 새싹톤 우수상 / AI SeSACTHON Excellence Award (4th/181)**, as previously published. The project began with a five-person MVP and continued with solo development and operation. Its service is now marked **Closed** in the public portfolio.

| Item | Previous profile | Current presentation |
| --- | --- | --- |
| Infrastructure | Earlier notes and the backend README describe 24 nodes; the 2026-09-18 profile describes 20 EC2 instances. | These snapshots are not reconciled. Omit the node count from the profile rather than choose one as verified current infrastructure. Terraform, Ansible, Kubernetes, and ArgoCD remain supported architecture descriptions. |
| Scan load | The backend README reports 97.8% at 1,000 VU; the latest profile also pairs 1,469/1,518 completed tasks with 97.8%. | 1,469 ÷ 1,518 = 96.77%, not 97.8%. Retain 97.8% only as a public project-reported rate, without the incompatible fraction. The original load-test receipt and its success definition are needed to reconcile the figures. |
| Authentication | 48→1,500 RPS | Keep this historical shorthand here. The currently published ext-authz result is 1,477 RPS at 2,500 VU; do not silently equate distinct runs or use a rounded endpoint as a new measurement. |
| Quality | 69.4→99.8/100; Swiss Cheese 3-Layer | Retained historical project-evaluation figure. The task set, rubric, judge, and repeatability must accompany any renewed headline use; this is not a general model-quality score. |
| Architecture | Tool calling, LangGraph parallelism, SSE, Agent SDK | Retain the chatbot-to-workflow engineering story rather than an undated claim that the service is currently running. |

The Scan percentage and ext-authz throughput belong to separate load tests. Neither is a count of real simultaneous users, and this profile revision does not independently reproduce either test.

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

### Harbor: paired execution, not shadow traffic

The reviewed run is `terminalbench21-sol-max-fullsuite-paired-20260827t190300z`. Its frozen plan is 89 tasks × 5 repetitions × 2 arms, using OpenAI subscription `gpt-5.6-sol` with requested effort `max`. Pairing aligns task and repetition, not random seeds or execution time. Harbor provides no shared seed control in this protocol. The diagram shows independent trial environments and evidence routes, not concurrent scheduling or every internal stage.

The historical GEODE adapter used `AgenticLoop` with one Harbor-backed `terminal_exec` tool. The later `GeodeRuntimeHarborAgent` treatment is not the implementation measured by these historical counts. The task verifier and frozen selection rules own scores; the internal runtime's Verify/Reflexion and the replay do not replace that authority.

The full-suite primary remains **not measurable**: `bn-fit-modify` and `tune-mjcf` were symmetrically excluded before model execution because their amd64 oracle/verifier paths did not complete normally under the arm64/Rosetta host (20 planned cells), and six native cells remained infrastructure-invalid. The common-valid secondary is **339/429 GEODE versus 331/429 native Codex**. Do not turn this incomplete population into a full-suite rank or a causal estimate of later runtime changes.

The public file table describes normalized derivatives, not a second raw store. A trajectory can carry source digests without publishing full action bodies. ATIF-derived casts remain derived replay; observer PTY captures remain procedural evidence. Neither proves complete historical behavior coverage. New runs retain new identities and do not fill old evidence retroactively. The Astra 1-task smoke is listed only as a separate integration check.

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

**Lead with current work and its evidence.** A short introduction leads directly to selected projects. Evolution and working methods follow the concrete systems rather than delaying them. Each project names the problem, design choice, and evidence boundary.

**Choose diagrams by the question they answer.** Per language, nine sequence diagrams become five diagrams: a GEODE boundary/architecture view, one runtime request/response sequence, a Harbor paired-rollout/evidence flow, an Eco² task/event topology, and a branching experiment decision flow. Project evolution, workload differences, operational ownership, and evidence provenance use tables. No minimum diagram count or sequence-diagram quota belongs in CI.

**Use progressive disclosure.** The GEODE overview and Harbor comparison stay visible. Runtime detail, the evaluation file map and measurement repairs, Eco² infrastructure, experiment gates, historical failure analysis, glossary, and secondary projects can be expanded. Native Markdown, Mermaid, and GitHub's own typography keep the page maintainable and theme-aware; no separate frontend is needed.

**Explain vocabulary at the point of need.** The main text defines meta-harness when introducing the build boundary. Optional definitions distinguish agent, harness, meta-harness, and RSI. These are working definitions for this profile, not a universal taxonomy.

**Use badges as navigation, not decoration.** One GEODE release badge points to live release metadata. Profile CI has its own footer badge and is explicitly not project-performance certification. Evidence links stay beside their claims. No visitor counters, contribution-score cards, tracking pixels, animated banners, or secrets are needed.

**Keep both languages aligned.** Titles, dates, results, evidence boundaries, project coverage, and destinations should change together. CI catches structural mistakes and selected fact/link drift, not translation quality or truthfulness.

### Reference profiles and documentation

[Simon Willison's profile](https://github.com/simonw/simonw) informed the direct route from current work to releases and writing. [Anthony Fu's profile](https://github.com/antfu/antfu) informed compact navigation. Their content and assets are not copied; these are design references, not endorsements or a ranked survey.

[GitHub profile README documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) defines profile publication. [Shields static-badge documentation](https://shields.io/badges/static-badge) informs badge formatting. This repository needs no separate Pages site: merging the root README into the default branch updates the profile.

[GitHub diagram documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) and the [Mermaid flowchart reference](https://mermaid.js.org/syntax/flowchart.html) support the native diagram choices. Local rendering checks syntax and legibility; GitHub's deployed Mermaid version and theme still require a post-publication check.

## Maintenance and next improvements

**After a meaningful release or published experiment:** review both README files and the source map together. Keep volatile versions in the release badge, not a hard-coded heading. A review date changes only after an actual content review.

**Next content improvement:** publish one permission-cleared REODE case study with the problem, minimal change, checks, and acceptance scope. Do not expose client code or describe private records as publicly reproducible.

**Next navigation improvement:** curate profile pins around GEODE, Compiler AX Lab, Eco², and the evaluation-record repository. Pinning is a separate profile-setting action; this README change does not modify it.

**Optional later automation:** a small feed of releases or selected writing could be generated from public data after editorial review. Do not automatically rewrite career claims, infer achievements from commit counts, or mark content reviewed merely because a bot ran.

### Local checks and release procedure

```bash
python3 scripts/check_profile.py
python3 scripts/check_architecture_profile.py
python3 -m unittest discover -s tests -v
```

No additional packages or network access are needed. The checker's supported authoring subset is inline Markdown links/images, HTML links/images, and explicit HTML anchor IDs. Reference-style links are rejected rather than silently ignored.

Use a feature branch, review the diff, run profile CI, then merge the PR. After merging, verify the default-branch content and actual profile rendering, including the English switch, expanded sections, and badge destinations. Do not force-push or relax a failing check to publish.

Checks validate local targets, explicit anchors, image alt text, selected preserved facts, bilingual destination parity, and basic document structure. **They do not validate external HTTP availability, metric truth, employment history, browser layout, or the correctness of linked projects.** Those require source review and a publication check.
