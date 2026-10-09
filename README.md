# Shawdai Marie

I build AI infrastructure for reliable, accountable agent systems: policy checks before execution, reproducible evaluations, and audit records that others can verify.

My focus is **AI infrastructure engineering, supported by research and technical writing**. I work in Python, Go, TypeScript, and SQL, and document the architecture, tradeoffs, and limits so another engineer can inspect, run, and maintain the system.

## Principles, and where they are enforced

A principle that nothing enforces is only a preference. Each one below is backed by code or a check that you can inspect and run.

| Principle | In practice | Enforced in |
|---|---|---|
| **Evidence over assertion** | A claim links to a test, a workflow run, or a verifiable record. | Sentinel's [deterministic evaluator](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION.md) and [CI evidence](https://github.com/Shawdaimarie/sentinel/actions) |
| **Fail closed** | When a check cannot decide, the answer is no. | [Aegis](https://github.com/Shawdaimarie/sentinel/tree/main/Aegis) denies on missing identity, stale policy, missing approval, or audit failure |
| **Safety is never averaged away** | A strong overall score cannot hide a single safety failure. | Sentinel's hard safety gates and baseline regression checks |
| **Least privilege** | Each component gets only the access its task needs. | Aegis capability tokens scoped to tool, action, and resource; role-separated database credentials in [evaluation history](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION_HISTORY.md) |
| **People keep authority** | Consequential actions need a recorded human decision. | Aegis approval requirements; Article's *Human Oversight for AI* check |
| **Verifiable by anyone, anywhere** | Checks run offline, without vendor accounts, in more than one language. | Audit-chain [verifiers in Python, TypeScript, and Go](https://github.com/Shawdaimarie/sentinel/tree/main/Sentinel/verifiers); [offline trace fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures) |
| **State the limits** | Every project says what it does not establish. | Sentinel's [scope and limits](https://github.com/Shawdaimarie/sentinel#scope-and-limits); Aegis [threat model](https://github.com/Shawdaimarie/sentinel/blob/main/Aegis/docs/THREAT_MODEL.md) |
| **Built to last** | Versioned specifications, recorded history, and reviewed dependency updates. | Article's *Dependency Integrity* and *Sustainability & Longevity* checks; Sentinel's [portable audit spec](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/spec/SPEC.md) |

## Work

### [Sentinel](https://github.com/Shawdaimarie/sentinel) · Python · Go · TypeScript · SQL

A reference platform for governed agent execution and reproducible evaluation.

- Evaluates proposed agent actions against policy before they are dispatched.
- Normalizes OpenTelemetry traces into evaluation records.
- Compares candidate and baseline runs with explicit safety and regression gates.
- Verifies tamper-evident audit chains independently in three languages.
- Stores evaluation history in PostgreSQL with least-privilege roles.
- Includes **Aegis**, a Go authorization gateway. Aegis decides whether a workload identity may use a tool, action, and resource, and it denies whenever it cannot decide.

**Start here:** [Quick start](https://github.com/Shawdaimarie/sentinel#trace-to-evaluation-quick-start) · [Architecture](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/ARCHITECTURE.md) · [Security model](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/SECURITY.md) · [Reviewer path](https://github.com/Shawdaimarie/sentinel#reviewer-path)

### [Article](https://github.com/Shawdaimarie/article-) · Python

A machine-readable charter of ten engineering principles, and a CLI that checks a project against them. The principles include transparency, security, privacy, accessibility, and human oversight of AI. It can gate CI on a minimum score, and it never executes code from the project it checks.

### [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures) · Python

Synthetic OpenTelemetry traces for testing AI-agent trace importers, covering topology errors and sensitive-data handling. No API keys, network access, or production data are needed.

### Learning and interfaces

| Project | Focus |
|---|---|
| [CS–AI Path](https://github.com/Shawdaimarie/cs-ai-path) | A structured, self-paced path from computer-science fundamentals to modern AI, using free resources |
| [Nyx Market Dashboard](https://github.com/Shawdaimarie/nyx-market-dashboard) | A browser-based market research and decision interface in HTML, CSS, and JavaScript |

## Technical writing

Three starting points for reviewing the engineering decisions behind the code:

| Question | Read | What it covers |
|---|---|---|
| How should agent behavior be evaluated reproducibly? | [Deterministic agent evaluation protocol](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION.md) | Observable assertions, safety gates, baseline comparisons, and recorded run artifacts |
| What can a tamper-evident audit chain actually prove? | [Portable audit-chain specification](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/spec/SPEC.md) | A versioned verification contract, independent implementations, and explicit limits on deletion and truncation detection |
| Where does an authorization system place its trust? | [Aegis threat model](https://github.com/Shawdaimarie/sentinel/blob/main/Aegis/docs/THREAT_MODEL.md) | Trust boundaries, workload identity, scoped capabilities, approval requirements, and fail-closed decisions |

These documents connect design choices to inspectable contracts and controls. Read the stated assumptions and limits alongside the implementation.

## Current priorities

- Complete and verify a successful Sentinel container release through the vulnerability gate, with signed build provenance and a software bill of materials tied to the image digest.
- Publish reproducible studies of evaluation quality, latency, and cost, with explicit baselines, failure cases, and limits.
- Make every project installable, reproducible, and verifiable by someone who has never spoken to me.
- Contribute tested fixes to the open-source tools these projects depend on.

## Scope

These are reference implementations. Their tests and controls show the behavior they cover. They do not establish universal safety, certification, or production readiness for every use case.

Want to reproduce an example or report a problem? Start with the repository's documentation and contribution guide. Please report security findings privately, following each repository's security policy.

[Portfolio](https://essentialdigitalsolution.com/) · [All repositories](https://github.com/Shawdaimarie?tab=repositories) · [Codeforces](https://codeforces.com/profile/Shawdaimarie) · [LeetCode](https://leetcode.com/u/Shawdaimarie/) · [CodeChef](https://www.codechef.com/users/plush_rain_95)
