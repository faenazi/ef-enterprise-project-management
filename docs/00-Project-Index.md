# Project Index

This file is the central control point for the Environment Fund Enterprise Project Management Platform documentation, readiness, document status, confirmed scope decisions, and material blockers.

## Project Information

| Field | Value |
|---|---|
| Project Name | Environment Fund Enterprise Project Management Platform |
| Arabic Name | منصة إدارة المشاريع المؤسسية لصندوق البيئة |
| Project Description | A unified enterprise platform for governing and managing strategies, portfolios, programs, initiatives, projects, work, resources, finances, contracts, risks, quality, benefits, reporting, knowledge, and operational transition across the complete project lifecycle. |
| Business Owner | TBD — to be confirmed by the Environment Fund |
| Product / System Owner | TBD — to be confirmed by the Environment Fund |
| Project Type | Enterprise Project Portfolio Management / Project Management Information System |
| Project Size | Large / Enterprise-wide |
| Current Phase | Requirements traceability and confirmed integration-scope harmonization |
| Delivery Approach | Documentation First → Agile Sprint Delivery |
| Target Scope | Complete target-state enterprise platform; not limited to an MVP or task-tracking tool |
| Solution / Technology | TBD — technology-neutral until requirements, fit-gap, architecture, security, operations, and commercial constraints are evaluated |
| Confirmed Direct Integrations | Oracle Fusion Cloud ERP; Microsoft Entra ID for SSO; Microsoft Exchange for enterprise email and calendar capabilities |
| Documentation Language | English governance documentation with detailed Arabic requirements and delivery backlog; bilingual solution requirements where applicable |
| Last Updated | 2026-07-18 |

## Confirmed Integration Scope

The following direct enterprise integrations are confirmed as the complete integration scope for the current target solution:

1. **Oracle Fusion Cloud ERP**
   - Provides the approved ERP integration boundary.
   - The exact modules, business objects, fields, APIs, events, directions, frequencies, reconciliation rules, and failure handling remain to be defined in the Data, API, and Integration Design.
   - The platform must not duplicate Oracle-controlled financial, procurement, supplier, contract, purchase-order, receipt, invoice, payment, or other ERP data as uncontrolled editable master data.

2. **Microsoft Entra ID**
   - Provides enterprise authentication and Single Sign-On for authorized users.
   - The detailed tenant, application registration, protocol, claim mapping, group or role mapping, lifecycle, conditional-access, MFA, session, and external-user behavior remain to be designed and approved.

3. **Microsoft Exchange**
   - Provides the approved enterprise email and calendar integration boundary.
   - The detailed scope may include system notifications, email delivery, calendar events, meeting invitations, and related approved interactions.
   - Exact service endpoints, permissions, mailboxes, identities, templates, throttling, delivery tracking, calendar ownership, and failure handling remain to be designed.

No other direct enterprise integration is currently in scope. In particular, prior draft references to OpenText ECM, HR platforms, analytics platforms, correspondence systems, strategy systems, risk systems, ITSM tools, execution tools, or any other external platform are superseded by this decision and must be removed, marked out of scope, or converted into non-integrated manual or file-based behavior where separately required.

This decision confirms the integration boundary only. It does not approve specific APIs, technical patterns, credentials, commercial products beyond the named platforms, or production configuration.

## Scope Commitment

The project documentation must cover the complete target-state system before implementation planning is treated as ready.

The scope includes the full lifecycle from strategy and demand intake through portfolio and program governance, project initiation, planning, procurement, execution, monitoring, control, acceptance, closure, benefits realization, post-project evaluation, and knowledge reuse. It also includes supporting data, roles, workflows, controls, security, reporting, user experience, non-functional requirements, operations, testing, release, and transition needs.

Incremental releases and Agile sprints may implement the documented scope. They must not be used to omit target-state capabilities or redefine the project as an MVP without an explicit documented decision.

## Capability Areas Requiring Full Documentation

