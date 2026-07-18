# Sprint Plan

## Purpose

Define the focused, executable scope of one sprint and provide the development team, vendor, or AI implementation tool with the exact context required to implement and test that scope.

Create a separate plan for each sprint and preserve it under the project sprint-history path, for example:

```text
docs/05-Agile-Delivery/sprints/Sprint-01-Plan.md
docs/05-Agile-Delivery/sprints/Sprint-02-Plan.md
```

## Required Context

1. `docs/05-Agile-Delivery/01-Product-Roadmap-and-Release-Plan.md`
2. `docs/01-Requirements/04-Delivery-Backlog.md`
3. Requirements and traceability entries linked to selected backlog items
4. Relevant solution-design documents
5. Relevant UI/UX documents
6. Relevant QA scenarios and cases

## AI Instructions

- Read only the context linked to the selected sprint items unless broader context is necessary.
- Include only documented backlog items that satisfy the Definition of Ready.
- Do not change requirements, business rules, architecture, security, or acceptance criteria silently.
- Record a blocker when a material decision, dependency, or design detail is missing.
- Update implementation documents, tests, traceability, and Sprint Status as work progresses.

## 1. Sprint Summary

| Field | Value |
|---|---|
| Sprint | {{SPRINT_NUMBER_OR_NAME}} |
| Sprint Goal | {{SPRINT_GOAL}} |
| Target Release | {{RELEASE_ID}} |
| Start Date | {{START_DATE}} |
| End Date | {{END_DATE}} |
| Sprint Owner | {{OWNER}} |
| Status | Planned |

## 2. Sprint Scope

| Backlog ID | Delivery Item | Requirements | Design References | Priority | Estimate | Owner | Status |
|---|---|---|---|---|---|---|---|
| BI-001 | {{DELIVERY_ITEM}} | {{FR_OR_NFR_IDS}} | {{DESIGN_REFERENCES}} | Must | {{ESTIMATE}} | {{OWNER}} | Planned |

## 3. Acceptance Criteria and Evidence

| Backlog ID | Acceptance Criteria | Verification Method | Evidence Expected | Status |
|---|---|---|---|---|
| BI-001 | {{AC_IDS_OR_CRITERIA}} | {{TEST_OR_REVIEW}} | {{EVIDENCE}} | Not Started |

## 4. Implementation Scope

Document applicable sprint work:

- Platform configuration
- Frontend or UI work
- Backend, workflow, service, or business-logic work
- Data, migration, reporting, or analytics work
- API and integration work
- AI, agent, prompt, retrieval, evaluation, or safety work
- Security, infrastructure, deployment, and observability work
- Documentation and knowledge-transfer work

## 5. Out of Scope

- {{OUT_OF_SCOPE_ITEM}}

## 6. Dependencies and Preconditions

| Dependency / Precondition | Owner | Needed By | Status | Impact |
|---|---|---|---|---|
| {{DEPENDENCY}} | {{OWNER}} | {{DATE_OR_STEP}} | Open | {{IMPACT}} |

## 7. Execution Sequence

| Step | Activity | Inputs | Output | Owner | Status |
|---|---|---|---|---|---|
| 1 | {{ACTIVITY}} | {{INPUTS}} | {{OUTPUT}} | {{OWNER}} | Not Started |

## 8. Sprint Test Scope

| Test / Review | Scenario or Case | Owner | Environment | Evidence | Status |
|---|---|---|---|---|---|
| {{TEST_OR_REVIEW}} | {{TS_OR_TC_IDS}} | {{OWNER}} | {{ENVIRONMENT}} | {{EVIDENCE}} | Not Started |

## 9. Sprint Risks, Assumptions, and Questions

| ID | Type | Description | Owner | Required Action | Status |
|---|---|---|---|---|---|
| SPQ-001 | Risk / Assumption / Question | {{DESCRIPTION}} | {{OWNER}} | {{ACTION}} | Open |

## 10. Sprint Completion Checklist

- [ ] Sprint scope meets documented acceptance criteria.
- [ ] Required tests and reviews are completed with evidence.
- [ ] Defects and known limitations are recorded.
- [ ] Documentation and traceability are updated.
- [ ] Sprint Status reflects the actual outcome.
- [ ] Incomplete items are returned to the backlog and not marked complete.

## 11. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial sprint plan |
