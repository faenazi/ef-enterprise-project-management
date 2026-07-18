# Project Index

This file should be customized for each new project created from this starter.

## Project Information

| Field | Value |
|---|---|
| Project Name | {{PROJECT_NAME}} |
| Project Description | {{PROJECT_DESCRIPTION}} |
| Business Owner | {{BUSINESS_OWNER}} |
| Product / System Owner | {{PRODUCT_OWNER}} |
| Project Type | {{PROJECT_TYPE}} |
| Project Size | {{PROJECT_SIZE}} |
| Current Phase | {{CURRENT_PHASE}} |
| Delivery Approach | Documentation First → Agile Sprint Delivery |
| Solution / Technology | {{SOLUTION_TYPE_AND_TECHNOLOGY_OR_TBD}} |

## Documentation Areas

1. Requirements: overview, business requirements and processes, system requirements, delivery backlog, and traceability
2. Solution Design: technology, architecture, application, data and integration, security, and operational design
3. UI/UX: users, information architecture, flows, screens, interaction behavior, and design system
4. QA and Testing: strategy, scenarios, cases, UAT, defects, and release readiness
5. Agile Delivery: product and release roadmap, sprint planning, sprint status, release, and operational transition

## Documentation Status Matrix

This is the central readiness view. Update it whenever a document changes status or gains a material blocker.

Allowed document statuses: `Not Started`, `Draft`, `Under Review`, `Ready`, and `N/A`.

| Document | Owner | Status | Material Blockers / Gaps | Last Updated |
|---|---|---|---|---|
| Project Overview | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Business Requirements | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| System Requirements | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Delivery Backlog | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Traceability Matrix | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Technology Stack | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Solution Overview and Architecture | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Application Architecture | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Data, API, and Integration Design | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Security and Access Control | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Non-Functional and Operational Design | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| UX Foundation and Users | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Information Architecture, Flows, and Screens | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Wireframes and Interaction Behavior | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Design System and Implementation Guidance | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| QA Strategy and Test Plan | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Test Scenarios | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Planned Test Cases | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| UAT and Defect Management Plan | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| QA Summary and Release Readiness | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Product Roadmap and Release Plan | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Active Sprint Plan | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Active Sprint Status | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |
| Release and Transition Plan | {{OWNER}} | Not Started | {{BLOCKERS_OR_NONE}} | {{DATE}} |

## Documentation Flow

```text
Project Index
→ Requirements
→ Solution Design
→ UI/UX
→ QA and Testing
→ Product Roadmap and Release Plan
→ Sprint Plan
→ Sprint Status
→ Release and Transition
```

## Agile Delivery

Complete the required documentation first, then use these documents to execute the implementation through Agile sprints:

```text
docs/05-Agile-Delivery/
├── 01-Product-Roadmap-and-Release-Plan.md
├── 02-Sprint-Plan.md
├── 03-Sprint-Status.md
├── 04-Release-and-Transition-Plan.md
└── sprints/
    └── README.md
```

Preserve completed sprint records under `docs/05-Agile-Delivery/sprints/`; do not overwrite the history of a previous sprint.

## Documentation Readiness Checklist

Implementation may begin when the scope selected for the first sprint satisfies all applicable checks:

- [ ] Required documents in the status matrix are `Ready` or `N/A` with a reason.
- [ ] Scope, business rules, functional requirements, NFRs, and acceptance criteria are sufficiently documented.
- [ ] Required architecture, data, integration, security, operational, and UI/UX decisions are recorded.
- [ ] Backlog items selected for the sprint meet the Definition of Ready.
- [ ] Traceability has no unresolved gap that blocks implementation of the selected scope.
- [ ] QA strategy, scenarios, planned cases, evidence expectations, and required test data are defined.
- [ ] Material dependencies, risks, assumptions, and open questions have owners and actions.
- [ ] No unresolved blocker requires the AI or delivery team to invent a business or technical decision.

This checklist records readiness for implementation and does not represent a formal approval or signature.

## Notes

- Generate each document outline based on the project size and complexity.
- Keep small projects lightweight.
- Expand medium and large projects as needed.
- Do not invent missing information.
- Keep unclear items under open questions.
- Documentation readiness is a review checkpoint, not a formal sign-off.
- QA plans and test cases are prepared before implementation; execution evidence and defects are recorded during the sprints.
- During implementation, update Sprint Status whenever meaningful progress, testing, decisions, or blockers occur.
