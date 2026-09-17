<p align="right"><strong>한국어</strong> · <a href="README_EN.md">English</a></p>

# 류지환

**자율 에이전트와 클라우드 시스템을 만들고, 실행에서 나온 증거를 다음 탐색의 입력으로 되돌립니다.**

분산 스토리지와 백엔드, 인프라를 거쳐 지금은 AI 에이전트 런타임과 개발 방법론을 다룹니다. 모델이 도구를 호출하는 것보다, 긴 작업을 어떻게 이어 가고 실패를 어떻게 남기며 결과를 어떻게 검증하고 다음 실험으로 연결할지에 더 관심이 있습니다.

한 번 잘 작동한 방법을 정답으로 고정하지 않습니다. 코드, 프롬프트, Skill, 도구 정책, 평가 방식, 역할 분해, 사람이 개입하는 지점까지 방법론 자체를 탐색 공간으로 둡니다. 개별 실행은 유한하게 닫고, 탐색 공간은 계속 열어 둡니다.

[GEODE](https://mangowhoiscloud.github.io/geode/) · [기술 블로그](https://rooftopsnow.tistory.com) · [YouTube](https://www.youtube.com/@mango_fr) · [LinkedIn](https://linkedin.com/in/jihwan-ryu-b6b04a202)

<p>
  <a href="https://mangowhoiscloud.github.io/geode/self-improving/"><img src="https://img.shields.io/badge/Research-RSI%20%26%20scaffold%20search-3f4854?style=flat-square" alt="RSI and scaffold search research"></a>
  <a href="https://github.com/mangowhoiscloud/geode"><img src="https://img.shields.io/badge/Systems-Autonomous%20Agents-3f4854?style=flat-square" alt="Autonomous agent systems"></a>
  <a href="https://mangowhoiscloud.github.io/eco2/"><img src="https://img.shields.io/badge/Infrastructure-Cloud%20%26%20Kubernetes-3f4854?style=flat-square" alt="Cloud and Kubernetes infrastructure"></a>
  <a href="https://github.com/mangowhoiscloud/geode/releases/latest"><img src="https://img.shields.io/github/v/release/mangowhoiscloud/geode?style=flat-square&amp;label=GEODE" alt="GEODE latest release"></a>
</p>

[작업 방식](#how-i-work) · [탐색 루프](#search-loop) · [대표 작업](#selected-work) · [이력](#experience)

<a id="how-i-work"></a>
## 작업 방식

**먼저 경계를 정합니다.** 실패한 입력과 실제 호출 경로를 찾고, 바꿀 수 있는 것과 보존해야 하는 것을 구분합니다. 큰 변경보다 문제를 재현하는 작은 검사를 먼저 만듭니다.

**탐색과 판정을 분리합니다.** 모델은 가설을 만들고 낯선 코드를 탐색하는 데 적극적으로 사용합니다. 채택 여부는 실행 결과, 테스트, 원본 로그와 독립된 평가로 결정합니다.

**실패를 버리지 않습니다.** 성공한 변경뿐 아니라 실패한 시도, 기각된 가설, 미완료 실행도 다음 후보를 만드는 데이터입니다. 결과를 요약하면서 원본을 지우지 않는 이유도 여기에 있습니다.

**방법론도 탐색 대상입니다.** 같은 문제를 더 잘 푸는 코드만 찾지 않습니다. 문제 분해, 컨텍스트 구성, 도구 선택, 검증 순서, Skill, 에이전트 역할과 권한 경계까지 후보로 둡니다. 특정 절차를 정답으로 고정하기보다 다음 실험이 이전 실험을 읽을 수 있게 만듭니다.

**배포까지 확인하되 범위를 넘겨 말하지 않습니다.** 코드 수정, CI, 병합, 설치와 배포는 각각 확인합니다. 실험이 동률이면 동률로 남기고, CPU에서 확인한 결과를 장치 성능으로 확장하지 않습니다.

<a id="search-loop"></a>
## 탐색 루프

```text
가설과 방법론 후보
        ↓
실행 → 관찰 → 검증 → 채택 또는 기각
 ↑                     ↓
 └──── 결과와 실패 기록 ────┘
```

이 루프에서 산출물은 최종 점수 하나가 아닙니다. trajectory, verifier receipt, 실패 원인, 기각 사유와 채택된 변경이 함께 남습니다. 이 기록은 다음 실험의 후보 생성과 평가 설계에 다시 사용됩니다.

RSI라는 표현은 여기서 **모델 가중치의 재귀적 자기학습이 아니라, 실행 결과를 이용해 모델 주변의 scaffold와 개발 방법론을 반복적으로 탐색하는 연구 방향**을 가리킵니다. GEODE의 공개 실험은 지속적인 자기개선을 입증했다고 주장하지 않습니다.

<a id="selected-work"></a>
## 대표 작업

### GEODE

자연어로 맡긴 일을 계획하고 도구를 사용하는 자율 에이전트 런타임입니다. 장기 실행 메모리, 여러 모델 제공자 연결, 도구 실행, 권한 경계, 평가와 실험 계층을 단독으로 구축해 왔습니다.

현재는 실행을 담당하는 `core`, 결과를 확인하는 `evals`, 변경 후보를 탐색하는 `evolve`의 경계를 분리합니다. 원본 결과와 파생된 분석을 구분하고, 실패와 미완료 호출도 보존해 다음 실험이 이전 실행을 데이터로 사용할 수 있게 합니다.

SIL은 안전성 관련 행동을, Crucible은 과제 수행 능력을 기준으로 변경 후보를 검사합니다. 바뀌는 대상은 모델 가중치가 아니라 지침, 도구 정책, Skill과 같은 실행 구성입니다.

[코드](https://github.com/mangowhoiscloud/geode) · [문서](https://mangowhoiscloud.github.io/geode/docs) · [실행 및 평가 기록](https://github.com/mangowhoiscloud/geode-eval-artifacts) · [RSI 실험 기록](https://mangowhoiscloud.github.io/geode/self-improving/)

### Compiler AX Lab

AI가 만든 코드를 원인, 변경, 실행 증거가 연결된 작은 수정안으로 넘기는 방법을 연구합니다. 공개 `furiosa-opt` SDK의 Rust 테스트와 Python 실행기를 다루는 독립 프로젝트이며 FuriosaAI 소속 또는 승인 프로젝트는 아닙니다.

2026-09-16 공개 CPU 기록에는 double buffering 예제의 **46,080개 출력값 일치**, 워크스페이스의 **720개 일반 테스트와 55개 doctest 통과**가 남아 있습니다. A/B 파일럿의 대조 검사 결과는 동률이었고, CPU 값 검증은 NPU 정확성이나 성능을 의미하지 않습니다.

[코드와 검증 범위](https://github.com/mangowhoiscloud/compiler-ax-lab) · [회고 보고서](https://mangowhoiscloud.github.io/compiler-ax-lab/report.pdf)

### REODE @ pinxlab

GEODE에서 출발한 하네스를 코드 마이그레이션 제품으로 재설계했습니다. 규칙 기반 변경은 OpenRewrite에 두고 문맥 해석이 필요한 부분에 LLM을 사용했습니다. 반복 오류가 발생했을 때 수정 전에 조사하는 절차를 도입했습니다.

2026.03 납품 기록은 Java 1.8에서 22, Spring 4에서 6으로의 전환을 포함한 **5,523개 파일** 규모이며 **83/83 테스트와 프론트엔드 및 백엔드 종단 검증**을 통과했습니다. 기록된 실행은 33개 자율 세션, 1,133라운드, 5시간 48분입니다. 실행 중 사람 개입은 0회였지만 준비, 설계, 최종 검토가 없었다는 뜻은 아닙니다.

[공개 납품 기록의 범위](docs/PROFILE_NOTES.md#reode)

### Eco²

재활용을 돕는 AI 서비스입니다. 5인 팀의 백엔드와 인프라 담당으로 시작해 이후 고도화와 운영을 단독으로 이어갔습니다. 도구 호출, LangGraph 병렬 처리, SSE 스트리밍을 포함한 멀티에이전트 워크플로우와 클라우드 인프라를 함께 운영했습니다.

**2025 AI 새싹톤 우수상(4th/181)**을 받았고 Terraform, Ansible, ArgoCD 기반 **24노드 Kubernetes**를 운영했습니다. 공개 부하 기록은 Scan API **1,000 VU에서 97.8%**, 별도의 ext authz 경로 **2,500 VU에서 1,477 RPS**입니다. VU는 실제 이용자 수가 아니라 부하 시험의 가상 사용자입니다. 서비스 운영은 종료됐습니다.

[기술 포트폴리오](https://mangowhoiscloud.github.io/eco2/) · [프로젝트 저장소](https://github.com/SeSACTHON/backend)

<details>
<summary><strong>그 밖의 작업</strong></summary>

**Kiki @ pinxlab, 2026.04 to 05:** Slack에서 지시와 승인을 받고 여러 에이전트가 분석, 구현, 리뷰를 나누는 워크플로우입니다.

**Cotton @ pinxlab, 2026.05:** RPG 스크립트 번역 SaaS입니다. 분기, 조건, 캐릭터 말투, 자막 길이를 포함한 대화 그래프를 데이터 모델로 다뤘습니다.

**[Crumb & Crumb Studio](https://github.com/mangowhoiscloud/crumb), 2026.05:** 여러 CLI 에이전트를 공통 인터페이스로 묶고 실행 기록을 재생할 수 있게 한 게임 제작 실험입니다.

**[DREAM](https://github.com/KakaoTech-Hackathon-Dream), 2024.09:** 생성형 AI로 노년층의 못 이룬 꿈을 서사와 이미지로 풀어낸 카카오테크 해커톤 프로젝트입니다.

**[Aimo](https://github.com/KTB16Team), 2024:** LLM 기반 갈등 중재 앱의 백엔드를 개발했습니다.

</details>

## 공개 GitHub 활동

아래 카드는 공개 저장소를 기준으로 한 활동과 언어 분포입니다. 숙련도나 연구 성과의 점수로 사용하지 않습니다. GitHub Readme Stats의 공개 인스턴스는 GitHub API 제한에 따라 일시적으로 표시되지 않을 수 있습니다.

<p>
  <a href="https://github.com/anuraghazra/github-readme-stats"><img height="150" src="https://github-readme-stats.vercel.app/api?username=mangowhoiscloud&amp;hide_rank=true&amp;show_icons=false&amp;include_all_commits=true&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=57606a&amp;text_color=57606a" alt="Public GitHub activity statistics"></a>
  <a href="https://github.com/anuraghazra/github-readme-stats"><img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=mangowhoiscloud&amp;layout=compact&amp;langs_count=6&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=57606a&amp;text_color=57606a" alt="Languages in public non fork repositories"></a>
</p>

<a id="concepts"></a>
## 개념

**에이전트**는 답변만 생성하는 대신 도구를 사용해 일을 진행하는 프로그램입니다. **하네스**는 도구, 메모리, 권한, 실패 처리와 검증을 관리하는 실행 계층입니다. **Skill**은 특정 작업에서 필요할 때 불러오는 절차입니다. **평가 게이트**는 변경을 채택하기 전에 통과해야 하는 조건입니다.

<a id="experience"></a>
## 이력

| 기간 | 경험 |
| --- | --- |
| 2026.09 | **Compiler AX Lab** · 공개 CPU 테스트와 개발 워크플로우 연구 |
| 2026.02 to 현재 | **GEODE** · 단독 개발 · SIL, Crucible, RSI 및 scaffold 탐색 |
| 2026.03 to 05 | **pinxlab** · 프리랜스 · REODE, Kiki, Cotton 납품 |
| 2025.10 to 2026.02 | **Eco²** · 백엔드와 인프라, 이후 단독 고도화와 운영 |
| 2024.12–2025.08 | **Rakuten Symphony Korea** · Jr. Cloud Engineer, Storage Developer · 글로벌 팀에서 PB 규모 분산 스토리지 개발 |
| 2024.07 to 11 | **카카오테크 부트캠프** · 백엔드, DevOps, LLM |
| 2017.03–2023.08 | **부산대학교 정보컴퓨터공학부** · 학사 |

Rakuten에서는 C와 Kubernetes 기반 스토리지 개발에 참여했습니다. 기존 이력의 **Rakuten Cloud Native Platform, Storage Server v5.5.0 · Rakuten Storage v1.0.0** 경험도 이 시기에 해당합니다.

<a id="more"></a>
## 기록

구현 과정과 실험에서 얻은 내용은 [블로그](https://rooftopsnow.tistory.com)와 [YouTube](https://www.youtube.com/@mango_fr)에 남깁니다. 이전 GitHub 계정은 [@mng990](https://github.com/mng990)입니다.

<sub>내용 검토: 2026-09-17 · <a href="docs/PROFILE_NOTES.md">수치의 출처와 범위</a> · 프로필 지표는 공개 GitHub 활동의 시각화이며 프로젝트 성능 평가가 아닙니다.</sub>

[![Profile checks](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml/badge.svg?branch=main)](https://github.com/mangowhoiscloud/mangowhoiscloud/actions/workflows/profile.yml)
