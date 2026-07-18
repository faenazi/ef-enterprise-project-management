# UAT and Defect Management

## Purpose

Plan and track business validation, participants, scenarios, test data, observations, defects, retesting, known limitations, and UAT outcomes. This document records review and readiness information without requiring a formal approval.

## Required Context

1. `docs/01-Requirements/02-Business-Requirements.md`
2. `docs/01-Requirements/03-System-Requirements.md`
3. `docs/01-Requirements/04-Delivery-Backlog.md`
4. `docs/04-QA-and-Testing/01-QA-Strategy-and-Test-Plan.md`
5. `docs/04-QA-and-Testing/02-Test-Scenarios.md`
6. `docs/04-QA-and-Testing/03-Test-Cases.md`

## AI Instructions

- Do not invent business participants, schedules, outcomes, or acceptance decisions.
- Distinguish planned UAT from executed UAT.
- Capture observations and defects with evidence and ownership.
- Do not convert silence or incomplete testing into acceptance.
- Use readiness recommendations instead of signatures or approval fields.

## 1. UAT Scope and Objectives

Describe the business processes, capabilities, roles, interfaces, data, reports, and release scope to be validated.

## 2. Participants and Responsibilities

| Role / Business Area | Participant | Responsibility | Scenarios | Availability / Notes |
|---|---|---|---|---|
| {{ROLE_OR_AREA}} | {{PARTICIPANT_OR_TBD}} | {{RESPONSIBILITY}} | {{TS_IDS}} | {{NOTES}} |

## 3. Environment, Data, and Schedule

| Item | Details | Owner | Status |
|---|---|---|---|
| Environment | {{ENVIRONMENT}} | {{OWNER}} | Planned |
| Test Data | {{DATA_REFERENCE}} | {{OWNER}} | Planned |
| Execution Window | {{WINDOW}} | {{OWNER}} | Planned |

## 4. UAT Entry and Completion Criteria

| Type | Criterion | Evidence | Status |
|---|---|---|---|
| Entry / Completion | {{CRITERION}} | {{EVIDENCE}} | Not Met / Met / Not Applicable |

## 5. UAT Execution Summary

| Scenario / Case | Business Area | Result | Observation / Defect | Evidence | Retest Status |
|---|---|---|---|---|---|
| {{TS_OR_TC_ID}} | {{BUSINESS_AREA}} | Not Run / Passed / Failed / Blocked | {{REFERENCE}} | {{EVIDENCE}} | {{STATUS}} |

## 6. Defect and Issue Log

| Defect ID | Summary | Type | Severity | Priority | Related Requirement | Scenario / Case | Environment / Build | Owner | Status | Resolution / Workaround | Retest Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DEF-001 | {{SUMMARY}} | Defect / Issue / Observation | {{SEVERITY}} | {{PRIORITY}} | {{FR_ID}} | {{TS_OR_TC_ID}} | {{ENVIRONMENT}} | {{OWNER}} | Open | {{RESOLUTION}} | Not Retested |

## 7. Known Limitations and Deferred Items

| ID | Limitation / Deferred Item | Impact | Workaround | Owner | Target | Status |
|---|---|---|---|---|---|---|
| KL-001 | {{ITEM}} | {{IMPACT}} | {{WORKAROUND}} | {{OWNER}} | {{TARGET}} | Open |

## 8. UAT Outcome and Recommendation

Record the factual outcome, unresolved issues, business observations, and recommendation:

- Continue testing
- Ready with documented limitations
- Not ready
- Not applicable

This recommendation is a project-status statement, not a formal approval.

## 9. Open Questions

| ID | Question | Owner | Impact | Status |
|---|---|---|---|---|
| UATQ-001 | {{QUESTION}} | {{OWNER}} | {{IMPACT}} | Open |

## 10. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
