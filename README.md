<p align="right"><strong>한국어</strong> · <a href="README_EN.md">English</a></p>

# 류지환

**실행을 검증 가능한 시스템으로 만들고, 그 결과를 다음 탐색의 입력으로 돌립니다.**

분산 스토리지와 백엔드, 클라우드 인프라를 거쳐 현재는 **자율 에이전트 런타임과 RSI(Recursive Self-Improvement) 방법론**을 다룹니다. 한 번의 성공보다 실행이 관찰 가능하고 재현 가능한지, 결과와 실패가 다음 실험의 재료로 남는지를 중요하게 봅니다.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [기술 블로그](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

[![GEODE release](https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&label=GEODE)](https://github.com/mangowhoiscloud/geode/releases/latest)

`RSI / scaffold search` · `Autonomous agent runtime` · `Cloud / Kubernetes / IaC` · `Evidence / trajectories`

[작업 방식](#how-i-work) · [발전 과정](#evolution) · [대표 작업](#selected-work) · [검증과 기록](#evidence) · [개념](#concepts) · [이력](#experience) · [기록](#more)

<a id="how-i-work"></a>
## 작업 방식

**아이디어를 먼저 틀릴 수 있는 문장으로 바꿉니다.** “더 좋아질 것이다”는 실험이 아닙니다. 대상, 비율 또는 기준, 관찰할 행동과 결과를 먼저 정합니다. 제품 가설에서 `Y의 X%는 Z를 할 것이다`라고 쓰는 것과 같은 원리입니다. 에이전트 연구에서는 이를 `어떤 task family에서, 어떤 candidate가, 어떤 frozen metric과 veto를 통과할 것인가`로 번역합니다. 측정할 수 없는 기대는 승격 근거로 사용하지 않습니다.

**먼저 문제와 검증 범위를 좁힙니다.** 실패한 입력과 실제 호출 경로를 찾고, 무엇을 바꿀 수 있고 무엇을 보존해야 하는지 정한 뒤 가장 작은 재현 조건을 만듭니다.

**탐색에는 모델을 사용하고 판정에는 근거를 사용합니다.** AI로 가설과 구현 후보를 만들되 테스트, 원본 로그, 실행 기록과 외부 검증으로 변경의 성립 여부를 판단합니다.

**결과를 다음 탐색의 데이터로 남깁니다.** 성공한 변경, 실패한 시도, 기각된 가설, trajectory와 평가 결과를 보존합니다. 원인은 회귀 테스트로, 반복할 조사 과정은 Skill과 절차로 정리합니다.

**방법론 자체를 탐색 공간으로 둡니다.** 문제 분해, 컨텍스트, 도구 선택, 검증 순서, Skill, 에이전트 역할, 평가자 구성과 사람의 개입 지점까지 변경 후보가 됩니다. 개별 실행은 유한하게 닫되 탐색 공간은 닫지 않습니다.

<a id="evolution"></a>
## 발전 과정

Eco²에서는 실제 서비스를 운영하며 **비동기 에이전트 워크플로우와 클라우드 런타임**을 만들었습니다. GEODE에서는 이를 범용 **자율 에이전트 런타임과 메타 하네스**로 분리했습니다. SIL에서는 “scaffold 변경이 안전성 기준을 개선하는가”를 외부 audit로 측정했고, Crucible에서는 그 경험을 바탕으로 **candidate, evaluator, task pack, budget을 먼저 동결하는 실험 계약**으로 발전시켰습니다. 현재 Experimental Loop에서는 실행과 평가 기록을 다시 외부 scaffold 탐색 루프에 투입합니다.

```mermaid
sequenceDiagram
    participant E as Eco2
    participant G as GEODE Runtime
    participant S as SIL
    participant C as Crucible
    participant X as Experimental Loop
    E->>G: Product workflow becomes reusable runtime
    G->>S: Scaffold changes become measurable hypotheses
    S->>C: Audit history exposes experiment-design failures
    C->>X: Freeze candidate, evaluator, task pack, budget
    X-->>G: Accepted configuration or preserved rejection
    G-->>X: New trajectory and evaluation evidence
```

이 과정에서 중요한 변화는 “좋아 보이는 변경”을 만드는 능력이 아니라 **가설을 반증 가능하게 만들고, 실패가 다음 실험의 설계를 바꾸게 하는 능력**이었습니다.

### SIL에서 Crucible로

SIL은 Petri 계열의 다차원 safety audit와 critical-dimension floor를 사용해 scaffold 후보를 검사했습니다. 이 단계에서 생성, audit, promotion, revert를 하나의 루프로 닫고 실행 transcript와 비용을 남기는 기반을 만들었습니다.

Crucible의 2026년 7월 캠페인은 더 중요한 반례를 만들었습니다. 서로 다른 candidate revision에서 통과한 row를 이어 붙이면 겉으로는 target set이 닫혀 보여도, 마지막 candidate가 이전 row 전체에서 다시 검증된 것은 아니었습니다. 노출한 G4 row를 수정해 다시 쓰는 순간 그것은 held-out evidence가 아니라 training counterexample이 됐고, 천 개가 넘는 gate artifact와 수천만 token도 candidate, evaluator, task set, cost window가 함께 동결되지 않으면 재현 가능한 champion을 만들지 못했습니다.

그래서 현재 Crucible은 한 candidate commit, 한 evaluator/harness identity, content-bound task pack, paired comparison rule, budget과 veto를 **실행 전에 고정**합니다. 결과는 `KEEP`, `REJECT`, `INVALID`로 나뉘며 infrastructure failure를 낮은 task score로 바꾸지 않습니다. 실패한 train row는 다음 candidate의 counterexample이 되지만, 한 번 본 sealed row는 같은 promotion claim에 다시 쓰지 않습니다.

[Crucible frozen experiment kernel](https://github.com/mangowhoiscloud/geode/blob/main/docs/architecture/crucible-kernel.md) · [Self-Improving Roadmap](https://github.com/mangowhoiscloud/geode/blob/main/docs/plans/2026-05-22-self-improving-roadmap.md)

### RSI를 향한 현재 위치

RSI는 목표 방향이지 현재 달성 상태를 뜻하지 않습니다. 2026-05-22의 Self-Improving Roadmap은 `outer loop → inner memory/recall → cognitive loop` 순서로 문제를 분해했던 역사적 로드맵이며, 현재 문서 자체도 active execution ledger가 아니라 provenance라고 명시합니다. 지금은 그 초기 계획에서 **outer loop를 실행 가능한 실험 시스템으로 만들고, 그 과정에서 measurement와 promotion authority를 분리하는 단계**까지 왔습니다.

현재 위치를 간단히 쓰면 다음과 같습니다.

```text
service runtime
  -> autonomous agent runtime
  -> observable meta-harness
  -> SIL: safety-scaffold audit loop
  -> Crucible: frozen experiment + promotion ratchet   [current]
  -> repeated cross-task evidence and retained improvements
  -> broader recursive improvement across methodology [direction]
```

따라서 “RSI를 구현했다”가 아니라 **RSI를 지향하며, 반복 개선을 주장할 수 있는 실험 조건부터 구축하고 있다**고 표현합니다. 다음 단계의 핵심은 한 번의 KEEP이 아니라 서로 다른 task family와 새 sealed evidence에서 retained change가 다시 유효한지 확인하는 것입니다.

<a id="selected-work"></a>
## 대표 작업

### GEODE

장기 실행 메모리, 여러 모델 제공자 연결, 도구 실행, 권한 경계, 관찰과 평가를 갖춘 **자율 에이전트 런타임**입니다. 배포 경계는 `core`, `evals`, `evolve`로 나뉩니다. `core`는 실행, `evals`는 증거 생산, `evolve`는 실험적인 scaffold 탐색을 담당합니다.

메타 하네스는 Context Control, Plan and Execute, Verify, Observe, Scaffold로 제어 메커니즘을 구분합니다. 개념적인 분류가 아니라 실제 코드 경로와 제어 지점에 연결된 구조입니다.

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

컨텍스트 예산과 compaction, 동적 replan과 convergence detection, 검증 모드와 safety gate, event persistence와 session timeline을 서로 다른 계층에 두어 독립적으로 측정하고 변경할 수 있게 합니다.

[코드](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [메타 하네스 카탈로그](https://mangowhoiscloud.github.io/geode/docs/reference/meta-harness-catalog) · [실행과 평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI 실험](https://mangowhoiscloud.github.io/geode/self-improving/)

### Eco²

재활용을 돕는 AI 서비스입니다. Vision LLM, RAG, 도구 호출, LangGraph 기반 멀티에이전트 처리, 비동기 SSE와 Kubernetes 환경을 하나의 서비스 런타임으로 연결했습니다.

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

Eco²에서 얻은 핵심 경험은 **모델을 서비스 런타임 안에서 운영하는 문제**였습니다. 비동기 작업, 스트리밍, 외부 데이터, 관측성, 인증, 배포 자동화와 부하 검증이 함께 움직여야 했고, 이 경험이 GEODE의 런타임과 메타 하네스 분리로 이어졌습니다.

**주요 기록:** **2025 AI 새싹톤 우수상(4th/181)**, Terraform, Ansible, ArgoCD 기반 **24노드 Kubernetes**, Scan API **1,000 VU에서 97.8%**, 별도의 ext-authz 경로 **2,500 VU에서 1,477 RPS**. VU는 실제 이용자 수가 아닙니다. 서비스 운영은 종료됐습니다.

[기술 포트폴리오](https://mangowhoiscloud.github.io/eco2/) · [프로젝트 저장소](https://github.com/eco2-team/backend)

### Experimental Loop

GEODE의 외부 루프는 모델 가중치가 아니라 **모델 주변 scaffold**를 탐색합니다. 시스템 지침, 도구 정책, Skill, 작업 분해를 후보로 만들고 고정된 측정 계층에서 평가한 뒤 승격하거나 기각합니다.

```mermaid
sequenceDiagram
    participant H as Hypothesis
    participant B as Baseline
    participant S as Scaffold Search
    participant E as Evaluation
    participant L as Ledger
    participant R as Ratchet
    H->>B: Freeze target, metric, behavior, veto
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
    L-->>H: Evidence for next falsifiable hypothesis
```

**래칫은 점수가 한 번 올랐다는 이유만으로 움직이지 않습니다.** 후보 변경과 측정 장치를 분리하고 critical dimension의 회귀를 veto하며 gain을 불확실성과 비교합니다. baseline과 result ledger를 보존하고 실패한 후보도 지우지 않습니다. 승격은 다음 baseline을 바꾸고, 기각은 같은 baseline 위에서 다른 가설을 찾게 합니다.

[두 루프](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops) · [실험 루프](https://mangowhoiscloud.github.io/geode/docs/self-improving/loop-overview) · [공개 평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts)

### Harbor rollout에서 배운 것

외부 benchmark를 붙이는 일도 같은 방식으로 다룹니다. “Harbor가 붙었다”가 가설의 끝이 아니라, **어떤 실패를 보존하고 어떤 단위로 계산하며 어떤 evidence에 권한을 줄 것인가**를 다시 정의하는 계기가 됐습니다.

v1.0.28 준비 과정에서는 실제 rollout과 통합 초안을 대조하면서 여러 결함 지점을 찾았습니다. cache read/write의 포함 관계와 비용 표시가 UI까지 일관되게 전달되지 않았고, Harbor의 정리 단계에서 난 2차 오류가 원래 실행 오류를 가릴 수 있었으며, 성능 실패의 원시 표본이 충분히 남지 않았습니다. 문서와 최신 verifier 계약의 drift, 이미 대체된 오래된 통합 초안도 함께 분리했습니다. whole-runtime usage와 Reflexion 효능처럼 아직 관측하지 못한 것은 완료로 표시하지 않았습니다.

수정은 “성공률을 높였다”가 아니라 **측정 장치를 고쳤다**는 데 의미가 있습니다. 최초 실행 오류를 우선 보존하고, cache accounting의 owner와 denominator를 명시하고, raw sample과 진단을 남기고, superseded 변경을 재적용하지 않았습니다. 이후 Terminal-Bench 2.1 smoke에서는 run spec을 사전 동결한 뒤 Harbor 0.22.0에서 한 task를 한 번 실행해 reward **1/1**, verifier **6/6**, Harbor error/retry **0/0**, tool call/result **2/2, orphan 0**을 기록했습니다. 이 결과도 1/89 task, k=1의 account-scoped smoke일 뿐 suite 성능으로 확대하지 않습니다.

[Harbor gap closure PR #3311](https://github.com/mangowhoiscloud/geode/pull/3311) · [Terminal-Bench Astra smoke](https://github.com/mangowhoiscloud/geode/blob/main/docs/eval/2026-09-05-terminalbench-astra-openssl-smoke.md)

### REODE @ pinxlab

GEODE에서 출발한 코드 마이그레이션 하네스입니다. OpenRewrite와 LLM 기반 문맥 수정을 결합했습니다. Java 1.8→22, Spring 4→6 대상 **5,523개 파일** 규모 서비스에서 **83/83 테스트와 프론트엔드, 백엔드 종단 검증**을 통과했습니다. 기록된 실행은 33개 자율 세션, 1,133라운드, 5시간 48분이며 해당 실행 중 사람 개입은 0회였습니다. 준비와 최종 검토가 없었다는 의미는 아닙니다.

[납품 기록 범위](docs/PROFILE_NOTES.md#reode)

<a id="evidence"></a>
## 검증, 재현, 기록

**검증은 결과의 모양이 아니라 계약을 확인합니다.** 로컬 테스트, CI, 외부 평가, 설치, 배포 확인은 서로 대체하지 않습니다. 각 기록에는 무엇