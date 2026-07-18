# UX Foundation and Users

## Purpose

Define the user-experience direction, target users, roles, goals, pain points, accessibility needs, language needs, and experience principles before designing flows or screens.

Use `N/A` with a reason when the project has no user interface.

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
4. `docs/02-Solution-Design/04-Security-and-Access-Control.md`

## AI Instructions

- Derive users, roles, goals, and constraints from documented requirements.
- Do not invent personas, permissions, user research, or accessibility findings.
- Use role profiles instead of fictional personas when research evidence is unavailable.
- Distinguish confirmed user needs from assumptions that require validation.
- Consider Arabic, English, RTL, accessibility, responsive use, and device context where applicable.

## 1. UX Objective

Describe the experience outcome and how it supports the project objectives and target business process.

## 2. Users and Role Profiles

| Role ID | User Group / Role | Responsibilities | Goals | Pain Points | Access Context | Source |
|---|---|---|---|---|---|---|
| ROLE-001 | {{ROLE}} | {{RESPONSIBILITIES}} | {{GOALS}} | {{PAIN_POINTS}} | {{ACCESS_CONTEXT}} | {{SOURCE}} |

## 3. Key User Scenarios

| Scenario ID | User Role | User Goal | Trigger | Expected Outcome | Related Requirements |
|---|---|---|---|---|---|
| UXSC-001 | {{ROLE}} | {{GOAL}} | {{TRIGGER}} | {{OUTCOME}} | {{FR_IDS}} |

## 4. UX Principles

Document project-specific principles such as clarity, efficiency, consistency, progressive disclosure, prevention of errors, transparency of status, accessibility, and user control.

## 5. Language, Direction, and Content

Document supported languages, Arabic-first or bilingual behavior, RTL and LTR direction, terminology sources, date and number formats, content ownership, and translation constraints.

## 6. Accessibility and Inclusive Design

Document applicable accessibility targets, keyboard use, focus behavior, labels, contrast, text resizing, screen-reader considerations, motion preferences, error identification, and any confirmed user accommodations.

## 7. Devices and Usage Context

| Context | Device / Viewport | Frequency | Constraints | Priority |
|---|---|---|---|---|
| {{CONTEXT}} | {{DEVICE}} | {{FREQUENCY}} | {{CONSTRAINTS}} | {{PRIORITY}} |

## 8. UX Success Measures

| Measure | Baseline | Target | Measurement Method | Owner |
|---|---|---|---|---|
| {{MEASURE}} | {{BASELINE_OR_TBD}} | {{TARGET}} | {{METHOD}} | {{OWNER}} |

## 9. Assumptions and Open Questions

| ID | Type | Description | Owner | Validation Needed | Status |
|---|---|---|---|---|---|
| UXFQ-001 | Assumption / Question | {{DESCRIPTION}} | {{OWNER}} | {{VALIDATION}} | Open |

## 10. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
