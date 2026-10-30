# Shawdai Marie

**Software & AI Systems Engineer | Agent Evaluation, Runtime Infrastructure & Security**

I turn ideas into working systems—writing the code, shaping agent behavior, and making complex technology clear.

My work connects software engineering and technical writing through AI-agent execution, evaluation, and developer tools. I develop reference implementations with explicit system boundaries, reproducible checks, and documentation that explains how the code works and where its limits lie.

## Engineering focus

I focus on three practical challenges in building and reviewing AI-agent systems:

| Engineering challenge | Implemented approach | Evidence |
|---|---|---|
| A candidate AI change may regress required behavior | [Sentinel evaluation gates](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/src/sentinel/evaluation.py) compare candidate and baseline runs and keep safety failures explicit | Case-level results, regression decisions, and reproducible evaluation artifacts |
| A tool action may exceed its permitted scope | [Aegis authorization](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Aegis/internal/aegis/authorizer.go) checks identity, policy, and access conditions | Allow/deny decisions with audit evidence and documented trust boundaries |
| Trace data may be incomplete, ambiguous, or malformed | [Python trace checks](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tracecheck.py) use synthetic fixtures, explicit identities, and stable diagnostics | Reproducible failure cases with expected results and source fingerprints |

Each implementation links the engineering decision to source code and reviewable results.

## Explore my work