1. Strategy, objectives, initiatives, outcomes, and strategic alignment
2. Demand, idea, request, opportunity, and mandate intake
3. Business cases, feasibility, evaluation, scoring, and prioritization
4. Portfolio governance, optimization, scenario planning, and performance
5. Program governance, dependencies, shared outcomes, and benefits
6. Project initiation, classification, chartering, and governance
7. Stage gates, approvals, committees, exceptions, and decision controls
8. Scope, requirements, deliverables, WBS, and acceptance criteria
9. Schedules, milestones, dependencies, critical path, and baselines
10. Tasks, work management, Agile, Kanban, and hybrid delivery
11. Resources, skills, allocation, capacity, and timesheets
12. Budgets, forecasts, commitments, actual costs, cash flow, and earned value
13. Procurement, contracts, suppliers, purchase orders, receipts, invoices, and payments
14. Deliverable review, acceptance, completion, and certification
15. Quality planning, inspection, nonconformity, and corrective action
16. Risks, issues, assumptions, constraints, dependencies, and actions
17. Change requests, impact analysis, approval, and baseline control
18. Decisions, meetings, committees, communications, and stakeholder engagement
19. Documents, records, versions, templates, search, and controlled retention
20. Benefits, outcomes, value realization, impact, and post-project evaluation
21. KPIs, executive dashboards, PMO dashboards, analytics, and reporting
22. Status reporting, alerts, reminders, notifications, and escalation
23. Knowledge, lessons learned, and organizational reuse
24. Workflow, forms, reference data, configuration, and administration
25. Identity, roles, permissions, delegation, segregation of duties, and audit
26. Data governance, privacy, classification, retention, residency, and archival
27. The three confirmed direct integrations, including synchronization, reconciliation, failure handling, and support
28. Performance, availability, scalability, maintainability, accessibility, Arabic, English, RTL, LTR, backup, recovery, support, monitoring, and continuity
29. Governed intelligent capabilities where separately justified and documented

This capability list is an analysis boundary, not a substitute for detailed requirements. Processes, rules, exceptions, entities, fields, states, permissions, interfaces, reports, notifications, controls, acceptance criteria, and tests must be documented in their authoritative files.

## Documentation Areas

1. Requirements: project overview, current state, target state, stakeholder needs, business requirements, business rules, system requirements, backlog, and traceability
2. Solution Design: solution type, technology, architecture, application, data, APIs, the three confirmed integrations, security, access, non-functional design, deployment, and operations
3. UI/UX: users, roles, scenarios, information architecture, flows, screens, wireframes, interactions, design system, Arabic, English, RTL, accessibility, and implementation guidance
4. QA and Testing: strategy, scenarios, cases, test data, evidence, UAT, defects, regression, non-functional verification, and release readiness
5. Agile Delivery: product roadmap, release allocation, sprint planning, sprint evidence, release, cutover, rollback, handover, and early-life support

## Documentation Status Matrix

Allowed document statuses: `Not Started`, `Draft`, `Under Review`, `Ready`, and `N/A`.

