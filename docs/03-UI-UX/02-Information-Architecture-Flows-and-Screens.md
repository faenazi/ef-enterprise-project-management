# Information Architecture, Flows, and Screens

## Purpose

Define the navigation structure, user flows, routes, screens, role access, data needs, actions, and dependencies in one connected reference for design, implementation, and testing.

## Required Context

1. `docs/01-Requirements/03-System-Requirements.md`
2. `docs/01-Requirements/04-Delivery-Backlog.md`
3. `docs/02-Solution-Design/01-Solution-Overview-and-Architecture.md`
4. `docs/02-Solution-Design/02-Application-Architecture.md`
5. `docs/02-Solution-Design/03-Data-API-and-Integration-Design.md`
6. `docs/03-UI-UX/01-UX-Foundation-and-Users.md`

## AI Instructions

- Create pages, routes, and flows only from documented requirements and scenarios.
- Link every important flow and screen to requirement and backlog IDs.
- Show role restrictions and data dependencies explicitly.
- Include alternative, exception, cancellation, and recovery paths where material.
- Avoid duplicating detailed visual behavior that belongs in the wireframe and interaction document.

## 1. Information Architecture

Describe the application hierarchy, primary navigation, secondary navigation, modules, dashboards, global actions, breadcrumbs, search, and role-based variations.

```text
{{APPLICATION_NAME}}
├── {{PRIMARY_AREA_1}}
│   ├── {{PAGE_1}}
│   └── {{PAGE_2}}
└── {{PRIMARY_AREA_2}}
```

## 2. Navigation and Route Map

| Route ID | Route / Destination | Page | Available Roles | Entry Points | Related Requirements |
|---|---|---|---|---|---|
| ROUTE-001 | {{ROUTE}} | {{PAGE}} | {{ROLES}} | {{ENTRY_POINTS}} | {{FR_IDS}} |

## 3. User Flows

For each important flow, document:

- Flow ID and name
- User role and goal
- Trigger and preconditions
- Main steps and decision points
- Alternative, exception, and cancellation paths
- Permission checks
- Success and failure outcomes
- Related requirements, backlog items, screens, and interfaces

Use a Mermaid flowchart or sequence diagram when it materially improves understanding.

## 4. Flow Catalog

| Flow ID | Flow | Role | Trigger | Outcome | Screens | Requirements | Backlog Items |
|---|---|---|---|---|---|---|---|
| FLOW-001 | {{FLOW}} | {{ROLE}} | {{TRIGGER}} | {{OUTCOME}} | {{SCREEN_IDS}} | {{FR_IDS}} | {{BI_IDS}} |

## 5. Screen Inventory

| Screen ID | Screen | Route | Roles | Purpose | Main Actions | Data / API Dependency | Related Flow | Requirements | Backlog Items | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SCR-001 | {{SCREEN}} | {{ROUTE}} | {{ROLES}} | {{PURPOSE}} | {{ACTIONS}} | {{DEPENDENCY}} | FLOW-001 | FR-001 | BI-001 | Must | Planned |

## 6. Role-to-Screen Access

| Role | Screen / Area | Visibility | Allowed Actions | Data Scope | Conditions |
|---|---|---|---|---|---|
| {{ROLE}} | {{SCREEN_OR_AREA}} | Visible / Hidden | {{ACTIONS}} | {{DATA_SCOPE}} | {{CONDITIONS}} |

The security design remains the authoritative source for permissions. This table describes their UI effect.

## 7. Cross-Screen Patterns

Document global search, filters, saved views, pagination, navigation persistence, deep links, notifications, help, session timeout behavior, and return-to-previous-context behavior where applicable.

## 8. Gaps and Open Questions

| ID | Gap / Question | Impacted Flow or Screen | Owner | Status |
|---|---|---|---|---|
| IAFQ-001 | {{GAP_OR_QUESTION}} | {{REFERENCE}} | {{OWNER}} | Open |

## 9. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
