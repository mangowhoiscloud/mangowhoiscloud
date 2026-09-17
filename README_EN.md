<p align="right"><a href="README.md">한국어</a> · <strong>English</strong></p>

# Hi, I'm Jihwan Ryu 👋

**Turning ideas into working systems, and one-off fixes into reusable ways of working.**

My path runs through distributed storage, backend engineering, and infrastructure. Today I build **AI agent runtimes and development workflows**: systems that use tools, recover from failures, preserve evidence, and make it all the way to deployment.

“It's working!” is a good start. My favorite follow-up is **“Why did it work, and will it work again?”** I trace the cause in the logs, make a small change, and leave a test to catch the same problem next time.

[Explore GEODE](https://mangowhoiscloud.github.io/geode/) · [Technical blog](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

<p>
  <a href="https://github.com/mangowhoiscloud/geode/releases/latest"><img src="https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&amp;label=GEODE" alt="Latest GEODE release"></a>
  <a href="https://github.com/mangowhoiscloud/geode-eval-artifacts"><img src="https://img.shields.io/badge/Evidence-open%20records-5865F2?style=flat-square" alt="Browse public evaluation records"></a>
  <a href="https://github.com/mangowhoiscloud/compiler-ax-lab"><img src="https://img.shields.io/badge/Compiler%20AX-CPU%20tests-327A52?style=flat-square" alt="Compiler AX Lab CPU verification records with explicit scope"></a>
</p>

[How I work](#how-i-work) · [Selected work](#selected-work) · [A small glossary](#concepts) · [Experience](#experience) · [More](#more)

<a id="how-i-work"></a>
## How I work

**Narrow the problem first.** Before editing a large codebase, I find the failing input and the real call path. I define what may change, what must stay intact, and the smallest check that can reproduce the problem.

**Explore with models; decide with evidence.** I use AI actively to form hypotheses and navigate unfamiliar code. But “fixed” needs commands, test results, and original logs behind it. Deleting a test to get a green build is not a fix.

**Make today's debugging useful tomorrow.** A discovered failure becomes a regression test; a repeatable investigation becomes a short guide or Skill. I prefer retrieving the right instructions when needed to stuffing every lesson into one long prompt.

**Close the loop through deployment, without overselling the result.** A code change, passing CI, a merge, and a working installation or deployment are separate checks. A tied experiment stays a tie. A CPU result does not become a device-performance claim.

> The automation I want to build is not just automation nobody watches. It is automation that makes **what a person should review** clear.

<a id="selected-work"></a>
## Let the work introduce me

### 🪨 GEODE — An agent that uses tools and leaves a record

An **autonomous agent runtime** that plans work and calls tools from a natural-language request. I have built its long-running memory, multi-provider connections, tool execution, and permission boundaries as a solo project.

**My current focus:** separating `core` for execution, `evals` for checking, and `evolve` for experimental changes. Original results stay distinct from summaries; failures and incomplete calls remain visible so a reader can trace what actually happened.

**The experiments are public too:** SIL checks safety; Crucible evaluates task capability. They change the **configuration around the model**—instructions, tool policies, and Skills—not model weights. Sustained self-improvement has not been established.

[Code](https://github.com/mangowhoiscloud/geode) · [Docs](https://mangowhoiscloud.github.io/geode/docs) · [Execution and evaluation records](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [Self-improvement experiments](https://mangowhoiscloud.github.io/geode/self-improving/)

### 🔬 Compiler AX Lab — From an AI draft to a reviewable change

Independent research on handing over **small changes with their cause, diff, and execution evidence**, rather than plausible-looking code alone. The public project contains Rust tests for the public `furiosa-opt` SDK and a Python runner. It is unaffiliated with, and not approved by, FuriosaAI.

**What was checked:** public CPU records dated 2026-09-16 include **46,080 matching output values** in double-buffering examples, plus a workspace run with **720 regular tests and 55 doctests passing**. These are separate executions, not numbers to add into one score.

**The useful lesson:** the A/B pilot's control results were tied. Selecting B's change is not evidence that B's procedure was more effective. CPU value checks do not establish NPU correctness, execution overlap, or performance.

[Code and verification boundaries](https://github.com/mangowhoiscloud/compiler-ax-lab) · [Retrospective report](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### 🛠️ REODE @ pinxlab — Shipping a legacy migration

I redesigned the GEODE-derived harness into a code-migration product. OpenRewrite handled rule-based changes; LLMs handled the parts needing contextual interpretation. When a repair kept repeating the same error, I added an **investigate-before-fixing procedure**.

**March 2026 delivery record:** a **5,523-file** service targeting Java 1.8→22 and Spring 4→6 passed **83/83 tests plus frontend/backend end-to-end verification**. The recorded execution covered 33 autonomous sessions, 1,133 rounds, and 5 hours 48 minutes with zero human intervention during that run—not zero preparation, design, or final review.

Client code is private. The [previously public delivery summary and measurement scope](docs/PROFILE_NOTES.md#reode) remain available.

### 🌱 Eco² — From a chatbot to an operated service

An AI recycling service. I started as the backend/infrastructure engineer in a five-person MVP team, then continued the development and operation solo. The chatbot grew into a multi-agent workflow with tool calls, parallel LangGraph execution, and SSE streaming.

**Milestones:** the **2025 AI SeSACTHON Excellence Award (4th/181)** and a **24-node Kubernetes cluster** managed with Terraform, Ansible, and ArgoCD. Public load records report the Scan API at **97.8% with 1,000 VU**, and a separate ext-authz path at **1,477 RPS with 2,500 VU**. VU means virtual users in a load test, not actual users.

The service has closed; its architecture and engineering lessons live on in the technical portfolio.

[Current technical portfolio](https://mangowhoiscloud.github.io/eco2/) · [Project repository](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>More things I've built — collaboration, translation, and games</strong></summary>

**Kiki @ pinxlab · 2026.04–05:** a Slack-directed workflow in which agents split analysis, implementation, and review. The focus was not merely having more roles, but a two-stage gate against unsupported approval.

**Cotton @ pinxlab · 2026.05:** a single-tenant SaaS for RPG-script translation. Dialogue is a graph of branches, conditions, character voice, and subtitle budgets—not isolated strings. It uses LLM CLI adapters with separate generation and evaluation providers.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** a three-day game-studio experiment connecting multiple CLI agents through a shared interface. `transcript.jsonl` and pure reducers support replay, with generation and evaluation placed across providers.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** a KakaoTech hackathon service turning older adults' unrealized dreams into AI-generated narratives and images. I contributed across backend, AI, and infrastructure.

**[Aimo](https://github.com/KTB16Team) · 2024:** backend development for an LLM-based conflict-mediation app.

</details>

<a id="concepts"></a>
## A small glossary, no prerequisites

An **agent** uses tools to make progress on a task instead of only writing an answer. A **harness** manages the surrounding tools, memory, permissions, and failure handling. The model proposes an action; the harness controls its execution and how it gets checked.

```text
Task loop:    goal → use a tool → inspect the result → next action
Change loop:  candidate → check under matched conditions → adopt / reject
```

<details>
<summary><strong>What about Skills, regression tests, ratchets, and self-improvement?</strong></summary>

**Skill:** a task-specific guide retrieved when needed—for example, an investigation sequence that finds the caller and reproduces the failure before making a change. Having the file does not prove it helps; the next task must actually use and test it.

**Regression test:** a check that notices when a fixed problem returns. Think of it as a way for the codebase to remember the bug.

**Ratchet:** a mechanism that prevents an improved standard from slipping backward. When a check gets slower, investigate the cause rather than quietly relaxing the threshold.

**Evaluation gate:** conditions a result must satisfy before adoption. Independent checks take precedence over the generating agent's confidence. An LLM judge is a supporting tool, not an infallible answer key.

**Self-improvement:** revising the same answer repeatedly differs from retaining a change and reusing it on later tasks. GEODE experiments with changes around the model. Adoption and repeated improvement still need separate evidence.

[GEODE's two-loop explanation](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [How to read the evidence](https://github.com/mangowhoiscloud/geode-eval-artifacts)

</details>

<a id="experience"></a>
## The path so far

| Period | Experience |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · Public CPU-test and development-workflow research records |
| 2026.02–present | **GEODE** · Solo development. SIL experiments 2026.05–06; Crucible 2026.07–present |
| 2026.03–05 | **pinxlab** · Freelance delivery of REODE, Kiki, and Cotton |
| 2025.10–2026.02 | **Eco²** · Backend/infrastructure in a five-person MVP → solo development and operation · 2025 AI SeSACTHON Excellence Award |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer - Storage Developer · Full-time · Petabyte-scale distributed storage in a global team |
| 2024.07–11 | **Kakao Tech Bootcamp** · Backend, DevOps, LLM · DREAM hackathon project |
| 2017.03–2023.08 | **Pusan National University** · B.S., Computer Science & Engineering |

At Rakuten, I worked on C/Kubernetes-based storage. The previously listed **Rakuten Cloud Native Platform - Storage Server v5.5.0 · Rakuten Storage v1.0.0** experience belongs to this period.

<a id="more"></a>
## Notes beyond the code

I write up lessons on my [blog](https://rooftopsnow.tistory.com) and share walkthroughs on [YouTube](https://www.youtube.com/@mango_fr).
Always happy to compare notes on an agent behaving strangely, a legacy system that needed care, or a better way to check a result.

[Talk on LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202) · Previous GitHub account: [@mng990](https://github.com/mng990)

---

<sub>Content reviewed: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">Sources, scope, and maintenance notes</a> · The release badge links to the latest version; profile checks do not certify project performance.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