| Document | Owner | Status | Material Blockers / Gaps | Last Updated |
|---|---|---|---|---|
| Project Overview | TBD | Draft | Must be harmonized with the confirmed three-system integration scope; business and system ownership, current-state evidence, governance owners, and confirmed constraints remain to be validated | 2026-07-18 |
| Business Requirements | TBD | Draft | Must remove or mark out of scope any integration beyond Oracle Fusion Cloud ERP, Microsoft Entra ID, and Microsoft Exchange; current-state evidence, owners, approval rules, policies, detailed data ownership, and stakeholder validation remain open | 2026-07-18 |
| System Requirements | TBD | Draft | Arabic SRS baseline contains 332 FRs and 56 NFRs; its current candidate integration catalog must be reduced to the three confirmed integrations, while exact objects, APIs, directions, frequencies, reconciliation, security, and service targets remain open | 2026-07-18 |
| Delivery Backlog | TBD | Draft | Arabic baseline contains 24 epics and 190 detailed delivery items; integration items must be harmonized to the three confirmed integrations, and all records remain Not Ready pending reviewed requirements, design, security, UX, acceptance, and test readiness | 2026-07-18 |
| Traceability Matrix | TBD | Draft | Baseline traceability exists; it must record the confirmed integration boundary and track harmonization of conflicting draft references before downstream design | 2026-07-18 |
| Technology Stack | TBD | Not Started | Solution type, hosting, architecture, licensing, support, and fit-gap decisions are not confirmed; the integration products are confirmed but their technical patterns are not | 2026-07-18 |
| Solution Overview and Architecture | TBD | Not Started | Depends on reviewed requirements, confirmed integration boundary, backlog, and solution-type decisions | 2026-07-18 |
| Application Architecture | TBD | Not Started | Depends on confirmed solution type, modules, system requirements, integration boundary, and backlog | 2026-07-18 |
| Data, API, and Integration Design | TBD | Not Started | Must design only Oracle Fusion Cloud ERP, Microsoft Entra ID SSO, and Microsoft Exchange; authoritative objects, ownership, interfaces, fields, contracts, frequency, reconciliation, security, and failure behavior require confirmation | 2026-07-18 |
| Security and Access Control | TBD | Not Started | Entra ID is confirmed for SSO; roles, data classification, identity claims, policies, approval matrices, delegation, external access, and segregation-of-duties rules require confirmation | 2026-07-18 |
| Non-Functional and Operational Design | TBD | Not Started | Measurable performance, availability, capacity, recovery, support, monitoring, continuity, Exchange delivery, and integration service targets require confirmation | 2026-07-18 |
| UX Foundation and Users | TBD | Not Started | User groups, goals, contexts, evidence, language, accessibility, device, and external-user needs require confirmation | 2026-07-18 |
| Information Architecture, Flows, and Screens | TBD | Not Started | Depends on reviewed workflows, roles, requirements, lifecycle states, backlog, and system boundaries | 2026-07-18 |
| Wireframes and Interaction Behavior | TBD | Not Started | Depends on the approved screen inventory, flow catalog, permissions, fields, states, and acceptance needs | 2026-07-18 |
| Design System and Implementation Guidance | TBD | Not Started | Requires authoritative Environment Fund brand assets, accessibility requirements, and confirmed implementation stack | 2026-07-18 |
| QA Strategy and Test Plan | TBD | Not Started | Depends on reviewed requirements, backlog, risks, architecture, the three confirmed integrations, environments, and measurable targets | 2026-07-18 |
| Test Scenarios | TBD | Not Started | Depends on requirements, rules, workflows, interfaces, lifecycle states, risks, backlog, and planned controls | 2026-07-18 |
| Planned Test Cases | TBD | Not Started | Depends on approved scenarios, detailed expected behavior, data, environments, and item-level acceptance criteria | 2026-07-18 |
| UAT and Defect Management Plan | TBD | Not Started | Participants, environments, data, scope, governance, and readiness criteria require confirmation | 2026-07-18 |
| QA Summary and Release Readiness | TBD | Not Started | No execution evidence exists; document remains planned | 2026-07-18 |
| Product Roadmap and Release Plan | TBD | Not Started | Depends on reviewed backlog, architecture, dependencies, priorities, capacity, and delivery constraints | 2026-07-18 |
| Active Sprint Plan | TBD | Not Started | Implementation is not authorized and no backlog item is Ready | 2026-07-18 |
| Active Sprint Status | TBD | Not Started | No active implementation sprint | 2026-07-18 |
| Release and Transition Plan | TBD | Not Started | Depends on release scope, QA evidence, environments, security, operations, rollback, and support model | 2026-07-18 |

## Current Documentation Workstream

The active workstream is traceability completion and harmonization of all requirement documents with the confirmed integration scope.

```text
Project foundation
→ Project Overview
→ Comprehensive Business Requirements baseline
→ Detailed Arabic System Requirements baseline
→ Comprehensive Arabic Delivery Backlog baseline
→ Traceability Matrix
→ Confirmed integration-scope harmonization
→ Current-state evidence and stakeholder validation
→ Confirmed Business Rules, roles, approvals, and measurable NFR targets
→ Solution Design
→ UI/UX
→ QA Planning
→ Product Roadmap and Release Plan
→ Documentation Readiness Review
```

No implementation, production configuration, procurement commitment, or technical integration pattern is authorized by the current documentation status.

## System Requirements Baseline Summary

The current Arabic SRS draft establishes the following initial baseline:

- 332 functional requirements across 24 capability groups
- 27 initial user and stakeholder roles
- 16 primary record lifecycle models
- 55 validation and business-rule enforcement controls
- 62 business data entities or domains
- 25 reports and dashboards
- 14 candidate integration records that must now be harmonized to the 3 confirmed direct integrations
- 40 notifications, reminders, and escalation events
- 27 audit requirements
- 56 non-functional requirements
- 40 business exceptions and edge cases
- 50 system open questions

These counts describe the current draft only. They do not indicate approval, completion, implementation readiness, or test coverage. The previous candidate integration count is not an approved scope count.

## Delivery Backlog Baseline Summary

The current Arabic Delivery Backlog draft establishes:

- 24 epics aligned with the 24 SRS functional capability groups
- 190 detailed delivery items
- 152 features
- 14 configuration items
- 8 integration items that must be reviewed and reduced or reclassified against the 3 confirmed integrations
- 3 data or migration items
- 9 technical enablers
- 4 governed AI use cases
- 12 shared acceptance profiles
- 24 initial epic-level acceptance criteria
- 12 material dependencies and 12 backlog gaps
- 214 total `BI` records including epics and delivery items

