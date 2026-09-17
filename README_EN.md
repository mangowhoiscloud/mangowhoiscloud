<p align="right"><a href="README.md">한국어</a> · <strong>English</strong></p>

# Jihwan Ryu

**I build autonomous agents and cloud systems, then feed execution evidence back into the next search.**

My path runs through distributed storage, backend engineering, and infrastructure. Today I work on AI agent runtimes and development methodology. I am less interested in tool calling by itself than in how long running work continues, how failures remain inspectable, how results are verified, and how those results become inputs to the next experiment.

I do not freeze one successful method as the answer. Code, prompts, Skills, tool policies, evaluation design, role decomposition, and human intervention points can all become part of the search space. Individual runs are bounded. The methodological search space remains open.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [Technical blog](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

`RSI / scaffold search` · `autonomous agents` · `cloud / Kubernetes` · [GEODE latest release](https://github.com/mangowhoiscloud/geode/releases/latest)

[How I work](#how-i-work) · [Search loop](#search-loop) · [Selected work](#selected-work) · [Experience](#experience)

<a id="how-i-work"></a>
## How I work

**Set the boundary first.** I find the failing input and actual call path, then separate what may change from what must remain intact. I prefer a small reproducing check before a large edit.

**Separate exploration from judgment.** I use models actively to form hypotheses and navigate unfamiliar code. Adoption depends on execution results, tests, original logs, and independent evaluation.

**Keep failures.** Successful changes are not the only useful outputs. Failed attempts, rejected hypotheses, and incomplete runs become data for generating the next candidate. This is why summaries do not replace original records.

**Treat methodology as a search space.** I do not only search for better code. Problem decomposition, context construction, tool selection, verification order, Skills, agent roles, and permission boundaries are candidates too. The aim is not to declare one procedure final, but to make the next experiment able to learn from the previous one.

**Verify through deployment without exceeding the evidence.** A code change, CI, merge, installation, and deployment are separate checks. A tied experiment remains a tie. A CPU result does not become a device performance claim.

<a id="search-loop"></a>
## Search loop

```text
hypotheses and method candidates
              ↓
run → observe → verify → adopt or reject
 ↑                         ↓
 └──── results and failures ────┘
```

The output of this loop is not a single final score. Trajectories, verifier receipts, failure causes, rejection reasons, and adopted changes remain available. They become material for candidate generation and evaluation design in later experiments.

Here, RSI refers to a **research direction that recursively searches the scaffold and development methodology around a model using execution results**, not recursive weight training. GEODE's public experiments do not claim that sustained self improvement has been established.

<a id="selected-work"></a>
## Selected work

### GEODE

An autonomous agent runtime that plans work and uses tools from natural language requests. I have built its long running memory, multi provider connections, tool execution, permission boundaries, evaluation, and experimental layers as a solo project.

The current design separates the `core` execution runtime, `evals` measurement and evidence production, and `evolve` scaffold search. Inside the runtime, Model, Runtime, Harness, and Agent form the task loop. Outside it, candidate generation, measurement, promotion gates, and the ledger form a separate search loop. Original results and failures feed back into later candidates and search policy.

<p align="center"><img src="assets/geode-meta-harness.svg" alt="GEODE meta-harness: autonomous runtime inside an evidence-driven scaffold search loop" width="100%"></p>

SIL evaluates safety related behavior and Crucible evaluates task capability. The search changes instructions, tool policies, Skills, and other execution scaffolding rather than model weights.

[Code](https://github.com/mangowhoiscloud/geode) · [Docs](https://mangowhoiscloud.github.io/geode/docs) · [Execution and evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI experiment records](https://mangowhoiscloud.github.io/geode/self-improving/)

### Compiler AX Lab

Independent research on turning AI generated code into small changes connected to their cause, diff, and execution evidence. The public project contains Rust tests for the public `furiosa-opt` SDK and a Python runner. It is unaffiliated with and not approved by FuriosaAI.

Public CPU records dated 2026-09-16 include **46,080 matching output values** in double buffering examples and a workspace run with **720 regular tests and 55 doctests passing**. The A/B pilot's control result was tied. CPU value checks do not establish NPU correctness or performance.

[Code and verification boundaries](https://github.com/mangowhoiscloud/compiler-ax-lab) · [Retrospective report](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### REODE @ pinxlab

I redesigned the GEODE derived harness into a code migration product. OpenRewrite handled rule based changes while LLMs handled context dependent work. Repeated repair failures led to an investigate before fixing procedure.

The March 2026 delivery record covers a **5,523 file** service moving from Java 1.8 to 22 and Spring 4 to 6. It passed **83/83 tests plus frontend and backend end to end verification**. The recorded execution covered 33 autonomous sessions, 1,133 rounds, and 5 hours 48 minutes. Zero human intervention applies to that execution, not to preparation, design, or final review.

[Scope of the public delivery record](docs/PROFILE_NOTES.md#reode)

### Eco²

An AI recycling service. I started as the backend and infrastructure engineer in a five person MVP team, then continued development and operation solo. The system combined a multi agent workflow with cloud infrastructure, including tool calls, parallel LangGraph execution, and SSE streaming.

From the public portfolio, the application runtime can be read as an API edge feeding a LangGraph based agent workflow, model and data tools, an SSE response path, and an observability layer. That application plane ran on a Kubernetes platform provisioned with Terraform and Ansible and synchronized through ArgoCD. The diagram groups publicly described responsibilities rather than claiming source package boundaries.

<p align="center"><img src="assets/eco2-runtime.svg" alt="Eco2 runtime: multi-agent application flow on Kubernetes infrastructure" width="100%"></p>

The project received the **2025 AI SeSACTHON Excellence Award (4th/181)**. I operated a **24 node Kubernetes** environment with Terraform, Ansible, and ArgoCD. Public load records report the Scan API at **97.8% with 1,000 VU** and a separate ext authz path at **1,477 RPS with 2,500 VU**. VU means virtual users in a load test, not actual users. The service has closed.

[Technical portfolio](https://mangowhoiscloud.github.io/eco2/) · [Project repository](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>Other work</strong></summary>

**Kiki @ pinxlab, 2026.04 to 05:** a Slack directed workflow in which agents split analysis, implementation, and review.

**Cotton @ pinxlab, 2026.05:** an RPG script translation SaaS that models branches, conditions, character voice, and subtitle budgets as a dialogue graph.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb), 2026.05:** a game production experiment connecting multiple CLI agents through a shared interface with replayable execution records.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream), 2024.09:** a KakaoTech hackathon project using generative AI to turn older adults' unrealized dreams into narratives and images.

**[Aimo](https://github.com/KTB16Team), 2024:** backend development for an LLM based conflict mediation app.

</details>

## Public GitHub activity

I do not use public activity as a score for engineering or research quality. The previous GitHub Readme Stats images were removed because failed image loads appeared as question-mark boxes in some clients. From the profile README of public follower [@swstegall](https://github.com/swstegall), whose GitHub profile lists JPMorganChase, I kept the useful part of the pattern: clear section hierarchy and project-first visuals, without copying follower counters, view counters, streaks, or language-score cards.

<a id="concepts"></a>
## Concepts

An **agent** uses tools to make progress instead of only producing an answer. A **harness** manages tools, memory, permissions, failure handling, and verification around the model. A **Skill** is a procedure retrieved for a particular task. An **evaluation gate** is a condition that must be satisfied before a change is adopted.

<a id="experience"></a>
## Experience

| Period | Experience |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · Public CPU test and development workflow research |
| 2026.02 to present | **GEODE** · Solo development · SIL, Crucible, RSI and scaffold search |
| 2026.03 to 05 | **pinxlab** · Freelance delivery of REODE, Kiki, and Cotton |
| 2025.10 to 2026.02 | **Eco²** · Backend and infrastructure, followed by solo development and operation |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · Petabyte scale distributed storage in a global team |
| 2024.07 to 11 | **Kakao Tech Bootcamp** · Backend, DevOps, LLM |
| 2017.03–2023.08 | **Pusan National University** · B.S., Computer Science & Engineering |

At Rakuten, I worked on C and Kubernetes based storage. The previously listed **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0** experience belongs to this period.

<a id="more"></a>
## Notes

I publish engineering and experiment notes on my [blog](https://rooftopsnow.tistory.com) and [YouTube](https://www.youtube.com/@mango_fr). Previous GitHub account: [@mng990](https://github.com/mng990).

<sub>Content reviewed: 2026-09-18 · <a href="docs/PROFILE_NOTES.md">Sources and measurement boundaries</a> · Architecture diagrams summarize responsibility boundaries from public documentation and portfolio material; they are not project performance evaluations.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
