<p align="right"><strong>한국어</strong> · <a href="README_EN.md">English</a></p>

# 류지환

**에이전트의 실행을 만들고, 변경의 효과를 검증합니다.**

분산 스토리지와 백엔드, 클라우드 인프라를 거쳐 자율 에이전트 런타임과 평가 시스템을 개발합니다. 도구 호출이 실패했을 때 원인을 추적할 수 있는지, 코드나 scaffold를 바꾼 뒤 같은 조건에서 결과가 나아지는지를 다룹니다.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [블로그](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

[![GEODE release](https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&label=GEODE)](https://github.com/mangowhoiscloud/geode/releases/latest)

[대표 작업](#selected-work) · [발전 과정](#evolution) · [작업 방식](#how-i-work) · [검증과 기록](#evidence) · [이력](#experience)

<a id="selected-work"></a>
## 대표 작업

### GEODE · 실행과 제작의 경계

장기 세션의 메모리, 모델 연결, 도구 실행, 권한과 검증을 관리하는 **자율 에이전트 런타임**입니다. `core`는 실행을, `evals`는 측정을, `evolve`는 실험적인 scaffold 탐색을 맡습니다.

런타임을 만드는 시스템도 별도로 다룹니다. 여기서 **메타 하네스는 하네스의 코드와 scaffold를 제작·검증·수정하는 장치**입니다. Claude Code나 Codex CLI가 `AGENTS.md`, `CLAUDE.md`, Skills와 CI 계약을 읽어 GEODE를 고칩니다. 실행 위에 놓인 또 하나의 제어기를 뜻하지 않습니다.

![GEODE의 제작·실행·실험 경계. Build Scaffold가 coding agent의 변경을 안내하고, 런타임의 Context Control·AgenticLoop·Verify·Observe가 실행과 Trajectory를 관리한다. Experimental Loop의 Scaffold Search는 검토할 후보를 제안한다.](assets/geode-overview.svg)

실행 기록은 다음 변경의 근거가 됩니다. **변경 후보의 채택과 PR merge·release 승인은 별개**이며, 배포 권한은 운영자에게 남습니다.

<details>
<summary>메타 하네스 · 변경을 만들고 CI ratchet으로 회귀를 차단하는 과정</summary>

개발자는 작업 범위와 수용 조건을 정하고, coding agent는 기존 구현과 실패 근거를 읽은 뒤 격리된 worktree에서 변경합니다. **수정한 코드뿐 아니라 재발을 잡는 검사도 남깁니다.** CI는 같은 변경 revision을 검사하며, 실패하면 원인을 수정하고 다시 검증합니다.

![GEODE CI Ratchet. 격리 worktree에서 만든 코드·회귀 검사를 CI가 확인하며, 실패하면 수정한다. 통과한 뒤에도 현재 head와 base, 필수 checks와 검토 권한을 확인해야 merge할 수 있다.](assets/geode-ci-ratchet.svg)

| CI가 고정하는 기준 | 코드에 남긴 검사 | 차단하는 회귀 |
| --- | --- | --- |
| 실행·타입·의존성 계약 | Ruff, mypy, pytest, import contracts | 동작 실패, 타입 불일치, 계층 의존성 위반을 검사합니다. |
| 기준선과 정책 | Legacy import ratchet, architecture exception debt, performance baseline | 새 legacy import와 정책 위반, 성능 기준선 위반을 검사합니다. |
| 프롬프트·평가·문서의 일치 | Prompt hash, eval catalog/contract, generated-doc checks | 의도하지 않은 prompt 변경과 코드·계약·문서의 drift를 검사합니다. |
| PR 단위 승인 근거 | Required CI `Gate` + `scripts/merge_pr.py` | 누락·실패한 필수 job, 오래된 head/base SHA, 맞지 않는 branch protection 근거를 거부합니다. |

변경 경로에 따라 실제 검사 범위는 달라집니다. CI ratchet은 **코드·계약의 회귀를 막는 장치**이고, 아래 Experimental Loop의 ratchet은 **실험 후보를 채택하는 규칙**입니다. CI 통과만으로 merge 권한이나 성능 향상이 생기지는 않습니다.

[개발 절차](https://github.com/mangowhoiscloud/geode/blob/fd53e0b9c95c1179f8f36ee91a5d3f0b15674af5/docs/workflow.md) · [CI 구현](https://github.com/mangowhoiscloud/geode/blob/fd53e0b9c95c1179f8f36ee91a5d3f0b15674af5/.github/workflows/ci.yml) · [Merge admission](https://github.com/mangowhoiscloud/geode/blob/fd53e0b9c95c1179f8f36ee91a5d3f0b15674af5/scripts/merge_pr.py)

</details>

<details>
<summary>한 실행에서는 무엇이 반복되는가</summary>

아래는 호출과 응답의 시간순서가 중요한 구간입니다. 컨텍스트 구성과 compaction은 런타임이 관리하고, 검증은 해당 실행의 계약에 따라 수행합니다.

![GEODE 실행 순서. 사용자의 목표를 받은 AgenticLoop가 tool call과 observation을 반복하고, 실행 계약이 요구할 때 verifier에서 판정과 근거를 받는다. 완료 선언과 verifier 결과, 종료 사유는 별도 기록이다.](assets/geode-runtime.svg)

모델의 완료 선언, 검증 결과, 실행 종료 사유를 같은 값으로 취급하지 않습니다. 컨텍스트·실행·검증·관측을 나누면 어느 부분의 변경이 결과에 영향을 줬는지 조사할 수 있습니다.

</details>

[코드](https://github.com/mangowhoiscloud/geode) · [랜딩 페이지](https://mangowhoiscloud.github.io/geode/) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts)

<a id="harbor-rollout"></a>
#### Harbor · 점수 차이를 실행 기록으로 조사하기

Terminal-Bench 2.1에서 GEODE와 native Codex를 **paired rollout**으로 비교했습니다. 두 arm은 같은 task·repetition에 배정되지만, 매 시도마다 별도 컨테이너에서 독립적으로 작업합니다. Codex의 행동을 GEODE가 따라 하는 실행이나 실서비스 shadow traffic은 아닙니다.

계획은 **89 tasks × 5 repetitions × 2 arms = 890 cells**였습니다. Cell은 `task × repetition × arm`이며, 두 arm 모두 OpenAI subscription의 `gpt-5.6-sol`, 요청 effort `max`를 사용했습니다. 당시 GEODE arm은 `AgenticLoop`에 Harbor 기반 `terminal_exec` 하나를 연결한 구성입니다. 이후 full-runtime 실험과 구분합니다.

![Harbor paired rollout. 동결 계약 아래 GEODE와 native Codex를 각각 독립 컨테이너에서 실행하고 각 task verifier로 채점한다. 비공개 원본에서 계약상 선정·정규화·공개 검사를 거쳐 artifact와 파생 replay를 만든다.](assets/harbor-rollout.svg)

Harbor가 컨테이너·timeout·task verifier를 관리합니다. **Score는 verifier 결과와 동결된 선정 규칙으로 계산하고, trajectory는 도구 호출과 실패 경로를 조사하는 데 씁니다.** 그림의 분기는 두 arm의 독립성을 나타내며 동시 실행을 뜻하지 않습니다.

공통 유효 429쌍의 보조 관측에서 **통과 건수는 GEODE 339/429, Codex 331/429**입니다. 환경 문제로 제외·미해결 cell이 남아 사전 정의한 전체 평가값은 측정 불성립입니다. 공식 leaderboard 순위나 현재 GEODE 전체 런타임의 우위로 제시하지 않습니다.

[실행 계약과 한계](https://github.com/mangowhoiscloud/geode/blob/main/docs/eval/terminal-bench-2.md) · [공개 run artifact](https://github.com/mangowhoiscloud/geode-eval-artifacts/tree/main/terminal-bench/terminalbench21-sol-max-fullsuite-paired-20260827t190300z) · [GEODE / Codex replay](https://mangowhoiscloud.github.io/geode/benchmarks/terminal-bench/replay/)

<details>
<summary>어떤 데이터를 남겼고, 측정 장치는 어떻게 보강했는가</summary>

| 데이터 | 공개 파일 | 읽는 목적 |
| --- | --- | --- |
| 실행 계약 | `run-spec.json`, `task-manifest.json` | 모델·task·예산과 비교 범위를 확인합니다. |
| 시도 이력 | `attempts.jsonl` | 원래 시도와 보충 시도, 유효성·선정 여부를 추적합니다. |
| 행동 기록 | `trajectory.json`, replay 파생물 | 보존된 ATIF·세션 기록을 바탕으로 행동의 순서와 출처를 조사합니다. |
| 채점 근거와 분석 | `native-results.json`, `verifier-receipts.json`, `outcomes.json`, `analysis.json` | 원본 reward, 계약상 선정 결과, 집계의 분모를 확인합니다. |
| 공개 명세 | `publication*.json` | 공개 대상 파일·hash와 검증 범위를 확인합니다. |

원본 job은 비공개로 보존하고, schema·lineage·hash와 secret·PII·로컬 경로를 검사한 파생물을 공개합니다. ATIF에서 복원한 `recording.cast`는 **derived replay**이지 당시 PTY 원본 녹화가 아닙니다. Observer PTY는 실행 절차의 별도 기록입니다. 공개 replay가 모든 prompt·출력 본문을 담는 것도 아니며, 이후 재실행으로 과거의 누락 기록이나 점수를 덮어쓰지 않습니다.

후속 통합 점검에서는 inclusive-input 비용 추정의 cache-write 분리 누락, cleanup 오류가 최초 실행 오류를 가리는 경로, 성능 검사 실패 시 raw sample의 미보존을 확인했습니다. 비용 계산과 오류·표본 보존을 고치고, usage의 생산자와 분모를 명시했습니다.

후속 **별도 Astra smoke**는 run spec을 동결한 뒤 Harbor 0.22.0에서 reward 1/1, verifier 6/6, error/retry 0/0, tool call/result 2/2, orphan 0을 기록했습니다. 이는 1/89 task·k=1의 account-scoped 통합 확인이며, 위 `gpt-5.6-sol` 비교의 보충 표본이나 전체 suite·Reflexion 효과·whole-runtime usage의 완전성을 입증하는 결과가 아닙니다.

[Harbor gap closure PR #3311](https://github.com/mangowhoiscloud/geode/pull/3311) · [Terminal-Bench Astra smoke](https://github.com/mangowhoiscloud/geode/blob/main/docs/eval/2026-09-05-terminalbench-astra-openssl-smoke.md)

</details>

### Eco² · 연결이 끊겨도 작업은 계속되도록

재활용을 돕는 AI 서비스의 백엔드와 Kubernetes 인프라를 개발·운영했습니다. 긴 AI 작업을 처리하는 worker와 사용자에게 진행 상황을 전달하는 SSE connection의 수명을 분리했습니다. **2025 AI 새싹톤 우수상**(4th/181)을 받았으며, 서비스 운영은 종료됐습니다.

| 워크로드 | 실행 방식 | 설계의 초점 |
| --- | --- | --- |
| Chat | Intent routing, 필요한 도메인 노드의 병렬 실행과 합류 | 질문마다 필요한 작업을 선택하고 결과를 합쳐 답변합니다. |
| Scan | Celery chain: Vision → Rule/RAG → Answer → Reward | 오래 걸리는 작업의 실행과 진행 이벤트 전달을 분리합니다. |
| 이미지 생성 | 별도 graph branch | 대화의 다른 작업과 다른 실행 경로를 갖습니다. |

개발 방식, 네트워크, 배치 구조, 두 AI 워크플로우, 관측성을 나눴습니다. 아래 항목은 필요한 것만 펼쳐 볼 수 있습니다.

<details>
<summary>클러스터 구성 · 제어, 요청 처리, 작업 실행의 경계</summary>

**API 응답, AI 작업, 진행 이벤트는 같은 수명으로 움직이지 않습니다.** 백엔드 README의 5개 계층을 바탕으로, Kubernetes 내부에서 무엇을 함께 배치하고 무엇을 별도 경로로 나눴는지 보여줍니다.

![Eco² 클러스터 구성. Kubernetes control plane과 Platform controller 아래에 Edge, Service, Integration, Persistence를 배치하고 요청, 작업, 관측 경로를 구분한 도식.](assets/eco2-cluster.svg)

Gateway는 요청을 라우팅하고, 도메인 API는 작업을 등록합니다. **RabbitMQ가 전달하는 작업과 Redis 기반의 진행 이벤트는 별도 경로입니다.** AI worker는 Scan·Chat을, storage worker는 DB 저장·checkpoint 동기화를 담당합니다. Event Router와 SSE Gateway는 작업 실행과 분리돼 진행 상태를 전달합니다.

그림의 영역은 기능 경계입니다. 실제 배치는 다음 조건으로 나뉘며, 하나의 영역이 하나의 노드나 namespace를 뜻하지 않습니다.

| 배치 경계 | 구현에서 확인한 조건 |
| --- | --- |
| 클러스터·플랫폼 제어 | 단일 `k8s-master`에 kubeadm control plane을 구성합니다. Istiod·ALB Controller·ExternalDNS의 selector와 ArgoCD 설치 절차도 이 역할을 사용합니다. KEDA는 `infra-type=monitoring`에 배치합니다. |
| 진입점·인증 | Gateway는 `role=ingress-gateway`, ext-authz는 `domain=auth`와 `auth` namespace를 사용합니다. 인증을 요청하는 proxy와 판정하는 서버가 분리됩니다. |
| 작업 실행·이벤트 전달 | `worker-ai`와 `worker-storage`를 구분합니다. Event Router는 `domain=event-router`, SSE Gateway는 `domain=sse`를 사용하며 namespace도 `event-router`와 `sse-consumer`로 나뉩니다. |
| 상태·관측 | PostgreSQL과 용도별 Redis, RabbitMQ, monitoring·logging 역할을 구분합니다. PostgreSQL의 selector는 넓은 `domain=data`이며, `logging` namespace는 sidecar injection을 끕니다. |

**배치 분리는 HA나 보안 격리의 증명이 아닙니다.** 단일 master, PostgreSQL standalone, RabbitMQ dev 1 replica 선언은 그대로 남습니다. State KV는 Redis 데이터의 역할이지 추가 DB 서버가 아닙니다. 자료마다 다른 노드 수를 하나로 고정하지 않았으며, 종료된 서비스의 코드 구조를 설명합니다.

[README의 5개 계층](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/README.md#service-architecture) · [노드 선언](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/terraform/main.tf) · [kubeadm bootstrap](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/ansible/playbooks/02-master-init.yml) · [Namespace 경계](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/namespaces/base/namespaces.yaml) · [Cluster manifests](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/clusters/dev/apps) · [Workload 배치](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/domains)

</details>

<details>
<summary>네트워크 토폴로지 · ALB에서 애플리케이션까지</summary>

**ALB는 트래픽을 전달하고, Gateway는 라우팅과 인증 위임을 수행합니다.** Route 53의 DNS 조회, Istiod의 설정 배포, ext-authz의 권한 검사를 HTTP 전달 경로와 구분했습니다.

![Eco² ingress 경로. Client에서 Kubernetes 밖의 ALB로 HTTPS 요청을 보내고, instance target의 NodePort를 거쳐 Gateway와 API에 도달한다. ext-authz 인증 호출과 Istiod 설정 배포는 별도 경로다.](assets/eco2-ingress.svg)

- **AWS 경계:** ALB가 ACM 인증서로 TLS를 종료하고, `instance` target의 EC2 NodePort로 HTTP를 전달합니다. 전용 Gateway Pod가 있다고 ALB target이 그 노드로만 제한되는 것은 아닙니다.
- **Gateway 경계:** VirtualService·EnvoyFilter는 Envoy에 적용하는 설정이지 추가 proxy가 아닙니다. `CUSTOM` AuthorizationPolicy가 지정한 경로에서만 ext-authz에 gRPC 검사를 요청합니다.
- **네트워크 기반:** Calico VXLAN과 kube-proxy가 Pod·Service 전달을 뒷받침합니다. AI worker의 외부 LLM 호출은 ingress와 다른 outbound HTTPS 경로입니다.

Terraform의 EC2 선언은 public subnet을 사용하고, 전역 `default-deny-all`은 비활성화돼 있습니다. 따라서 private-only 배치나 ALB-only 접근, 전체 네트워크의 default-deny 격리를 주장하지 않습니다. 작업 queue와 SSE 이벤트 전달의 세부 경로는 아래 Scan·Chat 도식에서 이어집니다.

[ALB bridge 설정](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/routing/gateway/base/gateway.yaml) · [Istio·NodePort 설정](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/clusters/dev/apps/05-istio.yaml) · [VPC 정의](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/terraform/modules/vpc/main.tf) · [Gateway 인증 정책](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/routing/gateway/base/authorization-policy.yaml) · [NetworkPolicy 구성](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/network-policies/base/kustomization.yaml)

</details>

<details>
<summary>메타 하네스 구성 · 서비스와 인프라 변경은 어떻게 만드는가</summary>

개발자는 `CLAUDE.md`, Skills와 SDK 호환성 점검 command에 작업 맥락과 검증 절차를 정리했습니다. Claude Code는 **제작 측 coding agent**이며, 위 클러스터에서 사용자 요청을 처리하는 Chat/Scan worker와 다릅니다. 아래는 제작 도구와 산출물의 연결이지, 모든 작업이 거치는 단일 시퀀스가 아닙니다.

![Eco² 제작과 배포의 책임. 개발자와 scaffold가 Claude Code를 안내하고 CI는 변경 서비스를 검사한다. 조건에 맞는 빌드가 image와 Git manifest를 갱신하며 ArgoCD가 클러스터에 적용한다.](assets/eco2-build.svg)

| 제작 구성 | 역할 |
| --- | --- |
| 지침·Skills | `CLAUDE.md`와 `.claude/skills/`가 도메인 맥락, architecture·code review·Git workflow·K8s debugging 절차를 제공합니다. |
| 도구·검사 | `.claude/commands/check-sdk-compat.md`가 SDK 사용을 점검하고, CI가 변경된 서비스의 format·lint·test를 실행합니다. |
| 배포 산출물 | 해당 CI는 PR에서 품질 검사를, 조건에 맞는 push·수동 실행에서 이미지 build/push와 Git manifest의 tag 갱신을 수행합니다. ArgoCD가 Git 상태를 적용합니다. |

개발 과정에서는 실패 로그를 읽고 수정·재검증합니다. 이는 개발 절차이며 CI가 스스로 코드를 고치는 기능이 아닙니다. Eco²의 서비스별 CI와 GEODE의 기준선·계약 ratchet을 같은 구현으로 설명하지 않습니다. 개발·검토 권한, CI 검사, ArgoCD의 배포 책임도 구분합니다.

[개발 지침](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/CLAUDE.md) · [Skills·Commands](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/.claude) · [실제 CI](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/.github/workflows/ci-services.yml) · [ArgoCD 설정](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/clusters/dev/apps/40-apis-appset.yaml)

</details>

<details>
<summary>Scan 워크플로우 · 작업 실행과 진행 이벤트 전달의 분리</summary>

Scan API는 작업을 등록하고 `202 + job_id`를 반환합니다. Celery chain은 RabbitMQ의 단계별 queue를 따라 실행되며, 클라이언트는 별도의 SSE 연결로 진행 상태를 받습니다. SSE 연결이 닫혔다고 worker 작업까지 취소되는 구조는 아닙니다.

![Eco² Scan의 두 경로. RabbitMQ와 Celery chain이 Vision·Rule·Answer·Reward 작업을 실행한다. 각 단계의 Redis Streams 이벤트는 Event Router·Pub/Sub·SSE를 거쳐 전달되며 ACK와 재접속 복구 규칙을 따로 관리한다.](assets/eco2-scan.svg)

| 경로 | 저장·전달 규칙 |
| --- | --- |
| 작업 | `scan.vision → scan.rule → scan.answer → scan.reward` queue로 단계를 연결합니다. 이 Reward는 서비스의 캐릭터 보상이며 GEODE benchmark reward와 다릅니다. |
| 이벤트 | Worker가 `XADD`하고 Router가 consumer group으로 읽습니다. 처리 실패 시 ACK를 남기지 않아 pending 메시지를 reclaimer가 다시 처리할 수 있게 했습니다. |
| 재접속 | Pub/Sub은 실시간 전달을 맡습니다. State KV와 Streams는 상태 복구·catch-up의 근거이며, Pub/Sub 자체를 영속 로그로 취급하지 않습니다. |

[Scan tasks](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/apps/scan_worker/presentation/tasks) · [Event Router / SSE 수정 기록](https://rooftopsnow.tistory.com/237) · [부하 테스트와 병목 분석](https://rooftopsnow.tistory.com/255)

</details>

<details>
<summary>Chat 워크플로우 · 필요한 도구만 선택하고 결과를 합류시키기</summary>

Chat API가 RabbitMQ에 작업을 발행하고 TaskIQ worker가 LangGraph를 실행합니다. Router는 intent와 요청 맥락으로 필요한 노드를 선택합니다. 아래 세 갈래는 노드의 역할을 묶은 것이며 매 요청에서 모두 실행하지 않습니다.

![Eco² Chat의 선택과 합류. Intent router가 필요한 domain·API tool·image branch를 선택한다. Aggregator와 context 준비를 거쳐 답변하며 Eval은 설정한 경우에만 실행한다. Redis checkpoint와 PostgreSQL 보관은 별도 경로다.](assets/eco2-chat.svg)

| 실행·상태 | 구체적인 역할 |
| --- | --- |
| 선택과 합류 | 복수 intent를 `Send`로 dispatch하고 aggregator가 결과를 모읍니다. RAG feedback과 Eval은 설정에 따라 활성화되며, 무제한 재시도를 뜻하지 않습니다. |
| 도구 실행 | Production wiring은 주로 structured/function call로 인자를 정하고 application command를 실행합니다. 여러 ReAct agent가 자유롭게 반복하는 구성과 구분합니다. |
| 대화 상태 | Redis에 checkpoint를 쓰고 syncer가 PostgreSQL로 비동기 보관합니다. Redis miss 때 PG에서 읽는 경로와 대화 메시지를 저장하는 consumer는 별도입니다. |
| 사용자 전달 | Answer의 token event도 Event Router와 SSE Gateway를 거칩니다. HTTP 연결, worker 실행, checkpoint의 수명을 각각 관리합니다. |

[Graph factory](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/apps/chat_worker/infrastructure/orchestration/langgraph/factory.py) · [Checkpoint 구현](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/apps/chat_worker/infrastructure/orchestration/langgraph/sync) · [Redis / PostgreSQL 설계 기록](https://rooftopsnow.tistory.com/242)

</details>

<details>
<summary>관측성 구조 · 병목과 실패를 어느 기록에서 찾는가</summary>

Queue 적체, Pod의 상태, 요청 경로, LLM 노드의 실행은 서로 다른 기록을 요구합니다. 운영 메트릭·로그·분산 trace와 LLM trace를 한 가지 지표로 합치지 않고 나누어 수집했습니다.

![Eco² 관측성. API·worker·Envoy의 metrics, logs, request spans와 Chat LangGraph의 LLM trace를 구분해 수집한다. 각 저장·조회 경로를 queue 적체, 실패 맥락, 요청 지연, LLM 노드 조사에 연결한다.](assets/eco2-observability.svg)

| 조사할 문제 | 읽는 기록과 용도 |
| --- | --- |
| 작업 지연·적체 | Prometheus/Grafana의 queue depth, pending, 연결 수와 Pod 지표로 worker 부족과 전달 병목을 구분합니다. |
| 요청 실패 | 구조화 로그를 검색하고 Jaeger span으로 서비스·MQ·worker 호출 구간을 좁힙니다. Kiali는 mesh 관계를 보여줍니다. |
| LLM 응답 지연 | LangSmith의 노드 실행, token usage, 오류 기록으로 도구 대기와 모델 호출을 조사합니다. 사용 여부는 tracing 설정에 달려 있습니다. |

선언된 Istio trace sampling은 50%입니다. 이 도식은 **수집 경로와 조사 방법**을 설명하며 모든 요청의 trace가 보존됐다는 뜻은 아닙니다. 로그·trace는 관측 자료이지 응답 품질의 verifier 판정도 아닙니다.

[Logging manifests](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/logging) · [Trace sampling](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/workloads/routing/global/telemetry.yaml) · [LangSmith wiring](https://github.com/eco2-team/backend/blob/a0721271ac569679f1e4f19dd0745ab634a0c115/apps/chat_worker/infrastructure/telemetry/langsmith.py) · [Monitoring / tracing 배치](https://github.com/eco2-team/backend/tree/a0721271ac569679f1e4f19dd0745ab634a0c115/clusters/dev/apps)

</details>

<details>
<summary>개선 루프 · 관측한 실패가 다음 구조를 바꾸는 방식</summary>

Eco²에서 개선은 “새 기술을 추가했다”는 순서보다 **같은 압력을 재현하고, 병목 가설을 좁히고, 가장 작은 변경을 배포한 뒤 같은 신호로 다시 측정하는 순서**에 가까웠습니다. production runtime이 스스로 source를 바꾸는 자기개선은 아니었고, 사람과 coding agent가 함께 돌린 외부 engineering loop였습니다.

![Eco² 개선 과정의 책임별 경로. 같은 workload에서 실패를 재현하고 사람과 coding agent가 가설·작은 변경·회귀 검사를 만든다. CI와 Git·ArgoCD 배포 뒤 같은 신호로 다시 측정하며 사람이 keep·revise·revert를 결정한다.](assets/eco2-improvement.svg)

| 관측한 압력 | 세운 가설 | 변경 | 다음 측정에서 배운 것 |
| --- | --- | --- | --- |
| 50 VU 부근에서 SSE 연결과 RabbitMQ connection, scan-api memory가 함께 증가하고 readiness 503이 발생 | task 실행 수명과 progress delivery 수명이 한 연결 구조에 묶여 있다 | RabbitMQ는 task queue로 유지하고 진행 이벤트를 Redis Streams → Event Router → SSE Gateway로 분리 | 연결 증폭을 줄이자 queue wait, worker 상태, 외부 API가 다음 병목 후보로 이동했습니다. |
| publish 실패 뒤 ACK, reconnect gap, duplicate, hot Pub/Sub channel | event delivery는 단순 실시간 전송이 아니라 recovery contract가 필요하다 | ACK-on-success, reclaim, dedupe, Last-Event-ID catch-up, master-only Pub/Sub, 4-shard channel을 추가 | “정상 경로가 빠르다”보다 실패 뒤 복구 가능한지가 별도 검증 항목이 됐습니다. |
| VU sweep에서 CPU·memory보다 probe restart와 in-flight loss가 실패에 기여 | guardrail이 workload 특성과 맞지 않으면 보호 장치가 새로운 실패를 만든다 | KEDA min/max와 workload signal을 조정하고 probe 원인을 분리해 조사 | **guardrail 자체도 검증 대상**이라는 원칙이 생겼습니다. |
| Chat 응답 품질을 한 judge 점수로 설명하기 어려움 | 생성 품질과 evaluator 신뢰도를 같은 숫자로 합치면 실패 원인이 사라진다 | deterministic Code Grader, BARS LLM Judge, Calibration Monitor로 역할 분리 | 측정 장치도 drift와 wiring을 검증해야 했고, 이 경험이 GEODE의 evaluator separation으로 이어졌습니다. |

여기서 중요한 것은 성공 수치보다 **실패가 계약으로 바뀌는 과정**입니다. ACK 조건, recovery, KEDA fallback, CI 검증, Git desired state 같은 결정론적 규칙은 모델의 판단에 맡기지 않았습니다. Observability는 변경을 승인하는 권한이 아니라 다음 가설을 만드는 feedback surface였고, 최종 keep/revise/revert는 사람에게 남았습니다.

이 흐름을 압축하면 다음과 같습니다.

`failure signal → reproducible workload → hypothesis → scoped code/manifest diff → CI → Git/ArgoCD → same workload → human verdict → next contract`

GEODE에서는 이 느슨한 외부 루프를 trajectory, revision-bound evaluation, explicit ratchet과 promotion contract로 구조화했습니다. Eco²가 **운영 중 실패를 다음 변경의 입력으로 쓰는 루프**였다면, GEODE는 그 루프 자체를 재현 가능한 연구 대상으로 바꾸는 방향입니다.

</details>

공개 프로젝트 보고의 Scan 성공률은 **1,000 VU에서 97.8%**, 별도 ext-authz 부하 기록은 **2,500 VU에서 1,477 RPS**입니다. 서로 다른 workload이며 실제 사용자 수나 공통 성능 지표로 합치지 않습니다. 완료 건수와 성공률의 분모 불일치는 [출처 메모](docs/PROFILE_NOTES.md#eco2)에 남겼습니다.

[포트폴리오](https://mangowhoiscloud.github.io/eco2/) · [프로젝트 저장소](https://github.com/eco2-team/backend)

### Experimental Loop · 좋은 점수만으로는 채택하지 않기

모델 가중치가 아니라 시스템 지침, 도구 정책, Skill, 작업 분해 등 **scaffold의 변경 효과**를 탐색합니다. baseline과 candidate를 같은 task·evaluator·budget으로 비교하고, 모든 시도와 판정을 Ledger에 남깁니다.

<details>
<summary>Baseline이 바뀌는 조건: KEEP / REJECT / INVALID</summary>

![Experimental Loop의 Baseline 채택 조건. 동결한 비교의 Evaluation이 유효한지, 개선이 불확실성을 넘고 critical veto가 없는지 판정한다. KEEP·REJECT·INVALID와 모든 시도를 Ledger에 남기며 KEEP만 다음 Baseline을 바꾼다.](assets/experimental-admission.svg)

Ratchet은 이 판정 조건을 적용합니다. 단순 점수 상승, 동률, 불완전 실행만으로 baseline을 바꾸지 않습니다. `KEEP`도 해당 실험의 판정이지 배포 승인이나 지속적인 자기개선의 입증은 아닙니다.

</details>

[두 루프](https://mangowhoiscloud.github.io/geode/docs/concepts/two-loops/) · [실험 설계 · frozen experiment kernel](https://github.com/mangowhoiscloud/geode/blob/main/docs/architecture/crucible-kernel.md) · [RSI 실험 기록](https://mangowhoiscloud.github.io/geode/self-improving/)

### REODE @ pinxlab · 코드 마이그레이션

GEODE에서 출발한 코드 마이그레이션 하네스입니다. OpenRewrite와 LLM 기반 문맥 수정을 결합해 Java 1.8→22, Spring 4→6 대상 **5,523개 파일** 규모 서비스에서 **83/83 테스트와 프론트엔드·백엔드 종단 검증**을 통과했습니다.

2026년 3월 납품 기록은 33개 자율 세션, 1,133라운드, 5시간 48분입니다. 해당 실행 중 사람 개입은 0회였으며, 준비와 최종 검토가 없었다는 의미는 아닙니다. [납품 기록 범위](docs/PROFILE_NOTES.md#reode)

<a id="evolution"></a>
## 발전 과정

프로젝트가 바뀔 때마다, 검증해야 할 대상도 달라졌습니다.

| 작업 | 다룬 문제 | 다음 작업에 남긴 설계 |
| --- | --- | --- |
| Eco² | AI 작업과 연결·배포의 수명이 다릅니다. | 비동기 실행, 이벤트 복구, 운영 책임의 분리 |
| GEODE | 서비스별 구현을 재사용 가능한 실행기로 만들어야 합니다. | 런타임과 하네스 제작 시스템의 분리 |
| SIL | Scaffold 변경의 safety 효과를 측정해야 합니다. | 외부 audit, critical-dimension floor, 실패 기록 |
| Crucible | 다른 revision의 성공을 합쳐도 최종 candidate의 증명은 아닙니다. | Candidate·evaluator·task pack을 동결한 비교와 승격 조건 |

<details>
<summary>SIL → Crucible: 실험 설계를 바꾼 실패</summary>

SIL은 Petri 계열의 다차원 safety audit로 scaffold 후보를 검사했습니다. 생성·audit·채택·revert와 transcript·비용 기록을 연결한 단계였습니다.

Crucible의 2026년 7월 캠페인에서는 서로 다른 candidate revision에서 통과한 row를 합쳐 target set이 닫힌 것처럼 보이는 문제가 드러났습니다. 마지막 candidate가 앞선 row 전체를 통과했다는 증거는 아니었습니다. 확인한 G4 row를 수정에 사용한 뒤 다시 평가한 결과도 held-out evidence로 남길 수 없었습니다.

현재 실험 계약은 candidate commit, evaluator/harness identity, content-bound task pack, paired comparison rule, budget과 veto를 실행 전에 고정합니다. 실패한 train row는 다음 candidate의 counterexample이 될 수 있지만, 한 번 본 sealed row는 같은 promotion claim에 다시 쓰지 않습니다.

[Crucible frozen experiment kernel](https://github.com/mangowhoiscloud/geode/blob/main/docs/architecture/crucible-kernel.md) · [역사적 Self-Improving Roadmap](https://github.com/mangowhoiscloud/geode/blob/main/docs/plans/2026-05-22-self-improving-roadmap.md)

</details>

**RSI(Recursive Self-Improvement)는 연구 방향이며 달성 선언이 아닙니다.** 현재는 scaffold 변경을 실행·측정·판정하는 외부 실험 시스템을 구축하고 있습니다. 다음 증거는 서로 다른 task family와 새로운 sealed evidence에서도 채택한 변경이 유효한지입니다.

<a id="how-i-work"></a>
## 작업 방식

- **가설을 반증 가능하게 씁니다.** 어떤 task family에서 무엇을 바꾸고, 어떤 metric과 veto로 판단할지 먼저 정합니다.
- **가장 작은 재현부터 만듭니다.** 실패한 입력과 호출 경로를 찾고 변경 범위와 보존할 조건을 정합니다.
- **조사 결과를 구현에 남깁니다.** 확인한 원인은 회귀 테스트로, 반복할 조사 과정은 Skill로 정리합니다. 실패하면 threshold를 낮추기 전에 원인을 확인합니다.

작업 분해, 컨텍스트, 도구 선택, 검증 순서와 evaluator 구성도 변경 후보입니다. 개별 실행의 예산은 제한하되, 방법론을 고정된 정답으로 두지 않습니다.

<a id="evidence"></a>
## 검증, 재현, 기록

Trajectory는 연구 데이터입니다. 무엇을 만들었는지뿐 아니라 **누가 어떤 기록을 읽고 무엇을 결정하는지**를 연결합니다.

| 생산자 | 남기는 기록 | 읽는 주체와 결정 |
| --- | --- | --- |
| 실행기 | 요청, tool call/result, observation, retry, 종료 사유 | 엔지니어가 실패 지점과 재현 조건을 찾습니다. |
| Evaluator | Run spec, revision, task ID, verifier 결과 | 비교 분석이 표본의 유효성과 score를 계산합니다. |
| Promotion gate | Ledger, lineage, KEEP·REJECT·INVALID | 실험 시스템이 다음 Baseline 또는 보류 상태를 정합니다. |
| 운영자 | CI·설치·배포 확인과 승인 | 코드 병합과 배포 여부를 결정합니다. |

원본과 파생 요약을 구분하고, 공개 전에 provenance와 privacy를 확인합니다. 로컬 테스트, 외부 평가, CI, 배포 확인은 서로를 대신하지 않습니다.

구체적인 파일 구조와 관측 보강 사례는 [Harbor paired rollout](#harbor-rollout)에 정리했습니다.

<a id="concepts"></a>
<details>
<summary>용어: agent · harness · meta-harness · RSI</summary>

- **Agent:** 도구를 사용해 작업을 진행합니다.
- **Harness:** 도구, 메모리, 권한, 실패 처리와 검증을 관리합니다.
- **Meta-harness:** 하네스 자체의 코드와 scaffold를 제작·검증·수정하는 시스템입니다.
- **RSI:** 이전 실행에서 얻은 근거로 이후 변경과 실험을 개선하려는 연구 방향입니다. 변경 채택과 반복 개선은 별개의 증거를 요구합니다.

</details>

<a id="experience"></a>
## 이력

| 기간 | 경험 |
| --- | --- |
| 2026.02–현재 | **GEODE** · 단독 개발 · SIL 2026.05–06 · Crucible 2026.07 · Harbor x 터미널벤치2.1 890-cell 롤아웃(비교군: Codex) 2026.08–09 |
| 2026.03–05 | **pinxlab** · 프리랜서(단독 개발) · REODE, Kiki, Cotton |
| 2025.10–2026.02 | **Eco²** · 백엔드/인프라(FE-DESIGN-AI-BACKEND/INFRA 5인, 1개월)에서 단독 개발·운영(1인, 3개월) · 2025 AI 새싹톤 우수상 |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · 정규직 · PB급 분산 스토리지 |
| 2024.07–11 | **Kakao Tech Bootcamp** · Backend, DevOps, LLM |
| 2017.03–2023.08 | **부산대학교** · 컴퓨터공학 학사 |

Rakuten에서는 **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0**에 참여했습니다.

<details>
<summary>그 밖의 작업</summary>

- **Kiki @ pinxlab · 2026.04–05:** Slack 기반 멀티에이전트 분석·구현·리뷰와 2단계 검증 게이트.
- **Cotton @ pinxlab · 2026.05:** 대화를 그래프로 모델링한 RPG 번역 SaaS.
- **[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb) · 2026.05:** 재생 가능한 CLI 에이전트 게임 스튜디오 실험.
- **[DREAM](https://github.com/KakaoTech-Hackathon-Dream) · 2024.09:** 생성형 AI 서사와 이미지 서비스.
- **[Aimo](https://github.com/KTB16Team) · 2024:** LLM 기반 갈등 중재 백엔드.

</details>

<a id="more"></a>
## 기록

구현과 실험의 자세한 내용은 [블로그](https://rooftopsnow.tistory.com)와 [YouTube](https://www.youtube.com/@mango_fr)에 남깁니다. 이전 GitHub 계정: [@mng990](https://github.com/mng990)

<sub>내용 검토: 2026-09-18 · <a href="docs/PROFILE_NOTES.md">수치의 출처와 범위</a></sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