All backlog records remain `Not Ready` and `Not Started`. No target release or sprint has been assigned.

## Documentation Readiness Checklist

Implementation may begin only when the selected scope satisfies all applicable checks:

- [ ] Required documents in the status matrix are `Ready` or `N/A` with a reason.
- [ ] The complete target-state scope remains documented even when delivery is incremental.
- [ ] Current-state and target-state processes are sufficiently understood.
- [ ] Business requirements and business rules are reviewed and confirmed for the selected scope.
- [ ] Functional requirements, non-functional requirements, exceptions, validations, and acceptance criteria are sufficiently documented.
- [ ] Users, roles, data scopes, approvals, delegations, and segregation-of-duties rules are documented.
- [ ] Architecture, data, integration, security, operational, and UI/UX decisions are recorded.
- [ ] Only the three confirmed direct integrations remain in the authoritative scope and all conflicting draft references are resolved.
- [ ] Systems of record, ownership, contracts, synchronization, reconciliation, and failure behavior are defined for the confirmed integrations.
- [ ] Backlog items selected for the sprint meet the Definition of Ready.
- [ ] Traceability has no unresolved gap that blocks implementation.
- [ ] QA strategy, scenarios, planned cases, evidence expectations, environments, and test data are defined.
- [ ] Dependencies, risks, assumptions, constraints, and open questions have owners and actions.
- [ ] No unresolved blocker requires the delivery team or an AI tool to invent a business or technical decision.

This checklist records implementation readiness and does not represent a formal approval or signature.

## Current Material Open Questions

| ID | Question / Confirmation | Impact | Owner | Status |
|---|---|---|---|---|
| PIQ-001 | Confirm the formal business owner, product owner, system owner, document owners, and governance body. | Ownership, reviews, decisions, and escalation cannot be finalized. | Environment Fund | Open |
| PIQ-002 | Provide authoritative project-management policies, procedures, templates, approval matrices, reports, and sample records. | Current-state analysis, business rules, workflows, and detailed acceptance behavior cannot be completed without evidence. | Environment Fund | Open |
| PIQ-003 | Confirm organizational scope, user populations, external participants, and controlled-access requirements. | Roles, licensing, security, data scope, collaboration, and UX remain incomplete. | Environment Fund | Open |
| PIQ-004 | Confirm detailed integration boundaries for Oracle Fusion Cloud ERP, Microsoft Entra ID SSO, and Microsoft Exchange only, including authoritative objects, directions, frequencies, APIs, security, reconciliation, monitoring, fallback, and support ownership. | Integration design cannot be completed until the approved three-system boundary is detailed. | Environment Fund | Open |
| PIQ-005 | Confirm enterprise architecture, cybersecurity, data governance, hosting, privacy, accessibility, records, and continuity standards. | Technology, security, privacy, retention, accessibility, and operational controls cannot be confirmed. | Environment Fund | Open |
| PIQ-006 | Confirm project classifications, governance paths, stage gates, scoring models, health thresholds, reporting cycles, approval matrices, delegation, and segregation of duties. | Workflows, permissions, reports, validations, alerts, backlog readiness, and acceptance criteria remain provisional. | Environment Fund | Open |
| PIQ-007 | Confirm measurable performance, availability, capacity, support, monitoring, RPO, RTO, service-hour, browser, device, accessibility, and integration targets. | NFRs and technical backlog items remain directional rather than implementation-ready. | Environment Fund | Open |
| PIQ-008 | Confirm historical data, migration, retention, archival, legal-hold, and decommissioning scope. | Migration, records, transition, data-volume requirements, and related backlog items remain unclear. | Environment Fund | Open |
| PIQ-009 | Confirm which intelligent capabilities are required and their data, hosting, human-review, safety, and evaluation controls. | AI backlog items cannot be designed or released safely. | Environment Fund | Open |
| PIQ-010 | Confirm prioritization principles and constraints for allocating the backlog to releases. | No target release or sprint can be assigned responsibly. | Project governance | Open |

## Notes

- The integration scope is confirmed to three direct integrations only.
- Do not reintroduce another direct integration without an explicit documented scope decision.
- Expand documentation according to the enterprise scale and complexity of this project.
- Do not remove a target business capability merely because it is not selected for an early release.
- Do not invent missing information.
- Record unclear items as questions, assumptions, dependencies, constraints, risks, or blockers.
- Documentation readiness is a review checkpoint, not a formal sign-off.
- QA execution evidence and defects are recorded only when testing occurs.
- During implementation, preserve sprint, test, defect, decision, and evidence history.
