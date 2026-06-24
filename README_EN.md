<p align="right">
  <a href="README.md">🇰🇷 한국어</a> · <strong>🇺🇸 English</strong>
</p>

<h1 align="center">Jihwan Ryu (류지환)</h1>

<p align="center">
  <strong>I build action, verification, and improvement as loops.</strong><br/>
  LLMs diverge without control. My harness closes the loop until they converge.
</p>

<p align="center">
  <a href="https://github.com/mangowhoiscloud?tab=followers"><img src="https://img.shields.io/github/followers/mangowhoiscloud?label=Follow&style=social" alt="Follow"></a>&nbsp;
  <a href="https://www.youtube.com/@mango_fr"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>
  <a href="https://rooftopsnow.tistory.com"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=tistory&logoColor=white" alt="Blog"></a>
  <a href="https://linkedin.com/in/jihwan-ryu-b6b04a202"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/Self--Improving_Hub-6B4FBB?style=flat-square&logo=githubpages&logoColor=white" alt="Self-Improving Hub"></a>
</p>

---

### Loops All the Way Down

From a single agent turn to shipping to self-improvement, every layer runs as the same loop.
The outer loop measures what the inner one produced, and that measurement becomes the next loop's input.

```
┌─ ⑤ Feedback Loop          market · users · hiring challenges → input to the next build
│  ┌─ ④ Self-Improving Loop  quantify behavior → propose mutation → measurement gate → adopt/reject
│  │  ┌─ ③ Production Loop   plan → build → CI ratchet → ship → share
│  │  │  ┌─ ② Verify Loop    generate → verify → reflect → replan
│  │  │  │  ┌─ ① Agentic Loop   while(tool_use): reason → act → observe
```

### How I Work

- **I treat the agent as a search process over compute and wrap the system around it**: hands that call tools, a queue that schedules calls, memory that layers context, a permission gate in front of dangerous calls
- **Verification in deterministic code outside the agent**: no trust in self-reports, generation and evaluation split across providers (cross-provider judge), noise bands and control arms before any improvement curve
- **Each evaluation layer before the autonomy it allows**: one tool call, one new evaluation layer; code migration drew the deterministic 70% first, LLMs only in the ambiguous 30%

### Harness Engineering

