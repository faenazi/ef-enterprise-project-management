# Requirements Traceability Matrix

## Purpose

Maintain end-to-end traceability from business objectives through requirements, delivery, design, testing, and release without duplicating the source documents.

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

1. `docs/01-Requirements/01-Project-Overview.md`
2. `docs/01-Requirements/02-Business-Requirements.md`
3. `docs/01-Requirements/03-System-Requirements.md`
4. `docs/01-Requirements/04-Delivery-Backlog.md`
5. Relevant solution-design and QA documents

## AI Instructions

- Reference existing IDs exactly; never create an ID solely to make the matrix appear complete.
- Use one row per traceable relationship when a requirement maps to multiple items.
- Mark missing coverage as a gap rather than guessing.
- Update this matrix when requirements, backlog items, designs, tests, or releases change.

## Traceability Model

```text
Objective → Business Requirement / Rule → FR / NFR → Backlog Item → Design → Test → Release
```

## Identifier Standard

An ID is defined once in its authoritative source and reused unchanged when referenced elsewhere. Do not assign the same ID to different concepts. Document-local items use a distinct prefix so links remain unambiguous across the repository.

| Item | Prefix | Example |
|---|---|---|
| Objective | OBJ | OBJ-001 |
| Business Requirement | BR | BR-001 |
| Business Rule | RULE | RULE-001 |
| Functional Requirement | FR | FR-001 |
| Non-Functional Requirement | NFR | NFR-001 |
| Backlog Item | BI | BI-001 |
| Acceptance Criterion | AC | AC-001 |
| Test Scenario | TS | TS-001 |
| Test Case | TC | TC-001 |
| Project Assumption / Constraint / Dependency | PACD | PACD-001 |
| Business Assumption / Constraint / Dependency | BACD | BACD-001 |
| Architecture Decision | ADR | ADR-001 |
| Architecture Component | ARCMP | ARCMP-001 |
| UI Component | UICMP | UICMP-001 |
| Release | REL | REL-001 |
| Delivery Risk | DRISK | DRISK-001 |
| Defect | DEF | DEF-001 |
| Project Open Question | POQ | POQ-001 |
| Business Open Question | BOQ | BOQ-001 |
| System Open Question | SOQ | SOQ-001 |
| Technology Open Question | TOQ | TOQ-001 |
| Application Architecture Question | AAQ | AAQ-001 |
| Data and Integration Question | DIQ | DIQ-001 |
| UX Foundation Question | UXFQ | UXFQ-001 |
| Information Architecture and Flow Question | IAFQ | IAFQ-001 |
| Wireframe and Interaction Question | WIQ | WIQ-001 |
| Design System Question | DSQ | DSQ-001 |
| QA Strategy Question | QASQ | QASQ-001 |
| Test Case Question | TCQ | TCQ-001 |
| UAT Question | UATQ | UATQ-001 |
| QA Residual Risk | QARR | QARR-001 |
| Release Residual Risk | RELR | RELR-001 |

## Traceability Matrix

| Objective | BR / Rule | FR / NFR | Backlog Item | Design Reference | Test Scenario / Case | Release / Sprint | Coverage Status | Notes |
|---|---|---|---|---|---|---|---|---|
| OBJ-001 | BR-001 | FR-001 | BI-001 | {{DESIGN_REFERENCE}} | TC-001 | {{TARGET}} | Partial | {{NOTES}} |

## Traceability Gaps

| Gap ID | Missing Coverage | Impact | Required Action | Owner | Status |
|---|---|---|---|---|---|
| TG-001 | {{MISSING_COVERAGE}} | {{IMPACT}} | {{ACTION}} | {{OWNER}} | Open |

## Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
