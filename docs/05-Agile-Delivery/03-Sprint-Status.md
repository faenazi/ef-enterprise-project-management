# Sprint Status

## Purpose

Maintain the current, evidence-based status of the active sprint, including completed work, in-progress work, blockers, scope changes, changed artifacts, testing, and next actions.

At sprint closure, preserve the final record under `docs/05-Agile-Delivery/sprints/Sprint-{{SPRINT_NUMBER}}-Status.md`.

## Required Context

1. The active Sprint Plan
2. `docs/01-Requirements/04-Delivery-Backlog.md`
3. Relevant QA and traceability records

## AI Instructions

- Update this file after meaningful implementation, testing, decisions, or blockers.
- Do not mark an item complete without implementation and verification evidence.
- Preserve failed tests, blockers, known limitations, and incomplete scope.
- Return unfinished items to the backlog or a future sprint explicitly.
- Reference changed artifacts rather than copying their full contents.

## 1. Sprint Status Summary

| Field | Value |
|---|---|
| Sprint | {{SPRINT_NUMBER_OR_NAME}} |
| Sprint Goal | {{SPRINT_GOAL}} |
| Reporting Date | {{DATE}} |
| Overall Status | Not Started / In Progress / Blocked / At Risk / Completed |
| Goal Outcome | Not Evaluated / Met / Partially Met / Not Met |
| Updated By | {{UPDATED_BY}} |

## 2. Backlog Progress

| Backlog ID | Delivery Item | Owner | Status | Evidence / Reference | Notes |
|---|---|---|---|---|---|
| BI-001 | {{DELIVERY_ITEM}} | {{OWNER}} | Not Started | {{REFERENCE}} | {{NOTES}} |

## 3. Completed

| Item | Completion Evidence | Completed By | Date |
|---|---|---|---|
| {{ITEM}} | {{EVIDENCE}} | {{OWNER}} | {{DATE}} |

## 4. In Progress and Next

| Item | Current Activity | Next Step | Owner | Forecast |
|---|---|---|---|---|
| {{ITEM}} | {{CURRENT_ACTIVITY}} | {{NEXT_STEP}} | {{OWNER}} | {{FORECAST}} |

## 5. Blockers and Risks

| ID | Item | Blocker / Risk | Impact | Required Action | Owner | Status |
|---|---|---|---|---|---|---|
| BLK-001 | {{ITEM}} | {{BLOCKER_OR_RISK}} | {{IMPACT}} | {{ACTION}} | {{OWNER}} | Open |

## 6. Scope and Decision Changes

| ID | Change / Decision | Reason | Impact | Related Items | Owner | Date |
|---|---|---|---|---|---|---|
| CHG-001 | {{CHANGE_OR_DECISION}} | {{REASON}} | {{IMPACT}} | {{REFERENCES}} | {{OWNER}} | {{DATE}} |

## 7. Changed Artifacts

| File / Artifact | Change Summary | Backlog Item | Status |
|---|---|---|---|
| {{PATH_OR_ARTIFACT}} | {{CHANGE_SUMMARY}} | {{BI_ID}} | Updated |

## 8. Testing and Quality Status

| Scenario / Case / Review | Result | Defect / Gap | Evidence | Next Action |
|---|---|---|---|---|
| {{REFERENCE}} | {{RESULT}} | {{DEFECT_OR_GAP}} | {{EVIDENCE}} | {{NEXT_ACTION}} |

## 9. Incomplete or Carried-Over Items

| Backlog ID | Reason Incomplete | Remaining Work | Return Destination | Owner |
|---|---|---|---|---|
| {{BI_ID}} | {{REASON}} | {{REMAINING_WORK}} | Product Backlog / Sprint {{NUMBER}} | {{OWNER}} |

## 10. Sprint Review and Retrospective Notes

| Type | Observation | Action | Owner | Target |
|---|---|---|---|---|
| Review / Retrospective | {{OBSERVATION}} | {{ACTION}} | {{OWNER}} | {{TARGET}} |

## 11. Status History

| Date | Overall Status | Summary | Updated By |
|---|---|---|---|
| {{DATE}} | {{STATUS}} | {{SUMMARY}} | {{UPDATED_BY}} |
