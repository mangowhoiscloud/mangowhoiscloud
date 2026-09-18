#!/usr/bin/env python3
"""Render the profile's fixed-layout SVGs; reuse the approved Eco² theme."""
import argparse
from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def text(x, y, value, css="body", anchor="start"):
    return f'<text x="{x}" y="{y}" class="{css}" text-anchor="{anchor}">{escape(value)}</text>'


def rect(x, y, w, h, css="node"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="{css}"/>'


def path(d, css="flow", arrow=True):
    end = '' if arrow else ' style="marker-end:none"'
    return f'<path d="{d}" class="{css}"{end}/>'


def box(x, y, w, h, name, *lines, focus=False):
    return rect(x, y, w, h, "focus" if focus else "node") + text(x + 20, y + 36, name, "name") + "".join(
        text(x + 20, y + 68 + 28 * i, line) for i, line in enumerate(lines)
    )


def label(x, y, w, value):
    return rect(x - w // 2, y - 20, w, 28, "mask") + text(x, y, value, "small", "middle")


def diamond(x, y, w, h, *lines):
    return (f'<path d="M{x} {y-h//2} {x+w//2} {y} {x} {y+h//2} {x-w//2} {y}Z" class="node"/>'
            + "".join(text(x, y + 8 + (i - (len(lines)-1)/2) * 28, line, "body", "middle")
                      for i, line in enumerate(lines)))


def figure(name, height, title, subtitle, desc, background, edges, nodes, footer):
    theme = (ASSETS / "eco2-cluster.svg").read_text(encoding="utf-8")
    defs = re.search(r"<defs>.*?</defs>", theme, re.S).group()
    # Unique marker IDs also allow the figures to share one inline review page.
    defs = defs.replace('id="arrow', f'id="{name}-arrow').replace('url(#arrow', f'url(#{name}-arrow')
    body = "\n".join((background, edges, nodes))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="{name}-title {name}-desc">
<title id="{name}-title">{escape(title)}</title>
<desc id="{name}-desc">{escape(desc)}</desc>
{defs}
<rect width="1280" height="{height}" fill="var(--paper)"/>
{text(32, 48, title, "title")}
{text(32, 84, subtitle, "body muted")}
{body}
<path d="M32 {height-64}H1248" stroke="var(--rule)"/>
{text(32, height-28, footer, "small")}
</svg>
'''


def geode_overview():
    background = rect(32, 144, 352, 376, "boundary") + rect(424, 144, 824, 376, "boundary")
    edges = "".join((
        path("M208 312V368"), path("M640 268H688"),
        path("M360 424H664V268H688"), path("M952 252H1000"), path("M1000 296H952", "control"),
        path("M824 324V400"), path("M816 488V588"), path("M424 640H208V480", "control"),
    ))
    nodes = "".join((
        text(56, 176, "META-HARNESS / BUILD", "section"), text(448, 176, "GEODE / RUNTIME", "section"),
        box(56, 200, 304, 112, "Build Scaffold", "Instructions · Skills · CI"),
        box(56, 368, 304, 112, "Coding agents", "Claude Code · Codex CLI"),
        box(448, 216, 192, 108, "Context", "Control"),
        box(688, 216, 264, 108, "AgenticLoop", "Model · tools", focus=True),
        box(1000, 216, 224, 108, "Verify", "Run contract"),
        box(688, 400, 536, 88, "Observe", "Trajectory · usage · termination evidence"),
        box(424, 588, 528, 104, "Experimental Loop", "Scaffold Search · candidate evaluation"),
        label(512, 404, 256, "reviewed runtime change"), label(896, 548, 184, "execution evidence"),
        label(208, 568, 264, "candidate proposed for review"),
        text(992, 620, "Separate authority", "section"), text(992, 652, "PR merge / release"),
        text(992, 680, "remain operator-owned.", "small"),
    ))
    return figure("geode-overview", 768, "GEODE / Build, execute, investigate",
                  "The development harness changes the runtime; it does not control each live turn.",
                  "Build instructions guide coding agents. Reviewed code changes reach GEODE's context, loop and verification components. Execution observations feed experimental scaffold search; proposed candidates return for review. Experimental adoption, merge and release have separate authority.",
                  background, edges, nodes, "Solid: execution or artifact handoff. Dashed: verdict / proposal. Scaffold experiments do not update model weights.")


def geode_ci():
    edges = "".join((
        path("M336 268V308H172V364"), path("M640 212H1112V364", "control"),
        path("M312 424H360"), path("M640 424H680"), path("M904 424H976"),
        path("M792 508V556H172V484", "control"), path("M1112 484V604"),
    ))
    nodes = "".join((
        box(32, 160, 608, 108, "Developer scope + build scaffold", "Acceptance · AGENTS.md · CLAUDE.md · Skills"),
        box(32, 364, 280, 120, "Coding agent", "Source / GAP audit", "Isolated worktree"),
        box(360, 364, 280, 120, "Reviewed change", "Code + regression test", "Docs + CHANGELOG"),
        diamond(792, 424, 224, 168, "CI ratchet", "Checks pass?"),
        box(976, 364, 272, 120, "Merge admission", "Current head / base", "Checks + authority", focus=True),
        box(976, 604, 272, 96, "develop → main", "Recheck CI + approval"),
        label(944, 412, 56, "pass"), label(436, 556, 320, "fail → diagnose, correct, recheck"),
        label(1112, 304, 192, "review authority"),
        text(32, 644, "What is pinned", "section"),
        text(32, 680, "Behavior, dependencies, prompts and evaluation contracts."),
        text(32, 712, "The same revision must satisfy the required checks.", "small"),
    ))
    return figure("geode-ci-ratchet", 800, "GEODE / A passing check is not merge authority",
                  "Regression checks constrain the change; admission binds it to the current PR and approval.",
                  "Developer scope and shared instructions guide a worktree change with regression tests. CI failure returns evidence to the coding agent. A passing revision still needs current head/base checks and authorized review before develop and main promotion.",
                  "", edges, nodes, "CI ratchet: code and contract invariants. Experimental KEEP: a candidate verdict. Neither grants release permission.")


def geode_runtime():
    background = rect(268, 332, 980, 288, "boundary") + rect(380, 480, 844, 124, "zone")
    edges = "".join(
        f'<path d="M{x} 228V704" fill="none" stroke="var(--rule)" stroke-dasharray="6 6"/>'
        for x in (124, 432, 808, 1136)
    ) + "".join((
        rect(428, 284, 8, 400, "zone"), rect(804, 396, 8, 56, "zone"), rect(1132, 536, 8, 48, "zone"),
        path("M124 284H428"), path("M436 396H804"), path("M804 452H436", "control"),
        path("M436 536H1132"), path("M1132 584H436", "control"), path("M428 684H124", "control"),
    ))
    nodes = "".join((
        box(32, 152, 184, 76, "User"), box(292, 152, 280, 76, "AgenticLoop"),
        box(680, 152, 256, 76, "Tool / environment"), box(1024, 152, 224, 76, "Verifier"),
        label(272, 272, 272, "goal + session state"), text(288, 356, "REPEAT / until completion or a stopping condition", "section"),
        label(616, 384, 160, "tool call"), label(616, 440, 248, "observation / error"),
        text(396, 504, "ONLY WHEN REQUIRED BY THE RUN CONTRACT", "section"),
        label(784, 524, 184, "candidate result"), label(784, 572, 232, "verdict + evidence"),
        label(272, 672, 272, "result + execution trace"),
    ))
    return figure("geode-runtime", 784, "GEODE / One execution, distinct records",
                  "Context assembly and compaction belong to the runtime; verification follows the run contract.",
                  "Time runs downward across User, AgenticLoop, Tool/environment and Verifier lifelines. The loop calls tools and receives observations or errors. Contract-required verification returns a verdict and evidence. The final result and execution trace return to the user.",
                  background, edges, nodes, "Completion statement ≠ verifier verdict ≠ termination reason. Solid: call. Dashed: response.")


def harbor_rollout():
    background = rect(32, 292, 584, 184, "boundary") + rect(664, 292, 584, 184, "boundary")
    edges = "".join((
        path("M640 240V264H324V292"), path("M640 264H956V292"),
        path("M340 400H384"), path("M972 400H1016"),
        path("M200 448V504H352V564", "observe"), path("M832 448V504H352", "observe", False),
        path("M488 448V528H688V564", "observe"), path("M1120 448V528H688", "observe", False),
        path("M792 620H856"), path("M1052 676V708H412V744"), path("M792 788H856"),
    ))
    nodes = "".join((
        box(32, 144, 1216, 96, "Harbor / trial lifecycle", "Frozen run spec · separate environments · agent timeout · task-native verifier", focus=True),
        text(56, 324, "GEODE / independent trial container", "section"),
        text(688, 324, "CODEX / independent trial container", "section"),
        box(56, 348, 284, 100, "AgenticLoop", "One terminal_exec tool"),
        box(384, 348, 208, 100, "Task verifier", "Result · reward"),
        box(688, 348, 284, 100, "Native Codex", "CLI execution"),
        box(1016, 348, 208, 100, "Task verifier", "Result · reward"),
        box(32, 564, 760, 112, "Private raw jobs / preserve original evidence", "config · result · trajectory · verifier outputs", "Original and supplemental attempts retain their lineage."),
        box(856, 564, 392, 112, "Publication checks", "Normalize · select by contract", "Schema · hashes · privacy"),
        box(32, 744, 760, 88, "geode-eval-artifacts", "Append-only public derivatives + publication manifest"),
        box(856, 744, 392, 88, "Replay / docs", "Derived views, not score authority"),
    ))
    return figure("harbor-rollout", 912, "Harbor / Independent trials, traceable evidence",
                  "89 tasks × 5 repetitions × 2 arms = 890 planned cells, not 890 valid completed trials.",
                  "The frozen run spec controls Harbor. GEODE and native Codex use independent containers and separate task-verifier runs. Raw actions and verifier outputs remain private; normalization, selection, hash and privacy checks admit public derivatives. Replay is derived evidence, not a replacement for result authority.",
                  background, edges, nodes, "Branches mean independent arms, not simultaneous execution. Score authority: task verifier + frozen selection rules.")


def eco2_build():
    edges = "".join((
        path("M352 216H416"), path("M720 216H784"), path("M1016 268V348"),
        path("M784 408H568V268", "control"), path("M896 456V504H160V572"),
        path("M1120 456V528H496V572"), path("M640 624H696"), path("M928 624H984"),
        path("M160 676V728H1116V676", "control"),
    ))
    nodes = "".join((
        box(32, 160, 320, 108, "Developer + scaffold", "Scope · review · Skills", "CLAUDE.md · SDK checks"),
        box(416, 160, 304, 108, "Claude Code", "Development-side agent"),
        box(784, 160, 464, 108, "Code + manifests", "apps/ · workloads/"),
        box(784, 348, 464, 108, "GitHub Actions", "Changed-service format · lint · tests", focus=True),
        box(32, 572, 256, 104, "Container image", "Docker Hub"),
        box(348, 572, 292, 104, "Git manifests", "Versioned image tag"),
        box(696, 572, 232, 104, "ArgoCD", "ApplicationSet"),
        box(984, 572, 264, 104, "Cluster rollout", "Desired state"),
        label(632, 408, 264, "failure evidence → correction"),
        label(160, 548, 144, "build / push"), label(496, 560, 184, "update image tag"),
        label(632, 728, 160, "image pull"),
        text(32, 356, "Different responsibilities", "section"), text(32, 392, "Developer: scope and code review."),
        text(32, 428, "CI: quality checks; ArgoCD: reconcile Git."),
        text(32, 480, "Image publication requires an eligible push / manual build.", "small"),
    ))
    return figure("eco2-build", 816, "Eco² / From a reviewed change to a rollout",
                  "Coding-agent work, CI checks and ArgoCD reconciliation have different owners.",
                  "Developer scope and project scaffolding guide Claude Code changes. CI checks changed services. Eligible builds publish images and update Git image tags; ArgoCD applies manifests and the cluster pulls images. Failure evidence returns to the coding agent, not an autonomous CI code-editing mechanism.",
                  "", edges, nodes, "This is an artifact and responsibility map, not a mandatory sequence for every change or proof of universal CI coverage.")


def eco2_scan():
    background = rect(328, 152, 920, 224, "boundary")
    edges = "".join((
        path("M280 276H352"), path("M544 276H584"), path("M776 276H816"), path("M1008 276H1048"),
        path("M448 336V416H172V500", "observe"), path("M680 336V416H448", "observe", False),
        path("M912 336V416H680", "observe", False), path("M1136 336V416H912", "observe", False),
        path("M312 556H368"), path("M648 556H704"), path("M984 556H1040"),
    ))
    nodes = "".join((
        text(32, 188, "REQUEST / ACCEPT", "section"),
        box(32, 216, 248, 120, "Scan API", "Register chain", "202 + job_id"),
        text(352, 188, "TASK EXECUTION / RabbitMQ · Celery chain", "section"),
        box(352, 216, 192, 120, "Vision", "Image", "classification"),
        box(584, 216, 192, 120, "Rule", "Regulations", "Lite RAG"),
        box(816, 216, 192, 120, "Answer", "Disposal", "guidance"),
        box(1048, 216, 176, 120, "Reward", "Character", "grant / store"),
        label(700, 416, 408, "Each stage writes progress events with XADD"),
        text(32, 468, "PROGRESS DELIVERY / separate from the worker lifetime", "section"),
        box(32, 500, 280, 112, "Redis Streams", "Stage events", "Consumer group"),
        box(368, 500, 280, 112, "Event Router", "Process → publish", "ACK only on success", focus=True),
        box(704, 500, 280, 112, "Pub/Sub → SSE", "Live delivery", "Separate connection"),
        box(1040, 500, 208, 112, "Client", "Progress", "Result"),
        text(32, 656, "Recovery", "section"), text(160, 656, "Pending entries → reclaim. State KV + Streams → reconnect / catch-up."),
        text(160, 692, "Pub/Sub is live transport, not the recovery log.", "small"),
    ))
    return figure("eco2-scan", 776, "Eco² / The job outlives its SSE connection",
                  "Task queues move work; a separate event path reports how that work is progressing.",
                  "The Scan API registers a Celery chain and returns 202 plus a job ID. RabbitMQ queues connect Vision, Rule, Answer and character Reward stages. Every stage emits Redis Stream events. Event Router publishes to Pub/Sub and SSE independently of worker execution. ACK-on-success preserves pending entries for recovery.",
                  background, edges, nodes, "Solid: work / delivery. Dotted: stage events. Reward grants service characters; it is not a benchmark score.")


def eco2_chat():
    edges = "".join((
        path("M288 268H328"), path("M536 268H568V196H608"),
        path("M568 268V324H608"), path("M568 324V452H608"),
        path("M944 196H972V452H944", arrow=False), path("M944 324H972", arrow=False),
        path("M972 336H1000"),
        path("M1124 400V576"), path("M1000 632H944", "control"),
    ))
    nodes = "".join((
        text(32, 144, "Chat API → RabbitMQ → TaskIQ worker / LangGraph", "section"),
        box(32, 212, 256, 112, "Intent classifier", "Optional Vision"),
        diamond(432, 268, 208, 136, "Router", "Send"),
        box(608, 152, 336, 88, "Domain nodes", "Waste RAG · character"),
        box(608, 280, 336, 88, "API / tool nodes", "Location · weather · search"),
        box(608, 408, 336, 88, "Image generation", "Separate selected branch"),
        box(1000, 268, 248, 132, "Join + prepare", "Aggregator", "Optional compaction", focus=True),
        box(1000, 576, 248, 112, "Answer", "Token events", "To Event Router / SSE"),
        box(608, 576, 336, 112, "Optional Eval", "Grading", "Bounded regeneration"),
        text(32, 420, "Choose, do not broadcast", "section"),
        text(32, 456, "One or more branches run."), text(32, 492, "The join checks required context."),
        text(32, 544, "Structured / function calls select arguments;", "small"),
        text(32, 568, "application commands perform the work.", "small"),
        label(972, 556, 176, "when configured"),
        rect(32, 748, 1216, 100, "zone"), text(52, 780, "CONVERSATION STATE", "section"),
        text(52, 816, "Redis checkpoint → asynchronous syncer → PostgreSQL; message persistence uses a separate consumer."),
    ))
    return figure("eco2-chat", 936, "Eco² / Select the work, then join its results",
                  "Intent and request context determine the active branches, not a fixed broadcast to every node.",
                  "Chat uses a TaskIQ worker running LangGraph. Intent and optional Vision guide Send dispatch into selected domain, API/tool or image-generation nodes. The aggregator checks required context before optional compaction and streamed answering. Eval is configuration-dependent and bounded. Checkpoints and stored messages have separate persistence paths.",
                  "", edges, nodes, "Only selected branches execute. Optional Eval is not unlimited retry or an unrestricted multi-agent ReAct loop.")


def eco2_observe():
    background = rect(32, 204, 248, 384, "zone") + rect(32, 624, 248, 104, "zone")
    edges = "".join(path(f"M280 {y}H360", "observe") + path(f"M880 {y}H932", "observe")
                    for y in (256, 396, 536, 676))
    nodes = "".join((
        text(32, 164, "PRODUCER", "section"), text(360, 164, "COLLECT / RETAIN / QUERY", "section"),
        text(948, 164, "INVESTIGATION", "section"),
        text(52, 248, "API / workers", "name"), text(52, 284, "Envoy", "name"),
        text(52, 356, "Metrics"), text(52, 392, "stdout / stderr"), text(52, 428, "Request spans"),
        text(52, 664, "Chat LangGraph", "name"), text(52, 700, "LLM / tool calls"),
        box(360, 204, 520, 104, "Prometheus → Grafana", "Alertmanager · Kiali / mesh topology"),
        box(360, 344, 520, 104, "Fluent Bit → Elasticsearch", "Kibana / structured log search"),
        box(360, 484, 520, 104, "OpenTelemetry → Jaeger", "Request spans / sampled traces"),
        box(360, 624, 520, 104, "LangSmith", "Node timing · token usage · errors"),
        text(948, 244, "Queue / Pod pressure", "name"), text(948, 280, "Backlog versus capacity"),
        text(948, 384, "Failure context", "name"), text(948, 420, "Search the failing event"),
        text(948, 524, "Request path", "name"), text(948, 560, "Locate a slow / failed span"),
        text(948, 664, "LLM-node execution", "name"), text(948, 700, "Model or tool wait?"),
        text(32, 772, "Istio sampling: 50%. LangSmith and LangGraph → OTel require tracing configuration.", "small"),
    ))
    return figure("eco2-observability", 856, "Eco² / Read the record that matches the failure",
                  "A queue, a failed request and a slow model call leave different evidence.",
                  "APIs, workers and Envoy emit operational metrics, logs and request spans. Prometheus, Fluent Bit/Elasticsearch and OpenTelemetry/Jaeger serve different investigations. LangGraph's configured LangSmith path records LLM-node execution. Collection paths do not establish complete trace coverage or an answer-quality verdict.",
                  background, edges, nodes, "Dotted: observation path. These are collection responsibilities, not a claim that every request retained a trace.")


def eco2_improvement():
    background = "".join(rect(x, 152, w, 668, "zone") for x, w in ((32, 352), (456, 352), (880, 368)))
    edges = "".join((
        path("M360 284H480"), path("M632 340V448"), path("M784 504H904"),
        path("M1064 560V672"), path("M904 732H844V612H208V672"),
        path("M360 732H480"), path("M632 792V832H416V504H480", "control"),
    ))
    nodes = "".join((
        text(56, 188, "REPRODUCE / MEASURE", "section"),
        text(480, 188, "HUMAN + CODING AGENT", "section"), text(904, 188, "CI / DELIVERY", "section"),
        box(56, 228, 304, 112, "Reproduce failure", "Workload + pressure", "Metrics · logs · traces"),
        box(480, 228, 304, 112, "Bottleneck hypothesis", "Falsifiable explanation", "Expected signal change"),
        box(480, 448, 304, 112, "Small diff + contract", "Code / manifest change", "A check for recurrence"),
        box(904, 448, 320, 112, "Accepted revision", "CI checks + review", "Git → ArgoCD"),
        box(904, 672, 320, 120, "Kubernetes", "Reconcile desired state", "Rerun the workload"),
        box(56, 672, 304, 120, "Same workload", "Measure the same signals", "New evidence"),
        box(480, 672, 304, 120, "Human verdict", "Keep / revise / revert", "Compare before and after", focus=True),
        label(720, 612, 240, "repeat under the change"),
        text(56, 448, "A failure becomes", "name"), text(56, 480, "a testable contract.", "name"),
        text(56, 528, "ACK / recovery / probe behavior", "small"),
        text(904, 268, "Checks admit a revision.", "body"),
        text(904, 304, "They do not prove the fix.", "body"),
        label(416, 832, 200, "revise the contract"),
    ))
    return figure("eco2-improvement", 920, "Eco² / Turn a failure into a testable change",
                  "The same workload connects a bottleneck hypothesis to the decision to keep, revise or revert.",
                  "Responsibility lanes separate reproduction and observation, human/coding-agent diagnosis and changes, and CI/delivery. A reviewed, checked revision reaches Kubernetes through Git and ArgoCD. Repeating the workload produces new evidence. The human owns the final decision, not the telemetry system or production runtime.",
                  background, edges, nodes, "External engineering process, not runtime self-modification. The developer-written case table below supplies the evidence.")


def experiment_gate():
    edges = "".join((
        path("M156 236V288"), path("M280 336H320"), path("M528 336H624"), path("M944 336H1056"),
        path("M424 416V544"), path("M784 432V544"),
        path("M156 384V740", "observe"), path("M424 644V740", "observe"),
        path("M784 644V740", "observe"), path("M1152 384V740", "observe"),
    ))
    nodes = "".join((
        box(32, 148, 1216, 88, "Frozen Baseline + candidate", "Content-bound task pack · evaluator / harness identity · budget · paired comparison rule"),
        box(32, 288, 248, 96, "Evaluation", "Revision-bound run"),
        diamond(424, 336, 208, 160, "Valid", "execution?"),
        diamond(784, 336, 320, 192, "Gain beyond", "uncertainty and", "no critical veto?"),
        box(1056, 288, 192, 96, "KEEP", "Next Baseline", focus=True),
        box(312, 544, 224, 100, "INVALID", "Baseline unchanged"),
        box(624, 544, 320, 100, "REJECT", "Baseline unchanged"),
        box(32, 740, 1216, 104, "Ledger / every attempt and verdict", "Revision · raw evidence · lineage · validity · selection reason"),
        label(576, 324, 56, "yes"), label(1000, 324, 56, "yes"),
        label(424, 484, 48, "no"), label(784, 484, 48, "no"),
        label(156, 660, 136, "raw evidence"),
    ))
    return figure("experimental-admission", 928, "Experimental Loop / A score gain is not enough",
                  "The Ratchet admits a candidate only after validity, uncertainty and veto checks.",
                  "A frozen baseline/candidate comparison is evaluated. Invalid execution retains the baseline. Valid execution is rejected if its gain does not exceed uncertainty or a critical veto is present. Only KEEP adopts a next baseline. The ledger retains raw evidence and every outcome.",
                  "", edges, nodes, "KEEP is an experiment verdict, not PR merge, deployment approval or evidence of sustained self-improvement.")


DIAGRAMS = {
    "geode-overview": geode_overview,
    "geode-ci-ratchet": geode_ci,
    "geode-runtime": geode_runtime,
    "harbor-rollout": harbor_rollout,
    "eco2-build": eco2_build,
    "eco2-scan": eco2_scan,
    "eco2-chat": eco2_chat,
    "eco2-observability": eco2_observe,
    "eco2-improvement": eco2_improvement,
    "experimental-admission": experiment_gate,
}


def validate_svg(svg):
    root = ET.fromstring(svg)
    ns = {"s": "http://www.w3.org/2000/svg"}
    assert root.tag == "{http://www.w3.org/2000/svg}svg"
    assert root.find("s:title", ns).text and root.find("s:desc", ns).text
    ids = [element.attrib["id"] for element in root.iter() if "id" in element.attrib]
    assert len(ids) == len(set(ids)), "duplicate SVG ID"
    for ref in re.findall(r"url\(#([^)]*)\)", svg):
        assert ref in ids, f"missing marker: {ref}"
    for ref in root.attrib["aria-labelledby"].split():
        assert ref in ids, f"missing accessible description: {ref}"
    assert not root.findall(".//s:script", ns)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail on generated-asset drift")
    args = parser.parse_args()
    stale = []
    for name, render in DIAGRAMS.items():
        svg = render()
        validate_svg(svg)
        destination = ASSETS / f"{name}.svg"
        if args.check:
            if not destination.exists() or destination.read_text(encoding="utf-8") != svg:
                stale.append(destination.name)
        else:
            destination.write_text(svg, encoding="utf-8")
    if stale:
        parser.exit(1, "Stale diagram assets: " + ", ".join(stale) + "\n")
    print(f"{'Checked' if args.check else 'Rendered'} {len(DIAGRAMS)} fixed-layout diagrams.")


if __name__ == "__main__":
    main()
