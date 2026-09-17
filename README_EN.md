<p align="right"><a href="README.md">한국어</a> · <strong>English</strong></p>

# Jihwan Ryu

**I build verifiable systems, then feed their results back into the next search.**

My background spans distributed storage, backend engineering, and cloud infrastructure. Today I work on **autonomous agent runtimes and RSI (Recursive Self-Improvement) methodology**. I care less about a model succeeding once than about whether the execution is observable and reproducible, and whether its results remain useful as material for the next experiment.

Each execution is bounded by explicit scope and verification conditions. The search space is not. Rather than treating the prompt as the only variable, I explore task decomposition, context construction, tool policy, Skills, evaluation methods, agent roles, and points of human intervention as parts of the methodology itself.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [Technical blog](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

<p>
  <a href="https://github.com/mangowhoiscloud/geode/releases/latest"><img src="https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&amp;label=GEODE" alt="Latest GEODE release"></a>
  <a href="https://github.com/mangowhoiscloud/geode-eval-artifacts"><img src="https://img.shields.io/badge/Evidence-open%20records-555555?style=flat-square" alt="Public evaluation records"></a>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/RSI-scaffold%20search-555555?style=flat-square" alt="RSI scaffold search"></a>
  <a href="https://github.com/mangowhoiscloud/geode"><img src="https://img.shields.io/badge/Autonomous%20Agents-runtime-555555?style=flat-square" alt="Autonomous agent runtime"></a>
  <a href="https://mangowhoiscloud.github.io/eco2/"><img src="https://img.shields.io/badge/Cloud-Kubernetes%20%7C%20IaC-555555?style=flat-square" alt="Kubernetes and IaC cloud engineering"></a>
</p>

[How I work](#how-i-work) · [Selected work](#selected-work) · [Concepts](#concepts) · [Experience](#experience) · [Notes](#more)

<a id="how-i-work"></a>
## How I work

**Bound the problem and verification surface first.** Before editing a large codebase, I find the failing input and the actual call path. I define what may change, what must remain intact, and the smallest check that reproduces the problem.

**Use models for exploration and evidence for decisions.** I use AI actively to form hypotheses and navigate unfamiliar code, but a change is established by commands, test results, and original logs. Weakening a test to obtain a passing build is not a solution.

**Preserve results as data for the next search.** Successful changes are useful, but so are failed attempts, rejected hypotheses, execution trajectories, and evaluation results. A discovered cause becomes a regression test; a repeatable investigation becomes a concise guide or Skill. These records inform the next candidate and the shape of the search space.

**Treat methodology itself as a search space.** Task decomposition, context, tool selection, verification order, Skills, agent roles, evaluator composition, and human intervention can all become candidate variables. I do not freeze one method as the answer; I measure again under comparable conditions and let the result determine the next direction of search.

**Bound individual runs without closing the search space.** Code changes, CI, merge, installation, and deployment are checked separately. A tied experiment remains a tie. A CPU result does not become a device performance claim.

```text
hypothesis → execution → observation → verification → record
    ↑                                              │
    └──────── next candidate and methodology ←────┘
```

<a id="selected-work"></a>
## Selected work

### GEODE

An **autonomous agent runtime** that plans work and calls tools from a natural language request. I have built its long running memory, multi provider connections, tool execution, and permission boundaries as a solo project.

The current architecture separates `core` for execution, `evals` for evaluation and evidence production, and `evolve` for searching experimental changes. Original results stay distinct from summaries, while failures and incomplete calls remain visible. Evaluation results and trajectories are not only archives; they become inputs to later analysis, learning views, and experiment design.

SIL examines safety related behavior and Crucible evaluates task capability. The search changes **scaffolding around the model**, including system instructions, tool policy, Skills, and task decomposition, rather than model weights. I treat this as a non parametric form of RSI scaffold search without assuming that sustained self improvement has already been established.

[Code](https://github.com/mangowhoiscloud/geode) · [Docs](https://mangowhoiscloud.github.io/geode/docs) · [Execution and evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI experiments](https://mangowhoiscloud.github.io/geode/self-improving/)

### Compiler AX Lab

Independent research on handing over **reviewable changes with their cause, diff, and execution evidence**, rather than plausible looking code alone. The public project contains Rust tests for the public `furiosa-opt` SDK and a Python runner. It is unaffiliated with and not approved by FuriosaAI.

Public CPU records dated 2026-09-16 include **46,080 matching output values** in double buffering examples, plus a workspace run with **720 regular tests and 55 doctests passing**. These are separate executions and are not combined into one score.

The A/B pilot's control results were tied. Selecting B's change is separate from claiming that B's procedure was more effective. CPU value checks do not establish NPU correctness, execution overlap, or performance.

[Code and verification boundaries](https://github.com/mangowhoiscloud/compiler-ax-lab) · [Retrospective report](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### REODE @ pinxlab

I redesigned the GEODE derived harness into a code migration product. OpenRewrite handled rule based changes while LLMs handled parts requiring contextual interpretation. When a repair repeatedly returned to the same error, I introduced an investigation before fixing procedure.

**March 2026 delivery record:** a **5,523 file** service targeting Java 1.8→22 and Spring 4→6 passed **83/83 tests plus frontend and backend end to end verification**. The recorded execution covered 33 autonomous sessions, 1,133 rounds, and 5 hours 48 minutes with zero human intervention during that run. This does not mean there was no preparation, design, or final review.

Client code is private. The [previously public delivery summary and measurement scope](docs/PROFILE_NOTES.md#reode) remain available.

### Eco²

An AI recycling service. I started as the backend and infrastructure engineer in a five person MVP team, then continued development and operation solo. The chatbot grew into a multi agent workflow with tool calls, parallel LangGraph execution, and SSE streaming.

**Recorded milestones:** the **2025 AI SeSACTHON Excellence Award (4th/181)** and a **24 node Kubernetes cluster** managed with Terraform, Ansible, and ArgoCD. Public load records report the Scan API at **97.8% with 1,000 VU**, and a separate ext authz path at **1,477 RPS with 2,500 VU**. VU means virtual users in a load test, not actual users.

The service has closed. Its architecture and engineering lessons remain in the technical portfolio.

[Technical portfolio](https://mangowhoiscloud.github.io/eco2/) · [Project repository](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>Other work</strong></summary>

**Kiki @ pinxlab · 2026.04–05:** a Slack directed workflow in which agents split analysis, implementation, and review. The focus was a two stage gate against unsupported approval rather than the number of roles.

**Cotton @ pinxlab · 2026.05:** a single tenant SaaS for RPG script translation. Dialogue is modeled as a graph of branches, conditions, character voice, and subtitle budgets rather than isolated strings. It uses LLM CLI adapters with separate generation and evaluation providers.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** a game studio experiment connecting multiple CLI agents through a shared interface. `transcript.jsonl` and pure reducers support replay, with generation and evaluation placed across providers.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** a KakaoTech hackathon service turning older adults' unrealized dreams into AI generated narratives and images. I contributed across backend, AI, and infrastructure.

**[Aimo](https://github.com/KTB16Team) · 2024:** backend development for an LLM based conflict mediation app.

</details>

<a id="concepts"></a>
## Concepts

An **agent** uses tools to make progress on a task instead of only generating an answer. A **harness** manages the surrounding tools, memory, permissions, and failure handling. The model proposes an action; the harness controls execution and verification.

**RSI (Recursive Self-Improvement)** refers here to the recursive problem of feeding evidence from earlier executions back into later changes and experiments. GEODE searches the execution scaffold rather than directly training model weights. Adoption of a change and repeated improvement require separate evidence.

```text
task loop:    goal → tool execution → inspect result → next action
search loop:  candidate → evaluation → record → next candidate and search strategy
```

<details>
<summary><strong>Concepts used for verification and search</strong></summary>

**Skill:** task specific instructions retrieved when needed. The existence of a Skill does not establish effectiveness; it needs to be used and evaluated on subsequent work.

**Regression test:** a check that detects whether a resolved problem returns.

**Ratchet:** a mechanism that prevents an established verification standard from being quietly weakened.

**Evaluation gate:** conditions a result must satisfy before adoption. Independent checks take precedence over the generating agent's self assessment, and an LLM judge remains a supporting instrument rather than an infallible answer key.

**Search space:** the set of choices that may become change candidates. It includes prompts, task decomposition, context, tool policy, Skills, role composition, evaluation methods, and points of human intervention.

[GEODE's two loops](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [Evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts)

</details>

<a id="experience"></a>
## Experience

| Period | Experience |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · Public CPU test and development workflow research records |
| 2026.02–present | **GEODE** · Solo development. SIL experiments 2026.05–06, Crucible 2026.07–present |
| 2026.03–05 | **pinxlab** · Freelance delivery of REODE, Kiki, and Cotton |
| 2025.10–2026.02 | **Eco²** · Backend and infrastructure in a five person MVP, followed by solo development and operation · 2025 AI SeSACTHON Excellence Award |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · Full time · Petabyte scale distributed storage in a global team |
| 2024.07–11 | **Kakao Tech Bootcamp** · Backend, DevOps, LLM · DREAM hackathon project |
| 2017.03–2023.08 | **Pusan National University** · B.S., Computer Science & Engineering |

At Rakuten, I worked on C and Kubernetes based storage. The previously listed **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0** experience belongs to this period.

<a id="more"></a>
## Notes

I document implementation and experimental findings on my [blog](https://rooftopsnow.tistory.com) and [YouTube](https://www.youtube.com/@mango_fr). I prefer records that preserve execution details and failures in a form that can be reused in later work.

[LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202) · Previous GitHub account: [@mng990](https://github.com/mng990)

---

<sub>Content reviewed: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">Sources, scope, and maintenance notes</a> · The release badge links to the latest version; profile checks do not certify project performance.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
