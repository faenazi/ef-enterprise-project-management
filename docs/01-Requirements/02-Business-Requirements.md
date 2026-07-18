# Business Requirements

## Purpose

Document the business context, current and target processes, stakeholder needs, business requirements, and business rules. This document combines the BRD and business-process context so AI tools can understand the business before proposing a system solution.

## Document Information

| Field | Value |
|---|---|
| Project | {{PROJECT_NAME}} |
| Document Owner | {{DOCUMENT_OWNER}} |
| Prepared By | {{PREPARED_BY}} |
| Reviewed By | {{REVIEWED_BY}} |
| Version | 0.1 |
| Status | Draft |
| Classification | Internal |
| Last Updated | {{LAST_UPDATED}} |

## Required Context

1. `docs/00-Project-Index.md`
2. `docs/01-Requirements/01-Project-Overview.md`

## AI Instructions

- Focus on business needs and outcomes, not implementation choices.
- Clearly distinguish current state, target state, confirmed requirements, assumptions, and open questions.
- Assign stable IDs only to confirmed requirements and rules.
- Do not infer approvals, policies, roles, or rules that have not been confirmed.
- Add separate process subsections only when they materially improve understanding.

## 1. Executive Summary

Summarize the business need, affected areas, and intended outcome.

## 2. Business Context and Current Challenges

Describe the current situation, pain points, manual activities, gaps, and business impact.

## 3. Current State — As-Is

For each relevant process, document:

- Process name and owner
- Trigger and outcome
- Participants
- Main steps and decision points
- Systems, data, and documents used
- Exceptions, pain points, and controls

Use Mermaid swimlanes or flowcharts where a visual flow materially improves understanding.

## 4. Target State — To-Be

Describe the intended process, improvements, automation boundaries, controls, and expected outcomes without prescribing technology prematurely.

## 5. Stakeholder Needs

| ID | Stakeholder / Role | Need | Business Value | Priority |
|---|---|---|---|---|
| SN-001 | {{STAKEHOLDER}} | {{NEED}} | {{BUSINESS_VALUE}} | {{PRIORITY}} |

## 6. Business Requirements

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-001 | {{BUSINESS_REQUIREMENT}} | {{RATIONALE}} | {{SOURCE}} | Must | Draft |

Requirements should be clear, necessary, feasible, non-duplicative, and verifiable at the business level.

## 7. Business Rules

| ID | Rule | Source / Owner | Related Requirement | Exceptions | Status |
|---|---|---|---|---|---|
| RULE-001 | {{BUSINESS_RULE}} | {{SOURCE}} | BR-001 | {{EXCEPTIONS}} | Draft |

## 8. Business Data and Reporting Needs

| ID | Need | Users | Frequency | Source | Notes |
|---|---|---|---|---|---|
| DR-001 | {{DATA_OR_REPORTING_NEED}} | {{USERS}} | {{FREQUENCY}} | {{SOURCE}} | {{NOTES}} |

## 9. Business Exceptions and Edge Cases

| ID | Scenario | Expected Business Handling | Related Process / Rule |
|---|---|---|---|
| EX-001 | {{SCENARIO}} | {{EXPECTED_HANDLING}} | {{REFERENCE}} |

## 10. Assumptions, Constraints, and Dependencies

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| BACD-001 | Assumption / Constraint / Dependency | {{DESCRIPTION}} | {{IMPACT}} | {{OWNER}} | Open |

## 11. Open Questions

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-001 | {{QUESTION}} | {{OWNER}} | {{REFERENCE}} | Open |

## 12. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
