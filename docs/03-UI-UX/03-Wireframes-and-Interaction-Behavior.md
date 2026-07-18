# Wireframes and Interaction Behavior

## Purpose

Define the layout, hierarchy, interactions, responsive behavior, validation, permissions, feedback, and complete UI states required for each screen before implementation.

## Required Context

1. `docs/01-Requirements/03-System-Requirements.md`
2. `docs/02-Solution-Design/02-Application-Architecture.md`
3. `docs/03-UI-UX/01-UX-Foundation-and-Users.md`
4. `docs/03-UI-UX/02-Information-Architecture-Flows-and-Screens.md`

## AI Instructions

- Design only screens listed in the screen inventory.
- Define behavior, states, and accessibility—not only the happy-path layout.
- Preserve requirement, flow, screen, and backlog IDs in every screen specification.
- Do not invent business rules, permissions, data, or actions.
- Specify Arabic, English, RTL, LTR, and responsive behavior where applicable.

## 1. Screen Specification Template

Create one subsection per screen using this structure:

### SCR-001 — {{SCREEN_NAME}}

| Field | Details |
|---|---|
| Purpose | {{PURPOSE}} |
| Roles | {{ROLES}} |
| Related Flow | {{FLOW_IDS}} |
| Requirements | {{FR_IDS}} |
| Backlog Items | {{BI_IDS}} |
| Route | {{ROUTE}} |
| Data Dependencies | {{DATA_OR_API_DEPENDENCIES}} |

#### Layout and Hierarchy

Describe page regions, reading order, primary information, secondary information, actions, forms, tables, filters, and navigation.

#### Actions and Interaction Rules

| Action | Trigger | Preconditions | System Response | Success Feedback | Failure Feedback |
|---|---|---|---|---|---|
| {{ACTION}} | {{TRIGGER}} | {{PRECONDITIONS}} | {{RESPONSE}} | {{SUCCESS}} | {{FAILURE}} |

#### Fields and Validation

| Field | Type | Required | Validation | Error Message | Permissions | Notes |
|---|---|---|---|---|---|---|
| {{FIELD}} | {{TYPE}} | Yes / No | {{VALIDATION}} | {{MESSAGE}} | {{PERMISSIONS}} | {{NOTES}} |

#### UI States

Define, where applicable:

- Initial and default state
- Loading and progressive loading
- Empty and no-results states
- Validation and error states
- Offline, timeout, and unavailable dependency states
- Success and confirmation states
- Read-only, disabled, and permission-denied states
- Draft, submitted, processing, completed, rejected, cancelled, and archived states
- Concurrent update or stale-data behavior

#### Responsive and Directional Behavior

Document breakpoints or layout modes, touch behavior, table adaptation, navigation changes, text expansion, RTL mirroring, mixed Arabic/English content, and printing where required.

#### Accessibility Behavior

Document keyboard order, focus movement, modal focus, labels, announcements, error association, semantic structure, contrast dependencies, and non-color indicators.

## 2. Reusable Interaction Patterns

Document confirmation dialogs, unsaved changes, destructive actions, bulk operations, filtering, sorting, pagination, uploads, downloads, approvals, notifications, and long-running operations.

## 3. Prototype and Design References

| Reference | Screen / Flow | Version | Owner | Status | Notes |
|---|---|---|---|---|---|
| {{LINK_OR_PATH}} | {{REFERENCE}} | {{VERSION}} | {{OWNER}} | Draft / Reviewed / Final | {{NOTES}} |

## 4. Open Questions

| ID | Question | Related Screen / Flow | Owner | Status |
|---|---|---|---|---|
| WIQ-001 | {{QUESTION}} | {{REFERENCE}} | {{OWNER}} | Open |

## 5. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
