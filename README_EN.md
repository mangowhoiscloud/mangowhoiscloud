<p align="right"><a href="README.md">한국어</a> · <strong>English</strong></p>

# Jihwan Ryu

**I build verifiable systems, then feed their results back into the next search.**

My background spans distributed storage, backend engineering, and cloud infrastructure. Today I work on **autonomous agent runtimes and RSI (Recursive Self-Improvement) methodology**. I care about observable, reproducible execution and about preserving results and failures as material for the next experiment.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [Technical blog](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

[![GEODE release](https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&label=GEODE)](https://github.com/mangowhoiscloud/geode/releases/latest)

`RSI / scaffold search` · `Autonomous agent runtime` · `Cloud / Kubernetes / IaC` · `Evidence / trajectories`

[How I work](#how-i-work) · [Evolution](#evolution) · [Selected work](#selected-work) · [Verification and records](#evidence) · [Concepts](#concepts) · [Experience](#experience) · [Notes](#more)

<a id="how-i-work"></a>
## How I work

**Bound the problem first.** I find the failing input and actual call path, define what may change, then construct the smallest reproducible condition.

**Use models for exploration and evidence for decisions.** AI helps form hypotheses and implementation candidates. Tests, original logs, execution records, and external verification decide whether a change holds.

**Preserve results as data for the next search.** Successful changes, failed attempts, rejected hypotheses, trajectories, and evaluation results remain available. Causes become regression tests; repeatable investigations become Skills or procedures.

**Treat methodology itself as a search space.** Task decomposition, context, tool selection, verification order, Skills, agent roles, evaluator composition, and human intervention can all become candidate variables. Individual runs are bounded; the search space stays open.

<a id="evolution"></a>
## Evolution

Eco² was a production service where I built an **asynchronous agent workflow and cloud runtime**. GEODE separated those lessons into a reusable **autonomous agent runtime and meta-harness**. The current Experimental Loop feeds execution and evaluation evidence back into an **outer scaffold-search loop**.

```mermaid
sequenceDiagram
    participant E as Eco2
    participant G as GEODE Runtime
    participant M as Meta Harness
    participant X as Experimental Loop
    E->>G: Product workflow becomes reusable runtime
    G->>M: Runtime controls become explicit mechanisms
    M->>X: Verification becomes a search signal
    X->>M: Accepted scaffold candidate
    M->>G: Versioned policy and configuration
    G-->>X: New trajectory and evaluation evidence
```

The progression is mainly about separating the layers that **execute, control, observe, and improve** a stochastic system.

<a id="selected-work"></a>
## Selected work

### GEODE

An **autonomous agent runtime** with long-running memory, multi-provider routing, tool execution, permission boundaries, observability, and evaluation. The distribution separates `core` for execution, `evals` for evidence production, and `evolve` for experimental scaffold search.

Its meta-harness groups control mechanisms into Context Control, Plan and Execute, Verify, Observe, and Scaffold. These are code-backed control surfaces rather than conceptual labels.

```mermaid
sequenceDiagram
    participant U as User
    participant C as Context Control
    participant P as Plan and Execute
    participant V as Verify
    participant O as Observe
    U->>C: Goal and session state
    C->>P: Bounded context and tool surface
    loop Agentic execution
        P->>P: Plan, act, observe, replan
        P->>V: Candidate result
        V-->>P: Pass, retry, or replan
        P->>O: Events, calls, usage, state
    end
    O-->>U: Result plus session trajectory
```

Context budgets and compaction, dynamic replanning and convergence detection, verification modes and safety gates, event persistence, and session timelines live at different layers so each can be measured and changed independently.

[Code](https://github.com/mangowhoiscloud/geode) · [Docs](https://mangowhoiscloud.github.io/geode/docs) · [Meta-harness catalog](https://mangowhoiscloud.github.io/geode/docs/reference/meta-harness-catalog) · [Execution and evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI experiments](https://mangowhoiscloud.github.io/geode/self-improving/)

### Eco²

An AI recycling service that evolved from a chatbot into a multi-agent workflow using Vision LLM, RAG, tool calls, LangGraph-based processing, asynchronous SSE, and a Kubernetes platform.

```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant W as Agent Workflow
    participant L as LLM and RAG
    participant T as Tools and Data
    participant S as SSE Stream
    participant K as Kubernetes
    U->>A: Scan or chat request
    A->>W: Dispatch async workflow
    W->>L: Interpret and plan
    L->>T: Retrieve or call tool
    T-->>L: External observation
    L-->>W: Structured result
    W-->>S: Stream output
    S-->>U: Async response
    W->>K: Logs, metrics, traces
```

The main lesson was operating models inside a service runtime: asynchronous work, streaming, external data, observability, authorization, deployment automation, and load verification had to move together. This became the starting point for GEODE's runtime and meta-harness split.

**Recorded milestones:** **2025 AI SeSACTHON Excellence Award (4th/181)**, **24-node Kubernetes** with Terraform, Ansible, and ArgoCD, Scan API **97.8% at 1,000 VU**, and a separate ext-authz path at **1,477 RPS with 2,500 VU**. VU means virtual users, not actual users. The service has closed.

[Technical portfolio](https://mangowhoiscloud.github.io/eco2/) · [Project repository](https://github.com/eco2-team/backend)

### Experimental Loop

GEODE's outer loop searches **scaffolding around the model**, not model weights. System instructions, tool policy, Skills, and task decomposition can become candidates. A frozen measurement layer evaluates them before promotion or rejection.

```mermaid
sequenceDiagram
    participant B as Baseline
    participant S as Scaffold Search
    participant E as Evaluation
    participant L as Ledger
    participant R as Ratchet
    B->>S: Champion and search state
    S->>E: Candidate scaffold
    E->>E: Frozen audit and replication
    E-->>L: Scores, stderr, trajectory, lineage
    L->>R: Evidence-bound verdict input
    alt Real gain and no critical regression
        R->>B: Promote
    else Regression, tie, invalid run, or weak evidence
        R-->>S: Reject and preserve attempt
    end
    L-->>S: Prior for next hypothesis
```

**The ratchet does not move because a single score increased.** Candidate edits and measurement apparatus stay separate. Critical-dimension regressions can veto promotion, gain is compared against uncertainty, and baseline plus result ledgers are retained. Promotion changes the next baseline; rejection searches another hypothesis against the same baseline. CI adds deterministic ratchets for architecture, repository hygiene, prompt integrity, behavior, and coverage.

[Two loops](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [Experiment loop](https://mangowhoiscloud.github.io/geode/docs/self-improving/loop-overview) · [Public evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts)

### Compiler AX Lab

Independent research on handing over **reviewable changes with cause, diff, and execution evidence**. Public CPU records dated 2026-09-16 include **46,080 matching output values**, **720 regular tests**, and **55 doctests**. Separate executions are not combined into one score; the A/B controls tied, and CPU checks do not establish NPU performance. The project is unaffiliated with FuriosaAI.

[Code and verification boundaries](https://github.com/mangowhoiscloud/compiler-ax-lab) · [Retrospective report](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### REODE @ pinxlab

A GEODE-derived code-migration harness combining OpenRewrite with LLM-based contextual repair. A **5,523-file** Java 1.8→22 and Spring 4→6 delivery passed **83/83 tests** plus frontend/backend end-to-end verification. The recorded run covered 33 autonomous sessions, 1,133 rounds, and 5h 48m with zero human intervention during that run, not zero preparation or review.

[Delivery scope](docs/PROFILE_NOTES.md#reode)

<a id="evidence"></a>
## Verification, reproduction, and records

**Verification checks the contract.** Local tests, CI, external evaluation, installation, and deployment checks do not substitute for one another. Each record states what it actually established.

**Reproduction starts by freezing conditions.** Model route, harness revision, task set, effort, timeout, seed, and attempt lineage stay attached to a run when they can affect the result. Baseline and candidate share measurement conditions; errored or quota-contaminated runs stay separate.

**A trajectory is research data.** Requests, tool calls, external observations, failures, retries, and final verdicts form an execution trace. Successful trajectories show which controls were active. Failed trajectories become material for regression tests and mutation hypotheses. Original records take precedence over summaries, with provenance and privacy review for published artifacts.

```mermaid
sequenceDiagram
    participant A as Action
    participant O as Observation
    participant T as Trajectory
    participant V as Verification
    participant R as Regression Contract
    participant N as Next Experiment
    A->>O: Tool or environment interaction
    O->>T: Preserve raw observation
    T->>V: Replay with run conditions
    V-->>R: Pass, failure, tie, or invalid evidence
    R->>N: Test, gate, prior, or new hypothesis
    N-->>A: Next bounded execution
```

**A ratchet automates memory.** An understood failure becomes a regression test or deterministic check. A promoted baseline becomes the next reference. When a check fails, the first response is investigation, not relaxing the threshold.

<a id="concepts"></a>
## Concepts

An **agent** uses tools to make progress. A **harness** manages tools, memory, permissions, failure handling, and verification. A **meta-harness** makes that harness observable, bounded, and evolvable. **RSI (Recursive Self-Improvement)** here means feeding evidence from earlier executions back into later changes and experiments while keeping adoption and repeated improvement as separate claims.

<details>
<summary><strong>Other work</strong></summary>

**Kiki @ pinxlab · 2026.04–05:** Slack-directed multi-agent analysis, implementation, and review with a two-stage gate.  
**Cotton @ pinxlab · 2026.05:** RPG translation SaaS modeling dialogue as a graph.  
**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** replayable CLI-agent game-studio experiment.  
**[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** generative AI narrative and image service.  
**[Aimo](https://github.com/KTB16Team) · 2024:** LLM-based conflict-mediation backend.

</details>

<a id="experience"></a>
## Experience

| Period | Experience |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · CPU-test and workflow research |
| 2026.02–present | **GEODE** · Solo development · SIL 2026.05–06 · Crucible 2026.07–present |
| 2026.03–05 | **pinxlab** · Freelance · REODE, Kiki, Cotton |
| 2025.10–2026.02 | **Eco²** · Backend/infrastructure to solo development and operation · 2025 AI SeSACTHON Excellence Award |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · PB-scale distributed storage |
| 2024.07–11 | **Kakao Tech Bootcamp** · Backend, DevOps, LLM |
| 2017.03–2023.08 | **Pusan National University** · B.S., Computer Science & Engineering |

Rakuten work included **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0**.

<a id="more"></a>
## Notes

I document implementation and experimental findings on my [blog](https://rooftopsnow.tistory.com) and [YouTube](https://www.youtube.com/@mango_fr). [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202) · Previous GitHub account: [@mng990](https://github.com/mng990)

<sub>Content reviewed: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">Sources, scope, and maintenance notes</a></sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