| Area | Start here | What to look for |
|---|---|---|
| Coding and debugging | [Trace checker](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tracecheck.py) and [regression tests](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tests/test_tracecheck.py) | Bounded input handling, span identity, parent relationships, and deliberate failure cases |
| Technical writing | [Reviewing an AI-agent trace importer with synthetic fixtures](docs/trace-importer-review.md) | A runnable walkthrough, expected output, diagnostic interpretation, and explicit limits |
| Deployment and handoff | [Sentinel installation guide](https://github.com/Shawdaimarie/sentinel/blob/main/INSTALLING.md) and [first-run guide](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/FIRST_RUN.md) | Setup instructions and checks for someone approaching the project for the first time |

The trace walkthrough records a local Python 3.12.14 run on October 12, 2026: nine fixture expectations matched and eight unit tests passed. These are synthetic checks, with the source revision and limitations recorded in the guide.

## Selected projects

**Start with [Sentinel’s reviewer path](https://github.com/Shawdaimarie/sentinel#reviewer-path)** for architecture, code, tests, and example evidence. For a smaller project you can inspect offline, start with [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures).

### [Sentinel](https://github.com/Shawdaimarie/sentinel) · Python · Go · TypeScript · SQL

A reference platform for governed agent execution and reproducible evaluation.

- Evaluates proposed agent actions against policy before they are dispatched.
- Normalizes OpenTelemetry traces into evaluation records.
- Compares candidate and baseline runs with explicit safety and regression gates.
- Includes separate audit-chain verification implementations in three languages.
- Stores evaluation history in PostgreSQL with least-privilege roles.
- Includes **Aegis**, a Go authorization gateway that checks whether a workload identity may use a specified tool, action, and resource. Unresolved authorization decisions are denied.

**Start here:** [Quick start](https://github.com/Shawdaimarie/sentinel#trace-to-evaluation-quick-start) · [Architecture](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/ARCHITECTURE.md) · [Security model](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/SECURITY.md) · [Reviewer path](https://github.com/Shawdaimarie/sentinel#reviewer-path)

### [Article](https://github.com/Shawdaimarie/article-) · Python

A machine-readable charter of ten engineering principles with a command-line tool for checking projects against them. It covers transparency, security, privacy, accessibility, and human oversight of AI. The tool supports a minimum-score CI gate and inspects projects without executing their code. Its static checks support human review; they do not constitute a security or legal audit.

### [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures) · Python

Synthetic OpenTelemetry traces for testing AI-agent trace importers, covering topology errors and sensitive-data handling. No API keys, network access, or production data are needed.

### Creative tools and learning

| Project | Focus |
|---|---|
| [CS–AI Path](https://github.com/Shawdaimarie/cs-ai-path) | A structured, self-paced path from computer-science fundamentals to modern AI, using free resources |
| [Nyx Market Dashboard](https://github.com/Shawdaimarie/nyx-market-dashboard) | A browser-based market research and decision interface in HTML, CSS, and JavaScript |

## Technical writing

Writing is part of my engineering process. These guides explain the decisions, contracts, and tradeoffs behind the implementation:

| Question | Read | What it covers |
|---|---|---|
| How should agent behavior be evaluated reproducibly? | [Deterministic agent evaluation protocol](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION.md) | Observable assertions, safety gates, baseline comparisons, and recorded run artifacts |
| What can a tamper-evident audit chain actually prove? | [Portable audit-chain specification](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/spec/SPEC.md) | A versioned verification contract, independent implementations, and explicit limits on deletion and truncation detection |
| Where does an authorization system place its trust? | [Aegis threat model](https://github.com/Shawdaimarie/sentinel/blob/main/Aegis/docs/THREAT_MODEL.md) | Trust boundaries, workload identity, scoped capabilities, approval requirements, and fail-closed decisions |

Each document connects the design to source code, explicit assumptions, and practical review steps.

## Evaluation results: trace-review reliability

A pinned baseline and a repaired Python checker were replayed against **20 labeled synthetic cases**, with acceptance criteria committed before the published measurement.

| Acceptance measure | Baseline | Candidate |
|---|---:|---:|
| Exact diagnostic agreement | 12/20 | **20/20** |
| False accepts on eight malformed-sibling cases | 8 | **0** |
| False alarms on six valid controls | 0 | **0** |
| Original fixture expectations matched | 9/9 | **9/9** |

The candidate met all technical acceptance criteria, produced stable diagnostics across 100 repeated batches, and passed 16 unit test methods. The intended benefit is more reliable trace review. These synthetic cases target a known defect; production accuracy, review-time savings, customer acceptance, and financial impact remain unmeasured.

[Results and reproduction](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/748b9e2b61831ebf4b22057b2cf582d06ecd8894/pilots/trace-container-v1/README.md) · [Baseline and acceptance protocol](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/906d40859e2e846eac2e892924adaec2459d89f3/pilots/trace-container-v1/PROTOCOL.md) · [Raw evidence](https://github.com/Shawdaimarie/agent-trace-fixtures/tree/748b9e2b61831ebf4b22057b2cf582d06ecd8894/pilots/trace-container-v1/results/2026-10-23) · [Pull request #2](https://github.com/Shawdaimarie/agent-trace-fixtures/pull/2)

These automated results provide a reproducible starting point for independent review.

## Benchmark results: offline evaluation

Sentinel's [October 14 offline benchmark](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/docs/benchmarks/OFFLINE_2026-10-14.md) records a bounded synthetic workload, predeclared acceptance criteria, and archived raw logs:

| Result | Conditions and evidence |
|---|---|
| **2,606 validated batches in approximately five minutes** | Two workers, 120 synthetic evaluation records per batch; **8.684 batches/s**, approximately **1,042 fixture evaluations/s** |
| **All seven normal stages passed, through eight concurrent workers** | Within the protocol's latency, error, and memory criteria; no unexpected errors in the recorded normal stages |
| **10 deliberate input rejections followed by 10 successful recovery batches** | Missing or malformed local files; seeded outputs preserved on rejection |

The benchmark used an installed wheel on Python 3.12.14 and a shared macOS arm64 desktop. Results apply to **offline fixture evaluation** under those conditions; production capacity and customer outcomes were not measured. The [published summary, raw log, and SHA-256 fingerprints](https://github.com/Shawdaimarie/sentinel/tree/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/benchmarks/results/2026-10-14-offline-v1/) support inspection; [capacity-testing instructions](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/docs/CAPACITY_TESTING.md) explain reproduction. Independent reproduction remains outstanding.

## Languages in practice

Explore how I use each language in published implementations. The links show specific areas of work rather than a proficiency ranking.

| Language | Published implementation | What a reviewer can inspect |
|---|---|---|
| **Python** | [Trace checker](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tracecheck.py) and [Sentinel importer](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/src/sentinel/trace_import.py) | Bounded input handling, trace identities, topology checks, and evaluation records |
| **TypeScript** | [Portable audit verifier](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/verifiers/typescript/src/verifier.ts) | Typed JSON validation, safe integer constraints, and audit-chain verification |
| **JavaScript** | [Nyx dashboard source](https://github.com/Shawdaimarie/nyx-market-dashboard/blob/34c9502146a681d7f34e2ce30ec4f9ad1c88132d/market-dashboard.html) | DOM rendering and event handling in a browser interface; live integrations require separate validation |
| **SQL** | [PostgreSQL history schema](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Sentinel/src/sentinel/migrations/001_history.sql) | Relational keys, constraints, evaluation history, and data integrity |
| **Go** | [Aegis authorizer](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/Aegis/internal/aegis/authorizer.go) | Policy decisions, scoped authorization, denial paths, and audit integration |
| **Bash** | [Container smoke checks](https://github.com/Shawdaimarie/sentinel/blob/3b2e7cf0716e3940ef5f8af7beb0177408afe333/scripts/smoke-image.sh) | Failure propagation, cleanup, and packaged-behavior checks with synthetic inputs |

The [language development plan and engineering standard](docs/engineering-standard.md) distinguish supported implementation areas from future learning targets.

## Professional context

My résumé describes implementation, evaluation, and technical handoff within a practice spanning **120+ client mandates across eight sectors**. It also records **ORACLE workflow validation across 14 client environments** and a brief-to-publication pipeline supporting campaigns that generated **more than one million audience engagements**.

These résumé-reported figures describe client delivery and audience engagement. They are separate from the repository benchmarks and do not measure software performance or financial impact.

## Validation and next steps

The published work consists of reference implementations supported by synthetic fixtures and offline measurements. Independent reproduction and production validation remain outstanding. The next step is an authorized workflow pilot with a recorded baseline, operating costs, and user acceptance criteria. Claims about customer savings, revenue, or adoption will require separate evidence.

Development and documentation are AI-assisted. I remain responsible for reviewing changes, checking results, and explaining my contributions. Automated checks cover the documented cases; independent assessment of my ability to explain and modify the work remains separate. The projects do not claim universal safety, certification, or production readiness.

I welcome reproducible failure reports, independently checked results, and tested interoperability improvements. Follow each repository’s documentation and contribution guide, and report security findings privately through its security policy.

[Portfolio](https://essentialdigitalsolution.com/) · [All repositories](https://github.com/Shawdaimarie?tab=repositories) · [Codeforces](https://codeforces.com/profile/Shawdaimarie) · [LeetCode](https://leetcode.com/u/Shawdaimarie/) · [CodeChef](https://www.codechef.com/users/plush_rain_95)
