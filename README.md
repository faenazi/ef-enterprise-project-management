# EF Enterprise Project Management Platform

**Arabic name:** منصة إدارة المشاريع المؤسسية لصندوق البيئة

This repository is the documentation and delivery source of truth for the Environment Fund Enterprise Project Management Platform.

The platform is intended to provide one integrated institutional system for governing and managing strategies, portfolios, programs, initiatives, projects, work, resources, finances, contracts, risks, quality, benefits, reporting, knowledge, and operational transition across the complete project lifecycle.

## Project Vision

Establish a unified, governed, auditable, and decision-oriented platform that enables the Environment Fund to manage the complete lifecycle of portfolios, programs, initiatives, and projects from demand and idea intake through evaluation, prioritization, approval, planning, procurement, execution, monitoring, control, acceptance, closure, and benefits realization.

## Full-Scope Commitment

This project is not being documented as a task-tracking tool, a limited PMO dashboard, or an MVP-only solution.

The documentation must define the complete target-state system and all material business, functional, data, integration, security, operational, reporting, and user-experience requirements needed for an enterprise-grade platform. Incremental releases and Agile sprints may be used later to implement the fully documented scope, but they must not be used to silently reduce or omit the target capabilities.

Any capability that is deferred from an implementation release must remain visible in the documented target scope, backlog, roadmap, dependencies, and traceability records.

## Target Capability Scope

The target platform is expected to cover, subject to detailed requirements confirmation, the following integrated capability domains:

1. Strategy, objectives, initiatives, and strategic alignment
2. Demand, idea, request, and opportunity intake
3. Business cases, feasibility assessments, and option analysis
4. Scoring, prioritization, selection, and scenario planning
5. Portfolio management and portfolio governance
6. Program management and cross-project coordination
7. Project initiation, classification, chartering, and governance
8. Stage gates, approvals, committees, and decision controls
9. Scope, requirements, deliverables, and work breakdown structures
10. Schedule, milestones, dependencies, critical path, and baselines
11. Tasks, work management, Kanban, Agile, and hybrid delivery
12. Resources, skills, allocation, capacity, and time management
13. Budgets, forecasts, commitments, actual costs, and earned value
14. Procurement, contracts, purchase orders, vendors, and payments
15. Deliverable review, acceptance, completion, and certification
16. Quality planning, inspections, nonconformities, and corrective actions
17. Risks, issues, assumptions, constraints, and dependencies
18. Change requests, impact analysis, approvals, and baseline control
19. Decisions, actions, meetings, committees, and communications
20. Stakeholder engagement and communication planning
21. Documents, records, versions, templates, and enterprise archiving
22. Benefits, outcomes, value realization, and impact measurement
23. Project, program, portfolio, vendor, and organizational KPIs
24. Executive dashboards, PMO dashboards, analytics, and reporting
25. Status reporting, alerts, notifications, escalation, and reminders
26. Enterprise search, knowledge, lessons learned, and reuse
27. Workflow, forms, templates, reference data, and administration
28. Identity, role-based access, segregation of duties, and auditability
29. Data governance, retention, privacy, classification, and residency
30. APIs and integrations with enterprise financial, procurement, HR, identity, document, correspondence, analytics, and notification systems
31. Availability, performance, scalability, accessibility, Arabic, English, RTL, LTR, backup, recovery, support, monitoring, and operational continuity
32. Optional future intelligent capabilities such as predictive risk detection, automated status summaries, semantic search, and AI-assisted project management, only when separately documented and governed

This list establishes the minimum capability landscape for detailed analysis. It is not a substitute for the business requirements, system requirements, process models, data model, integration catalog, security model, screen inventory, test coverage, or traceability matrix.

## Intended Users

The target platform must support the needs of different institutional user groups, including:

- Executive leadership
- Portfolio and program governance bodies
- Project Management Office roles
- Portfolio managers
- Program managers
- Project managers and coordinators
- Project team members
- Business owners and executive sponsors
- Finance, budget, procurement, contract, risk, quality, legal, audit, and technology functions
- Vendors, consultants, and external participants where controlled access is approved
- System administrators, support teams, data owners, and report consumers

Actual roles, responsibilities, data scopes, and permissions must be confirmed in the requirements and security documentation before implementation.

## Enterprise Integration Direction

The project must define clear ownership and system-of-record boundaries for connected enterprise platforms. Expected integration areas include, subject to confirmation:

- Oracle Fusion Cloud for financial, procurement, contract, supplier, commitment, receipt, invoice, employee, and organizational information
- OpenText ECM for controlled project documents, contracts, official records, versions, and archival
- Microsoft Entra ID or the approved enterprise identity platform for authentication and identity lifecycle
- Enterprise email, calendar, and notification services
- Power BI or the approved analytics platform for enterprise analytics where required
- Other strategy, risk, correspondence, HR, service-management, procurement, or government platforms where an approved business requirement exists

The project management platform must not duplicate authoritative enterprise transactions when another approved system is the system of record. Integration, synchronization, reconciliation, ownership, failure handling, and audit responsibilities must be explicitly documented.

## Documentation-First Delivery Method

The repository follows this controlled method:

```text
Understand the project and current state
→ Document the complete target scope
→ Confirm business requirements and rules
→ Translate them into testable system requirements
→ Build the delivery backlog and traceability
→ Complete solution, data, integration, security, operational, and UI/UX design
→ Prepare QA strategy, scenarios, and planned test cases
→ Review documentation readiness
→ Implement Ready scope through controlled Agile sprints
→ Record evidence, defects, decisions, releases, and operational transition
```

Implementation must not begin merely because template documents exist. The selected implementation scope must satisfy the readiness requirements defined in `AGENTS.md`, `docs/00-Project-Index.md`, and the Product Roadmap and Release Plan.

## Current Project Status

| Field | Current Position |
|---|---|
| Project phase | Project foundation and comprehensive documentation |
| Requirements status | Not yet completed |
| Target scope | Full enterprise platform |
| Solution type | To be determined after requirements and fit-gap analysis |
| Technology stack | Not selected |
| Implementation status | Not started |
| Current delivery mode | Documentation only |

## Repository Structure

```text
AGENTS.md
CLAUDE.md
docs/
├── 00-Project-Index.md
├── 01-Requirements/
├── 02-Solution-Design/
├── 03-UI-UX/
├── 04-QA-and-Testing/
└── 05-Agile-Delivery/
```

The detailed structure and documentation flow are controlled through `docs/00-Project-Index.md`.

## Working Rules

- Read `AGENTS.md` and `docs/00-Project-Index.md` before taking action.
- Treat the user's current explicit instruction as the highest-priority source.
- Do not invent requirements, approvals, roles, dates, technologies, fields, integrations, or test results.
- Keep confirmed facts, proposed decisions, assumptions, constraints, risks, gaps, and questions distinguishable.
- Preserve repository-wide identifiers and end-to-end traceability.
- Record missing information as an owned question, dependency, assumption, risk, or blocker.
- Do not commit directly to `main`.
- Do not merge a pull request without explicit user authorization.

## Documentation Quality

Pull requests validate Markdown quality, required files, and internal documentation references.

Run the repository checks with:

```bash
npx --yes markdownlint-cli2 '*.md' 'docs/**/*.md' '#node_modules'
python scripts/validate_docs.py
```
