# Reviewing an AI-agent trace importer with synthetic fixtures

An importer can parse JSON successfully and still lose a retry, connect a span to the wrong trace, or retain sensitive attributes. A useful review checks these behaviors separately, with expected results that another engineer can reproduce.

This walkthrough uses [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures), a small Python project with nine synthetic OTLP JSON fixtures. It is an offline reference exercise: it does not measure a production service or establish complete OpenTelemetry conformance.

## 1. Reproduce a known revision

Use Python 3.11 or newer. Fetching the repository requires network access; the checks themselves run offline without third-party Python packages, API keys, or production data.

```sh
git clone https://github.com/Shawdaimarie/agent-trace-fixtures.git
cd agent-trace-fixtures
git checkout c712de027af0812e927c3b9a5e8b4c669731b80c
python3 tracecheck.py
python3 -m unittest discover -s tests -v
```

At this revision, the corpus checker should report nine `PASS` lines and exit 0. The unit-test command should report eight passing tests. The [manifest](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/manifest.json) pairs each fixture with a content fingerprint and expected diagnostics.

The fingerprint answers whether the bytes changed. The expected diagnostic answers whether the observed behavior matches the declared contract. Neither substitutes for reviewing whether that contract is appropriate.

## 2. Read a passing negative case correctly

Consider these three outputs:

```text
PASS retry: valid-profile
PASS missing-parent: missing_parent
PASS parent-cycle: parent_cycle
```

All three expectations passed. Only the first has no diagnostic under this checker's profile. The other two passed because the checker detected the condition the fixture deliberately introduced.

| Case | Review question | Failure to look for in your importer |
| --- | --- | --- |
| Retry | Are the original attempt and its retry preserved as distinct spans? | Combining two attempts and hiding the failure |
| Missing parent | Does the importer represent incomplete exports according to its documented contract? | Silently discarding the child or inventing a parent |
| Parent cycle | Can parent traversal terminate and report a cycle? | Looping indefinitely or presenting a fabricated hierarchy |
| Duplicate span | Does repeated identity produce a deliberate outcome? | Overwriting one record without a diagnostic |

A missing parent can result from a partial export; it is not automatically invalid OTLP. Decide what your application retains, rejects, or flags, and test that choice explicitly.

The [implementation](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tracecheck.py) keys parent relationships by both trace ID and span ID. The [tests](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/tests/test_tracecheck.py) include a cross-trace parent case. This makes a useful review pair: inspect the identity rule, then inspect the regression that protects it.

## 3. Check redaction without mistaking absence for success

The sensitive fixture contains two exact synthetic markers. Running the output checker against that unredacted fixture is a deliberate negative control:

```sh
python3 check_redaction.py fixtures/sensitive-attributes.json
```

Expected result:

```text
FAIL: 2 exact synthetic markers remain
```

The command exits 1 and does not print the marker values. A real adapter test should run the importer, apply the intended redaction, and pass the resulting UTF-8 artifact to this checker.

There is a crucial limitation: an empty output file passes this marker check. Zero surviving markers does not prove that useful records survived. Pair the absence check with assertions about retained span count, trace/span identity, required fields, and the information the reader actually needs.

The [redaction checker](https://github.com/Shawdaimarie/agent-trace-fixtures/blob/c712de027af0812e927c3b9a5e8b4c669731b80c/check_redaction.py) detects known exact strings only. Encoded variants and unknown secrets are outside its scope; it is not a general redaction engine.

## 4. Record enough evidence to review the result

Keep the source revision, runtime version, commands, exit codes, observed output, and any adapter-specific assertions together. If a fixture changes, review both its content and expected outcome before updating the manifest. Automatically blessing new hashes would hide the very change the fingerprint is meant to reveal.

For this walkthrough, a local run on October 12, 2026 with Python 3.12.14 produced:

| Check | Observed result |
| --- | --- |
| Corpus expectations and fingerprints | 9 of 9 matched; exit 0 |
| Unit tests | 8 passed; exit 0 |
| Unredacted sensitive fixture | 2 exact markers detected; exit 1 |
| Empty-file control | 0 exact markers detected; exit 0 |

These are author-side synthetic checks, not an independent customer reproduction. The fixture profile does not cover every OTLP field, transport, encoding, or provider convention. Its input-size and span-count ceilings are implementation limits. Use it to make a small set of failure modes inspectable, then add tests for the actual adapter contract.

*Engineering note · Essential Digital Solution. Prepared with AI assistance; commands and observed results verified against the pinned public source.*
