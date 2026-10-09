# Shawdai Marie

I build AI infrastructure for reliable, accountable agent systems: policy checks before execution, reproducible evaluations, and audit records that others can verify.

My focus is **AI infrastructure engineering, supported by research and technical writing**. I work in Python, Go, TypeScript, and SQL, and document the architecture, tradeoffs, and limits so another engineer can inspect, run, and maintain the system.

## Selected engineering

**Start with [Sentinel’s reviewer path](https://github.com/Shawdaimarie/sentinel#reviewer-path)** for architecture, code, tests, and example evidence. For a smaller project you can inspect offline, start with [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures).


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

A machine-readable charter of ten engineering principles, and a CLI that checks a project against them. The principles include transparency, security, privacy, accessibility, and human oversight of AI. It can gate CI on a minimum score and reads the target project without executing its code. Its static checks are heuristics for human review, not a security or legal audit.

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

## Engineering principles

| Principle | How I put it into practice |
|---|---|
| **Evidence over assertion** | Define observable outcomes and compare candidate runs against a baseline. See the [evaluation protocol](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION.md). |
| **Bounded authority** | Check identity, scope, policy, and required approval before dispatch. See the [Aegis threat model](https://github.com/Shawdaimarie/sentinel/blob/main/Aegis/docs/THREAT_MODEL.md). |
| **Safety as a separate gate** | Keep safety failures visible rather than allowing an aggregate score to hide them. See [Sentinel’s evaluator](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/docs/EVALUATION.md). |
| **Independent verification** | Specify the audit format and provide verifiers in Python, TypeScript, and Go. See the [portable specification](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/spec/SPEC.md). |
| **Maintainability and honest limits** | Document contracts, review dependency changes, preserve version history, and distinguish checks from certification. See [Article’s charter and limitations](https://github.com/Shawdaimarie/article-). |

## Current priorities

- Complete and verify a successful Sentinel container release through the vulnerability gate, with signed build provenance and a software bill of materials tied to the image digest.
- Publish reproducible studies of evaluation quality, latency, and cost, with explicit baselines, failure cases, and limits.
- Make every project installable, reproducible, and verifiable by someone who has never spoken to me.
- Contribute tested fixes to the open-source tools these projects depend on.

## Scope

These are reference implementations. Their tests and controls show the behavior they cover. They do not establish universal safety, certification, or production readiness for every use case.

Useful contributions include a reproducible failure case, an independently checked result, or a tested interoperability fix. Start with the repository's documentation and contribution guide. Please report security findings privately, following each repository's security policy.

[Portfolio](https://essentialdigitalsolution.com/) · [All repositories](https://github.com/Shawdaimarie?tab=repositories) · [Codeforces](https://codeforces.com/profile/Shawdaimarie) · [LeetCode](https://leetcode.com/u/Shawdaimarie/) · [CodeChef](https://www.codechef.com/users/plush_rain_95)
