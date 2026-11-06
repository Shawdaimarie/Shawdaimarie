# Shawdai Marie

**Software Engineer | AI Engineering | Evaluation & Developer Tools**

I build reference implementations for AI-agent evaluation, scoped authorization, and trace validation. My work connects code, reproducible checks, and technical documentation so reviewers can inspect both the behavior and its limits.

**Seeking software and AI engineering roles.** Start with the code and evidence below.

[Portfolio](https://essentialdigitalsolution.com/) · [Repositories](https://github.com/Shawdaimarie?tab=repositories) · [Engineering standard](docs/engineering-standard.md)

## Start here: three code reviews

### 1. [Sentinel](https://github.com/Shawdaimarie/sentinel#reviewer-path)
**Python · Go · TypeScript · SQL**

A reference platform for governed agent execution and reproducible evaluation. Inspect candidate-versus-baseline evaluation gates, OpenTelemetry trace ingestion, PostgreSQL evaluation history, and portable audit-chain verification. Aegis, the Go authorization gateway, checks workload identity and scoped tool actions, with unresolved decisions denied.

[Reviewer path](https://github.com/Shawdaimarie/sentinel#reviewer-path) · [Architecture](https://github.com/Shawdaimarie/sentinel/blob/main/Sentinel/ARCHITECTURE.md) · [Threat model](https://github.com/Shawdaimarie/sentinel/blob/main/Aegis/docs/THREAT_MODEL.md)

### 2. [EDS Assurance](https://github.com/Shawdaimarie/eds-assurance)
**Python · REST APIs · SQLite · CI**

Evidence contracts and evaluation infrastructure for AI applications: versioned sources, citation permissions, exact-quote checks, scoped API access, audit records, and backup verification. Provider adapters for OpenAI, Anthropic, and xAI are implemented and tested with mocked HTTP responses.

**Scope:** the demonstration is synthetic; live provider inference is not verified in the published documentation. Exact quote matching does not establish answer truth. The hosted free portfolio demo has ephemeral storage.

[Source and setup](https://github.com/Shawdaimarie/eds-assurance#install-and-verify) · [Architecture](https://github.com/Shawdaimarie/eds-assurance/blob/main/docs/ARCHITECTURE.md) · [Verification record](https://github.com/Shawdaimarie/eds-assurance/blob/main/docs/VERIFICATION.md)

### 3. [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures)
**Python · Regression testing · OpenTelemetry**

An offline fixture corpus and reference checker for trace structure, span identities, parent relationships, and deliberate failure cases. Runs without API keys or production data.

A candidate repair in **[open, unmerged PR #2](https://github.com/Shawdaimarie/agent-trace-fixtures/pull/2)** improved exact diagnostic agreement from **12/20 to 20/20** on purpose-selected synthetic cases. This is a targeted regression result, not held-out or production accuracy. **[Draft PR #3](https://github.com/Shawdaimarie/agent-trace-fixtures/pull/3)** adds explicit evidence checks that remain active under optimized Python; it is also unmerged.

[Baseline checker](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tracecheck.py) · [Candidate results and reproduction](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/748b9e2b61831ebf4b22057b2cf582d06ecd8894/pilots/trace-container-v1/README.md) · [Review walkthrough](docs/trace-importer-review.md)

## Engineering in practice

- **AI evaluation:** explicit acceptance criteria, comparable baseline/candidate runs, failure analysis, and inspectable evidence.
- **Backend and security:** typed contracts, bounded inputs, scoped authorization, auditability, and documented trust boundaries.
- **Developer tooling:** Python checks, CLI workflows, tests, CI, and reproducible setup instructions.
- **Languages with linked implementation evidence:** Python, Go, TypeScript, JavaScript, SQL, and Bash. [Detailed language evidence and prior benchmarks](docs/profile-evidence-2026-11-06.md#languages-in-practice).

## Selected research: AI, neuroscience, and physics

These sources provide technical context and directions for further work:

- **MIT ABxLab:** controlled studies of how changes to an agent's environment affect its choices.
- **Caltech-led LeanDojo:** language-model theorem proving connected to Lean's executable proof environment.
- **Stanford HELM and CMU WebArena:** transparent, multidimensional model evaluation and outcome-based testing of interactive agents.
- **MIT neural-dynamics research and Caltech physics-informed neural operators:** concrete connections between dynamical systems, neuroscience-inspired models, physical constraints, and machine learning.

[Source-to-engineering map and limits](docs/research-foundations.md). These are other researchers' contributions, not claims of my enrollment, degree, affiliation, endorsement, or reproduction of their results. The neuroscience and physics references are research context, not capabilities implemented in these repositories.

## More work

[Article: engineering-principles CLI](https://github.com/Shawdaimarie/article-) · [CS–AI learning path](https://github.com/Shawdaimarie/cs-ai-path) · [Nyx market dashboard](https://github.com/Shawdaimarie/nyx-market-dashboard)

[Technical writing and detailed prior evidence](docs/profile-evidence-2026-11-06.md) · [Codeforces](https://codeforces.com/profile/Shawdaimarie) · [LeetCode](https://leetcode.com/u/Shawdaimarie/) · [CodeChef](https://www.codechef.com/users/plush_rain_95)

Development and documentation are **AI-assisted**. The published projects are reference implementations with synthetic or offline evidence; independent reproduction and production validation remain outstanding. I remain responsible for reviewing changes, checking results, and explaining my contributions.
