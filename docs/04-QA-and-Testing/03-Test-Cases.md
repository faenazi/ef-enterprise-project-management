# Test Cases and Execution Evidence

## Purpose

Define executable test cases and capture execution results, evidence, environment, build, defects, and retest outcomes without forcing multi-step tests into a single oversized table cell.

## Required Context

1. `docs/04-QA-and-Testing/01-QA-Strategy-and-Test-Plan.md`
2. `docs/04-QA-and-Testing/02-Test-Scenarios.md`
3. Relevant requirements, design, UI/UX, and backlog items

## AI Instructions

- Create test cases only for documented scenarios and expected behavior.
- Use one subsection per test case when steps or evidence are non-trivial.
- Keep expected and actual results separate.
- Never mark a case Passed without execution evidence or an explicit recorded result.
- Reference defects and retests rather than overwriting failed history.

## Test Case Index

| Test Case ID | Scenario ID | Test Case | Requirements | Backlog Items | Priority | Execution Status | Latest Result |
|---|---|---|---|---|---|---|---|
| TC-001 | TS-001 | {{TEST_CASE}} | {{FR_OR_NFR_IDS}} | {{BI_IDS}} | High | Not Run | N/A |

## Test Case Template

### TC-001 — {{TEST_CASE_NAME}}

| Field | Details |
|---|---|
| Scenario | TS-001 |
| Objective | {{OBJECTIVE}} |
| Requirements | {{FR_OR_NFR_IDS}} |
| Backlog Items | {{BI_IDS}} |
| Preconditions | {{PRECONDITIONS}} |
| Test Data | {{TEST_DATA_REFERENCE}} |
| Environment | {{ENVIRONMENT}} |
| Build / Version | {{BUILD_OR_VERSION}} |
| Tester | {{TESTER}} |
| Execution Date | {{DATE}} |

#### Steps

| Step | Action | Expected Result | Actual Result | Evidence Reference | Result |
|---|---|---|---|---|---|
| 1 | {{ACTION}} | {{EXPECTED_RESULT}} | {{ACTUAL_RESULT}} | {{EVIDENCE}} | Not Run |

#### Execution Summary

| Field | Value |
|---|---|
| Overall Result | Not Run / Passed / Failed / Blocked / Not Applicable |
| Defect References | {{DEFECT_IDS_OR_NONE}} |
| Retest Of | {{PREVIOUS_EXECUTION_OR_NONE}} |
| Notes | {{NOTES}} |

## Execution History

| Execution ID | Test Case ID | Date | Environment / Build | Result | Defects | Evidence | Tester |
|---|---|---|---|---|---|---|---|
| EXE-001 | TC-001 | {{DATE}} | {{ENVIRONMENT_AND_BUILD}} | {{RESULT}} | {{DEFECT_IDS}} | {{EVIDENCE}} | {{TESTER}} |

## Open Questions

| ID | Question | Related Test Case | Owner | Status |
|---|---|---|---|---|
| TCQ-001 | {{QUESTION}} | {{TC_ID}} | {{OWNER}} | Open |

## Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
