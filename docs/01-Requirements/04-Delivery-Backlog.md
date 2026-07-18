# Delivery Backlog

## Purpose

Convert sufficiently documented and reviewed requirements into prioritized, traceable, and executable delivery items. The backlog supports custom development, low-code, enterprise platforms, data, integration, AI, and vendor-delivered projects.

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

1. `docs/01-Requirements/02-Business-Requirements.md`
2. `docs/01-Requirements/03-System-Requirements.md`

## AI Instructions

- Create backlog items only from documented scope.
- Link each item to at least one requirement or explicitly mark it as an enabling technical item.
- Choose the appropriate item type; do not force every project into user stories.
- Do not mark an item Ready when requirements, dependencies, or acceptance criteria remain materially unclear.
- Keep implementation choices aligned with confirmed solution-design decisions.

## 1. Backlog Structure

Supported item types include:

- Epic
- Feature
- User Story
- Configuration Item
- Fit-Gap Item
- Integration Item
- Data / Migration Item
- AI Use Case
- Technical Enabler

## 2. Definition of Ready

An item is Ready when:

- Its purpose and scope are clear.
- Linked requirements are identified.
- Acceptance criteria are testable.
- Material dependencies and open questions are resolved or explicitly accepted.
- Required design context is available for implementation.

## 3. Backlog

| ID | Type | Epic / Feature | Delivery Item | Linked Requirements | Priority | Dependencies | Target Release / Sprint | Readiness | Status |
|---|---|---|---|---|---|---|---|---|---|
| BI-001 | User Story / Enabler / Other | {{EPIC_OR_FEATURE}} | {{DELIVERY_ITEM}} | FR-001 | Must | {{DEPENDENCIES}} | {{TARGET}} | Not Ready | Not Started |

## 4. User Story Format

Use when the backlog item is best expressed as a user story:

```text
As a {{USER_ROLE}},
I want {{CAPABILITY}},
so that {{BUSINESS_VALUE}}.
```

## 5. Acceptance Criteria

| Backlog ID | AC ID | Given | When | Then | Related Requirement |
|---|---|---|---|---|---|
| BI-001 | AC-001 | {{PRECONDITION}} | {{ACTION}} | {{EXPECTED_RESULT}} | FR-001 |

## 6. Backlog Gaps and Open Questions

| ID | Gap / Question | Impacted Items | Owner | Status |
|---|---|---|---|---|
| BG-001 | {{GAP_OR_QUESTION}} | {{ITEM_IDS}} | {{OWNER}} | Open |

## 7. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
