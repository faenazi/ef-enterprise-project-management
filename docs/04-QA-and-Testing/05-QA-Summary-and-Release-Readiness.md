# QA Summary and Release Readiness

## Purpose

Provide an evidence-based summary of test execution, coverage, defects, UAT outcome, known limitations, residual risks, and readiness recommendation before a release or transition.

This document does not require signatures or a formal QA approval.

## Required Context

1. `docs/01-Requirements/05-Traceability-Matrix.md`
2. `docs/04-QA-and-Testing/01-QA-Strategy-and-Test-Plan.md`
3. `docs/04-QA-and-Testing/02-Test-Scenarios.md`
4. `docs/04-QA-and-Testing/03-Test-Cases.md`
5. `docs/04-QA-and-Testing/04-UAT-and-Defect-Management.md`
6. Relevant release or delivery scope

## AI Instructions

- Summarize only recorded execution evidence and current defect status.
- Do not infer readiness from planned or incomplete testing.
- Highlight missing coverage, blocked tests, unresolved critical issues, and accepted limitations.
- Separate factual results from the readiness recommendation.
- Never imply a signature or approval that did not occur.

## 1. Release / Scope Summary

| Field | Value |
|---|---|
| Release / Delivery | {{RELEASE_OR_DELIVERY}} |
| Scope | {{SCOPE_SUMMARY}} |
| Environment / Build | {{ENVIRONMENT_AND_BUILD}} |
| Reporting Date | {{DATE}} |
| Overall QA Status | Not Started / In Progress / Completed with Gaps / Completed |

## 2. Coverage Summary

| Coverage Area | Planned | Executed | Passed | Failed | Blocked | Not Applicable | Coverage Notes |
|---|---|---|---|---|---|---|---|
| {{AREA}} | {{PLANNED}} | {{EXECUTED}} | {{PASSED}} | {{FAILED}} | {{BLOCKED}} | {{NA}} | {{NOTES}} |

## 3. Requirements Traceability Summary

| Status | Count | Notes |
|---|---|---|
| Fully Covered | {{COUNT}} | {{NOTES}} |
| Partially Covered | {{COUNT}} | {{NOTES}} |
| Not Covered | {{COUNT}} | {{NOTES}} |

## 4. Defect Summary

| Severity | Open | Resolved | Retest Pending | Deferred | Notes |
|---|---|---|---|---|---|
| Critical / High / Medium / Low | {{OPEN}} | {{RESOLVED}} | {{RETEST_PENDING}} | {{DEFERRED}} | {{NOTES}} |

## 5. UAT Outcome

Summarize executed business validation, untested areas, observations, unresolved issues, and the recorded UAT recommendation.

## 6. Non-Functional and Operational Readiness

| Area | Evidence / Result | Gap or Risk | Owner | Status |
|---|---|---|---|---|
| Security / Performance / Accessibility / Recovery / Monitoring / Other | {{EVIDENCE}} | {{GAP_OR_RISK}} | {{OWNER}} | {{STATUS}} |

## 7. Known Limitations and Residual Risks

| ID | Limitation / Risk | Impact | Workaround / Treatment | Owner | Status |
|---|---|---|---|---|---|
| QARR-001 | {{LIMITATION_OR_RISK}} | {{IMPACT}} | {{TREATMENT}} | {{OWNER}} | Open |

## 8. Pending Actions

| Action | Owner | Target Date | Release Blocking | Status |
|---|---|---|---|---|
| {{ACTION}} | {{OWNER}} | {{DATE}} | Yes / No | Open |

## 9. Readiness Recommendation

Choose one and provide evidence-based rationale:

- `Not Ready`
- `Ready for Limited / Controlled Release`
- `Ready with Documented Limitations`
- `Ready`
- `Not Applicable`

## 10. Review Record

| Reviewed By | Role / Team | Review Date | Notes |
|---|---|---|---|
| {{REVIEWED_BY}} | {{ROLE_OR_TEAM}} | {{DATE}} | {{NOTES}} |

The review record confirms that the summary was reviewed; it is not a formal approval or signature.

## 11. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