| Axis | Role | Practice |
|---|---|---|
| **Orchestration** | Decide the next action from LLM output | AgenticLoop `while(tool_use)`, SubGoal DAG, parallel sub-agent delegation, lane queues |
| **Context & Memory** | Layer, compress, recover long-session context | 5-Tier Memory, 2-Phase compaction, 200K absolute guard: zero overflow across long sessions, ~80% multi-turn input token cut via prompt-cache alignment |
| **Gateway** | One control point over multiple providers | Single interface over Anthropic·OpenAI·Zhipu, 4-stage failover, circuit breakers, cross-provider dispatch, per-token cost tracking |
| **Verify** | Converge nondeterministic output to trustable levels | Deterministic gates + LLM judges + drift detection in orthogonal layers, cross-LLM agreement (Krippendorff's α) |
| **Observe & Improve** | Measure everything; adopt improvement only by measurement | Hook event bus, per-run transcripts, Petri behavioral audits + measurement gate (Self-Improving Loop) |

#### Harness Landscape · 4-Quadrant Positioning

```
                          Autonomous
                              ▲
                              │
           Q2                 │                Q1
      Minimal+Autonomous      │       Comprehensive+Autonomous
                              │
      · SWE-agent             │         ★ GEODE (+ Self-Improving)
      · Codex CLI       · Claude Code   · REODE (delivered)
      · AutoGen          (← my build tool) · Devin · Manus
                              │         · OpenHands
                              │
  ◄───────────────────────────┼───────────────────────────────►
      Minimal                 │              Comprehensive
                              │
           Q3                 │                Q4
      Minimal+Assisted        │        Comprehensive+Assisted
                              │
      · Aider                 │         · Cursor · Copilot
      · Gemini CLI            │         · Eco² (Chat Harness)
      · CrewAI                │         · Kiki (Slack Governance)
                              │
                              ▼
                           Assisted
```

---

### Projects

**GEODE** · agentic-loop-based autonomous agent harness · [repo](https://github.com/mangowhoiscloud/geode) · [portfolio](https://mangowhoiscloud.github.io/portfolio/geode)
A long-running system specialized in exploration, research, and signal collection. Multi-provider gateway,
5-tier memory, 4-layer tool dispatch, and HITL permission gates, built solo from the SDK runtime up.
Runs my daily work autonomously.

**GEODE Self-Improving Loop** · a closed loop of measured self-improvement · [hub](https://mangowhoiscloud.github.io/geode/self-improving/) · [petri bundle](https://mangowhoiscloud.github.io/geode/petri-bundle/) · [video](https://www.youtube.com/watch?v=TuEOGQrO9Us)
Adversarial scenario generation (co-scientist topology) → Petri multi-dimensional behavioral audit → only mutations
clearing the no-mutation control arms' noise band get adopted. The first real measurements surfaced silent defects
(mutations that never fired, a lucky frozen baseline), which I published and corrected openly. The floor of trustworthy
measurement came before any improvement curve. The full audit archive ships as a public static bundle.

**REODE** · autonomous code-migration agent @ pinxlab (freelance, delivered)
GEODE's harness redesigned into a coding-agent product, delivering a live service's Java 8→22 and
Spring Boot 2→3 migration. Deterministic OpenRewrite (70%) split from LLM territory (30%); agent deception
(weakening tests to pass builds) blocked by a 5-gate scorecard; a 40-repeat stuck-fix incident resolved by
mandating explore-before-fix.

| Real-World Result (delivered 2026.03) | |
|------|------|
| Target | 5,523 files (241 Java + 355 JSP + 47 XML), Java 1.8→22 · Spring 4→6 |
| Outcome | 83/83 tests + FE/BE E2E verification passed |
| Run | 33 autonomous sessions · 1,133 agentic rounds · 5h 48m (zero human intervention) |

**Eco²** · AI multi-agent recycling service · [portfolio](https://mangowhoiscloud.github.io/portfolio/eco2) · SeSACTHON Excellence Award, 4th/181
Started on 14 EC2 nodes, provisioned as code with Terraform·Ansible, run declaratively via ArgoCD on a 24-node K8s cluster, all solo.
A strict temperature-0.1 chatbot grown into a production-level multi-agent system through tool calling,
parallel LangGraph dispatch, SSE streaming, and Agent SDK. Concurrency 0→1,000 VU at 97.8%,
evaluation quality 69.4→99.8/100 (Swiss Cheese 3-layer), auth handler 48→1,500 RPS.

**Kiki** · Slack-native multi-agent governance @ pinxlab
A CTO·PO·Lead·Dev·QA self-team autonomously analyzes, implements, and reviews a live legacy codebase;
the manager directs and approves through Slack alone. A 2-stage gate blocks "conservative PASS" at the system level.

**Cotton** · single-tenant SaaS for RPG game-script translation @ pinxlab
Existing tools (Crowdin·Lokalise) treat game dialogue as key-value strings. Cotton models the branching dialogue graph
as a first-class data model: branches, conditions, character voice, subtitle-length budgets. LLM CLI adapters
(Codex·Claude Code) and a cross-provider judge converge translation quality.

**Crumb & Crumb Studio** · multi-host agent game studio · [repo](https://github.com/mangowhoiscloud/crumb)
A 3-day spike abstracting Claude Code, Codex, and Gemini CLI behind one interface. Replay-deterministic state via a
transcript.jsonl single source of truth + pure reducers; same-provider evaluation inflation blocked by cross-provider placement.

---

### Timeline

```
mangowhoiscloud/
├── 2017.03-2023.08/  Pusan National University · B.S. Computer Science & Engineering
├── 2024.07-2024.11/  Kakao Tech Bootcamp · Backend · DevOps · LLM
├── 2024.12-2025.08/  Rakuten Symphony Korea · Cloud Engineer (petabyte-scale distributed storage, global team)
├── 2025.10-2026.02/  Eco² · BE/Infra in a team of 5 → solo E2E (24-node K8s, SeSACTHON 4th/181)
├── 2026.02-present/  GEODE · autonomous agent harness (solo)
├── 2026.03-2026.05/  REODE · Kiki · Cotton @ pinxlab · freelance delivery
└── 2026.05-2026.06/  GEODE Self-Improving Loop · measurement-gated self-improvement
```

---

### Project Links

| Date | Project | Role | Link |
|------|---------|------|------|
| 2026.05-2026.06 | **Self-Improving Loop**: Petri audit × measurement gate | Solo | [hub](https://mangowhoiscloud.github.io/geode/self-improving/) |
| 2026.05 | **Crumb**: multi-host agent studio | Solo | [mangowhoiscloud/crumb](https://github.com/mangowhoiscloud/crumb) |
| 2026.05 | **Cotton**: RPG game-script translation SaaS · branching-dialogue-graph data model | Freelance | pinxlab |
| 2026.04-2026.05 | **Kiki**: Slack-native agent-org orchestration | Freelance | pinxlab |
| 2026.03-2026.04 | **REODE**: migration & coding agent, forked from GEODE | Freelance | pinxlab |
| 2026.02-present | **GEODE**: autonomous agent harness | Solo | [mangowhoiscloud/geode](https://github.com/mangowhoiscloud/geode) |
| 2026.02 | **LLMART**: CLI-based LLM-as-judge evaluation | Solo | [mangowhoiscloud/llmart](https://github.com/mangowhoiscloud/llmart) |
| 2025.10-2026.02 | **Eco²**: AI multi-agent, 24-node K8s | BE/Infra → E2E | [SeSACTHON/backend](https://github.com/SeSACTHON/backend) |
| 2024.12-2025.08 | **Rakuten Robin Storage · Object Storage**: distributed storage | Cloud Engineer | Rakuten Symphony |
| 2024 | **Aimo**: LLM conflict-mediation app | Backend | [KTB16Team](https://github.com/KTB16Team) |
