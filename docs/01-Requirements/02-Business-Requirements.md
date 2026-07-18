# Business Requirements

## Purpose

Define the complete business requirements for the Environment Fund Enterprise Project Management Platform as an enterprise project portfolio management and project management information system.

This document describes the business context, target operating model, lifecycle processes, stakeholder needs, business capabilities, governance expectations, business information needs, exceptions, dependencies, and unresolved decisions. It is intentionally technology-neutral and does not authorize implementation, configuration, procurement, or a specific product.

## Document Information

| Field | Value |
|---|---|
| Project | Environment Fund Enterprise Project Management Platform |
| Arabic Name | منصة إدارة المشاريع المؤسسية لصندوق البيئة |
| Document Owner | TBD — to be confirmed by the Environment Fund |
| Prepared By | AI-assisted business analysis under user direction |
| Reviewed By | TBD — business, PMO, finance, procurement, IT, security, data, and other relevant owners |
| Version | 0.2 |
| Status | Draft |
| Classification | Internal |
| Last Updated | 2026-07-18 |

## Required Context

1. `docs/00-Project-Index.md`
2. `docs/01-Requirements/01-Project-Overview.md`
3. Authoritative Environment Fund policies, procedures, templates, approval matrices, reports, and current-state evidence when provided

## AI and Analysis Instructions

- Treat the user's explicit requirement for a complete enterprise system as the confirmed scope commitment.
- Keep current-state findings, confirmed requirements, proposed operating rules, assumptions, and open questions distinguishable.
- Do not confirm approval levels, monetary thresholds, named owners, target dates, technology, hosting, service levels, or source-system details without evidence.
- Use the business-requirement identifiers in this document as the baseline capability requirements derived from the confirmed full-scope direction.
- Candidate operating rules are not authoritative business rules until the relevant Environment Fund owner confirms them.
- Detailed functional behavior, fields, permissions, validations, interfaces, notifications, and acceptance criteria must be defined in `docs/01-Requirements/03-System-Requirements.md`.
- The target platform may be delivered incrementally, but the documented target-state capability set must remain complete.

## 1. Executive Summary

The Environment Fund requires a unified enterprise platform to govern and manage strategies, portfolios, programs, initiatives, projects, delivery work, resources, finances, contracts, risks, quality, decisions, documents, benefits, reporting, and organizational knowledge across the complete lifecycle.

The platform is intended to replace fragmented project information, inconsistent governance, manual follow-up, disconnected financial and delivery views, and limited portfolio-level insight with a controlled and traceable enterprise operating model.

The target state must support:

- strategy-to-execution alignment;
- demand intake, evaluation, prioritization, and authorization;
- portfolio, program, initiative, and project governance;
- predictive, Agile, and hybrid delivery models;
- schedule, scope, resource, financial, procurement, contract, risk, issue, change, quality, and deliverable control;
- executive, PMO, portfolio, program, project, functional, financial, and operational reporting;
- benefits realization and post-project evaluation;
- controlled collaboration, document management, decisions, actions, meetings, notifications, and escalation;
- enterprise identity, access, audit, data governance, integration, records, and operational controls; and
- complete traceability from strategic objective through requirement, delivery, acceptance, outcome, and benefit.

The solution must function as an enterprise management platform and authoritative business view of project performance. It must not be reduced to a task tracker, document repository, dashboard-only solution, or limited MVP.

## 2. Business Context

### 2.1 Organizational Context

The Environment Fund operates enterprise initiatives and projects that may involve multiple business areas, shared-service functions, internal teams, external suppliers, consultants, contracts, budgets, approvals, deliverables, risks, regulatory obligations, and strategic outcomes.

Projects may differ in:

- strategic importance;
- financial value;
- duration and complexity;
- delivery method;
- regulatory or mandatory nature;
- number of participating entities;
- sourcing and contracting model;
- technology involvement;
- data sensitivity;
- operational criticality; and
- expected financial, institutional, environmental, or service impact.

The target platform must therefore support configurable governance proportional to project type, risk, value, complexity, and delivery model without fragmenting information across separate uncontrolled tools.

### 2.2 Business Drivers

The principal business drivers are:

1. Establish one trusted enterprise register for all demands, initiatives, programs, projects, and related work.
2. Improve strategic alignment and investment prioritization.
3. Standardize governance while allowing approved variations by project type.
4. Improve visibility of schedule, cost, scope, quality, risk, contract, and benefit performance.
5. Support evidence-based executive and portfolio decisions.
6. Strengthen accountability, ownership, approvals, and escalation.
7. Connect delivery performance with financial, procurement, contract, document, identity, and analytics information.
8. Reduce manual consolidation, duplicate entry, spreadsheet dependency, and inconsistent reporting.
9. Preserve institutional knowledge, decisions, history, and lessons learned.
10. Improve the reliability, timeliness, and auditability of project information.

### 2.3 Business Outcomes

The target operating model is expected to enable:

- a complete and current portfolio view;
- consistent project initiation and authorization;
- transparent prioritization and resource allocation;
- controlled baselines and changes;
- earlier identification of delays, cost pressure, risks, and contract concerns;
- more reliable status reporting;
- improved deliverable acceptance and closure discipline;
- stronger supplier accountability;
- measurable benefit ownership and realization;
- reduced reporting effort;
- improved audit readiness; and
- reusable knowledge for future projects.

## 3. Current State — As-Is

### 3.1 Evidence Status

A complete current-state assessment has not yet been supplied. The following statements are analysis hypotheses and validation areas, not confirmed findings unless supported by later evidence.

Required current-state evidence includes:

- project-management policies and procedures;
- portfolio, program, and project governance documents;
- project intake forms and evaluation criteria;
- approval matrices and committee terms of reference;
- project charter, plan, status, risk, issue, change, and closure templates;
- current portfolio and project registers;
- current dashboards and reports;
- spreadsheet and collaboration-tool examples;
- financial, procurement, contract, receipt, invoice, and payment processes;
- current document and correspondence practices;
- current roles and organizational responsibilities;
- sample project records across different project types; and
- known audit, compliance, quality, or management observations.

### 3.2 Current-State Assessment Areas

| Area | Current-State Questions | Potential Business Impact if Fragmented |
|---|---|---|
| Demand intake | Where are ideas and project requests submitted, classified, and tracked? | Lost requests, inconsistent evaluation, duplicate work |
| Strategic alignment | How are projects linked to objectives and initiatives? | Weak prioritization and unclear strategic contribution |
| Portfolio governance | How are projects compared, selected, deferred, suspended, or terminated? | Suboptimal investment and capacity allocation |
| Project initiation | Are charters, sponsors, owners, and success criteria consistently established? | Ambiguous accountability and unstable scope |
| Planning | Are scope, WBS, schedule, resources, cost, procurement, quality, and risk plans integrated? | Unreliable baselines and hidden dependencies |
| Delivery tracking | How are tasks, milestones, deliverables, and progress updated? | Delayed reporting and inconsistent progress measures |
| Financial visibility | How are budgets, commitments, actuals, forecasts, and invoices connected to delivery? | Incomplete cost view and late corrective action |
| Contracts and suppliers | How are supplier obligations, deliverables, performance, changes, and claims tracked? | Contract leakage and weak supplier accountability |
| Risks and issues | Are risks, issues, actions, decisions, and escalations centrally maintained? | Delayed response and loss of decision history |
| Change control | How are scope, time, cost, and benefit changes assessed and approved? | Uncontrolled baseline movement |
| Status reporting | How are project reports prepared, reviewed, and consolidated? | High manual effort and inconsistent executive information |
| Documents and records | Where are authoritative records stored and versioned? | Duplicate files, weak traceability, records risk |
| Benefits | Are benefits assigned, measured, and tracked after delivery? | Projects judged by outputs rather than outcomes |
| Closure | Are contractual, financial, operational, knowledge, and benefit obligations completed? | Open liabilities and incomplete transition |
| Data and audit | Can the organization reconstruct who changed, approved, or decided what and when? | Audit and accountability gaps |

### 3.3 Typical Current-State Risks Requiring Validation

- Multiple uncontrolled project lists.
- Inconsistent project identifiers and classification.
- Manual aggregation of portfolio reports.
- Subjective or inconsistent health assessments.
- Limited connection between progress and financial information.
- Unclear ownership of overdue decisions and actions.
- Status updates based on narrative rather than evidence.
- Baseline changes not consistently distinguished from forecast updates.
- Supplier deliverables and project deliverables tracked separately.
- Benefits not assigned to accountable owners.
- Closed projects retaining open contracts, invoices, risks, or actions.
- Limited ability to compare projects using consistent metrics.
- Important knowledge remaining in email, personal folders, or individual files.

## 4. Target State — To-Be

### 4.1 Target Operating Model

The target platform must support the following end-to-end lifecycle:

```text
Strategy and objectives
→ Demand, idea, request, or opportunity
→ Triage and classification
→ Business case and feasibility
→ Evaluation, scoring, and prioritization
→ Portfolio decision and authorization
→ Program, initiative, or project creation
→ Charter and governance setup
→ Integrated planning and baselining
→ Procurement, contracting, and mobilization
→ Execution and collaboration
→ Monitoring, control, forecasting, and reporting
→ Deliverable review and acceptance
→ Operational transition and project closure
→ Benefit realization and post-project evaluation
→ Knowledge capture and portfolio learning
```

### 4.2 Target-State Principles

1. **Single enterprise view:** all governed work must be discoverable through one controlled register.
2. **Strategy-to-value traceability:** projects must connect to objectives, outputs, outcomes, benefits, and measures.
3. **Proportionate governance:** controls must be configurable according to project characteristics.
4. **Authoritative ownership:** every material record must have a defined accountable role or owner.
5. **Controlled lifecycle:** state changes, approvals, rejections, returns, suspensions, terminations, and closures must be traceable.
6. **Integrated control:** scope, schedule, resources, finance, procurement, contracts, quality, risk, and benefits must be understood together.
7. **Evidence-based status:** reported progress and completion must be supported by defined evidence.
8. **Separation of plan, baseline, actual, and forecast:** each must remain distinguishable.
9. **Exception visibility:** overdue, blocked, breached, rejected, failed, and at-risk conditions must be visible and actionable.
10. **Enterprise records and auditability:** decisions, approvals, changes, and evidence must be retained according to applicable requirements.
11. **Role-based usability:** each user must receive information and actions appropriate to role and data scope.
12. **Technology neutrality:** business requirements must not be constrained by an unconfirmed product or implementation approach.

### 4.3 Enterprise Hierarchy

The business hierarchy must support, when applicable:

```text
Strategic Objective
└── Strategic Initiative
    └── Portfolio
        ├── Program
        │   ├── Project
        │   └── Project
        ├── Project
        └── Other Governed Work
```

The hierarchy must also support cross-cutting relationships such as:

- one project contributing to multiple strategic objectives;
- one benefit dependent on multiple projects;
- dependencies between projects in different portfolios;
- shared resources across programs and projects;
- contracts serving one or more projects;
- projects funded by one or more sources; and
- projects managed through predictive, Agile, or hybrid methods.

## 5. Business Process Catalog

| Process ID | Process | Trigger | Primary Outcome | Key Participants |
|---|---|---|---|---|
| BP-01 | Strategy and objective administration | Approved strategy or objective change | Governed strategic hierarchy and measures | Strategy owner, executive management, PMO |
| BP-02 | Demand and idea intake | New need, mandate, opportunity, issue, or proposal | Registered and classified demand | Requestor, business owner, PMO |
| BP-03 | Triage and duplication review | Submitted demand | Validated, returned, rejected, merged, or advanced request | PMO, subject-matter reviewers |
| BP-04 | Business case and feasibility | Qualified demand | Evidence for investment decision | Business owner, finance, IT, procurement, risk |
| BP-05 | Evaluation and prioritization | Complete business case | Ranked and scored candidate | Portfolio governance body |
| BP-06 | Portfolio decision | Prioritized candidate set | Approve, defer, reject, suspend, or request revision | Executive or delegated authority |
| BP-07 | Program or project initiation | Approved investment decision | Governed record, ownership, charter, and lifecycle | Sponsor, owner, PMO, project manager |
| BP-08 | Integrated planning | Authorized project | Approved scope, schedule, resource, cost, risk, procurement, quality, and communication plans | Project manager and functional owners |
| BP-09 | Procurement and mobilization | Approved sourcing need | Contracted and mobilized delivery capability | Project, procurement, contracts, finance, supplier |
| BP-10 | Execution and work management | Approved plan or sprint | Completed work and produced deliverables | Project team, supplier, manager |
| BP-11 | Monitoring, control, and forecasting | Active project | Current performance, forecast, exceptions, and actions | Project manager, PMO, sponsor |
| BP-12 | Risk, issue, dependency, and action control | Identified uncertainty or problem | Owned response and resolution | All governed roles |
| BP-13 | Change control | Proposed change | Approved, rejected, deferred, or returned change with impact | Change authority and affected owners |
| BP-14 | Deliverable review and acceptance | Submitted deliverable | Accepted, conditionally accepted, rejected, or returned deliverable | Business owner, quality, project, supplier |
| BP-15 | Status reporting and governance review | Reporting cycle or escalation | Approved factual status and decisions | Project, PMO, sponsor, committees |
| BP-16 | Project closure and transition | Completion or termination condition | Closed project with obligations transferred or resolved | Project, business owner, PMO, finance, procurement, operations |
| BP-17 | Benefit realization | Benefit measurement date or outcome event | Measured value and corrective action | Benefit owner, strategy, PMO |
| BP-18 | Knowledge and post-project evaluation | Closure or review milestone | Lessons, evaluation, and reusable knowledge | PMO, project participants, stakeholders |

## 6. Stakeholder Needs

| ID | Stakeholder / Role | Need | Business Value | Priority |
|---|---|---|---|---|
| SN-001 | Executive management | A concise enterprise view of portfolio health, value, risk, finance, delivery, and decisions required | Faster and better-informed governance decisions | Must |
| SN-002 | Portfolio governance body | Comparable information for prioritization, funding, continuation, suspension, and termination decisions | Optimized investment portfolio | Must |
| SN-003 | PMO | Standard governance, complete registers, compliance visibility, consolidated reporting, and intervention capability | Stronger project governance and control | Must |
| SN-004 | Portfolio manager | Portfolio composition, scenario, dependency, resource, risk, and benefit visibility | Better balancing and optimization | Must |
| SN-005 | Program manager | Coordinated project outcomes, shared dependencies, benefits, risks, and decisions | Realization of program-level value | Must |
| SN-006 | Project manager | One operational workspace for planning, control, collaboration, reporting, and evidence | Reduced administration and improved delivery control | Must |
| SN-007 | Project sponsor | Clear accountability, health, forecast, risks, decisions, and escalations | Effective sponsorship and timely intervention | Must |
| SN-008 | Business owner | Visibility and control of requirements, deliverables, acceptance, transition, outcomes, and benefits | Delivery of fit-for-purpose business value | Must |
| SN-009 | Team member | Clear assignments, priorities, due dates, dependencies, documents, and feedback | Efficient execution and accountability | Must |
| SN-010 | Resource or functional manager | Demand, availability, allocation, conflicts, skills, and forward capacity | Improved workforce planning | Must |
| SN-011 | Finance | Reliable connection between approved budgets, commitments, actuals, forecasts, receipts, invoices, and project performance | Financial control and forecasting | Must |
| SN-012 | Procurement and contracts | Project-linked sourcing, obligations, milestones, changes, performance, claims, and closure | Better commercial governance | Must |
| SN-013 | Risk, compliance, and audit | Traceable controls, decisions, approvals, changes, access, and evidence | Reduced control and audit risk | Must |
| SN-014 | Quality or assurance reviewer | Defined quality criteria, reviews, nonconformities, corrective actions, and acceptance evidence | Improved deliverable quality | Must |
| SN-015 | Data and analytics teams | Controlled, well-defined, timely, and traceable project data | Trusted analytics and reporting | Must |
| SN-016 | IT and application operations | Clear integration, identity, security, support, monitoring, and operational ownership | Sustainable operation | Must |
| SN-017 | Supplier or consultant | Controlled access to assigned work, deliverables, actions, issues, and communications | Improved external collaboration and accountability | Should |
| SN-018 | Employee or requestor | Simple submission and visibility of owned requests | Transparent demand process | Must |
| SN-019 | Records and document management | Correct classification, retention, versioning, and authoritative archival | Records compliance and retrieval | Must |
| SN-020 | Benefit owner | Baselines, targets, measurement dates, actual outcomes, and corrective actions | Accountability for realized value | Must |

## 7. Business Requirements

### 7.1 Strategy and Alignment

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-001 | The organization shall maintain a governed hierarchy of strategic themes, objectives, initiatives, outcomes, and performance measures relevant to project investment. | Establishes the strategic context for selection and evaluation. | Confirmed complete-scope direction | Must | Draft |
| BR-002 | Every governed demand, program, initiative, and project shall be linkable to one or more strategic objectives or explicitly classified as mandatory, operational, regulatory, corrective, or otherwise justified. | Prevents unaligned investment and preserves rationale. | Confirmed complete-scope direction | Must | Draft |
| BR-003 | The organization shall be able to define and evaluate the expected contribution of projects and programs to strategic objectives, outcomes, and measures. | Enables strategy-to-execution analysis. | Confirmed complete-scope direction | Must | Draft |
| BR-004 | Strategic changes shall support impact assessment on related portfolios, programs, projects, benefits, and priorities. | Maintains alignment when strategy changes. | Confirmed complete-scope direction | Must | Draft |

### 7.2 Demand, Idea, and Request Management

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-005 | The organization shall provide a controlled intake process for ideas, demands, mandates, opportunities, corrective initiatives, and project requests. | Creates one entry point and complete demand register. | Confirmed complete-scope direction | Must | Draft |
| BR-006 | Intake shall support configurable request types, required information, attachments, declarations, and routing based on request characteristics. | Supports different business needs without uncontrolled forms. | Confirmed complete-scope direction | Must | Draft |
| BR-007 | Requests shall be classified, screened for completeness, checked for duplication or overlap, and returned, merged, rejected, or advanced with traceable reasons. | Improves intake quality and avoids duplicate investment. | Confirmed complete-scope direction | Must | Draft |
| BR-008 | Requestors and authorized stakeholders shall be able to track request status, required actions, decisions, and outcomes. | Improves transparency and reduces manual follow-up. | Confirmed complete-scope direction | Must | Draft |

### 7.3 Business Case, Feasibility, Evaluation, and Prioritization

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-009 | Qualified requests shall support a business case covering need, objectives, options, scope, stakeholders, costs, resources, risks, dependencies, timing, expected outcomes, benefits, and recommended approach. | Provides evidence for investment decisions. | Confirmed complete-scope direction | Must | Draft |
| BR-010 | The organization shall support multidisciplinary feasibility and impact assessments, including business, financial, procurement, contractual, operational, technology, security, data, legal, compliance, and change impacts when applicable. | Avoids approval without understanding delivery implications. | Confirmed complete-scope direction | Must | Draft |
| BR-011 | Candidate investments shall be evaluated using configurable criteria, weights, scoring methods, evidence, reviewer comments, and conflict-of-interest controls where applicable. | Enables consistent, transparent evaluation. | Confirmed complete-scope direction | Must | Draft |
| BR-012 | Prioritization shall consider strategic contribution, mandatory nature, urgency, value, cost, risk, readiness, dependencies, resource demand, and portfolio constraints. | Supports balanced decisions rather than isolated rankings. | Confirmed complete-scope direction | Must | Draft |
| BR-013 | Decision authorities shall be able to approve, conditionally approve, defer, reject, return, suspend, or terminate a candidate with rationale and conditions. | Creates a controlled decision record. | Confirmed complete-scope direction | Must | Draft |
| BR-014 | Evaluation and prioritization history shall be retained to explain changes in rank, score, decision, and portfolio composition over time. | Supports transparency and auditability. | Confirmed complete-scope direction | Must | Draft |

### 7.4 Portfolio Management

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-015 | The organization shall maintain one or more portfolios grouping programs, projects, initiatives, and other governed work according to approved management needs. | Enables enterprise and delegated portfolio governance. | Confirmed complete-scope direction | Must | Draft |
| BR-016 | Portfolio managers shall be able to evaluate portfolio composition across value, risk, cost, capacity, timing, strategic alignment, mandatory commitments, and benefit contribution. | Supports portfolio optimization. | Confirmed complete-scope direction | Must | Draft |
| BR-017 | Portfolio governance shall support scenario comparison, including the impact of approving, deferring, suspending, accelerating, reducing, or terminating investments. | Improves investment trade-off decisions. | Confirmed complete-scope direction | Must | Draft |
| BR-018 | Portfolio performance shall aggregate project and program schedule, financial, risk, resource, quality, benefit, contract, and health information without losing drill-down traceability. | Provides a reliable executive view. | Confirmed complete-scope direction | Must | Draft |
| BR-019 | Portfolio reviews shall capture decisions, conditions, actions, owners, due dates, and subsequent completion. | Converts governance meetings into controlled action. | Confirmed complete-scope direction | Must | Draft |
| BR-020 | Portfolio constraints, targets, thresholds, and planning periods shall be configurable and historically traceable. | Supports changing strategic and financial planning contexts. | Confirmed complete-scope direction | Must | Draft |

### 7.5 Program Management

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-021 | Related projects shall be manageable as a program when coordinated management is required to realize shared outcomes or benefits. | Supports value that cannot be managed project by project. | Confirmed complete-scope direction | Must | Draft |
| BR-022 | Programs shall maintain objectives, components, roadmap, interdependencies, shared risks, shared resources, governance, outcomes, benefits, and transition responsibilities. | Establishes complete program control. | Confirmed complete-scope direction | Must | Draft |
| BR-023 | Program performance shall aggregate component performance while preserving component-level accountability and traceability. | Supports effective program oversight. | Confirmed complete-scope direction | Must | Draft |
| BR-024 | Program changes and decisions shall support impact assessment across affected component projects and benefits. | Prevents isolated decisions from harming program outcomes. | Confirmed complete-scope direction | Must | Draft |

### 7.6 Project Initiation, Classification, and Governance

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-025 | Every approved project shall receive a unique identifier and governed classification, ownership, sponsorship, management, organization, lifecycle, and reporting profile. | Establishes accountability and consistent control. | Confirmed complete-scope direction | Must | Draft |
| BR-026 | Project classification shall support configurable dimensions such as type, value, complexity, risk, strategic importance, delivery model, funding source, confidentiality, and mandatory status. | Enables proportionate governance and analysis. | Confirmed complete-scope direction | Must | Draft |
| BR-027 | Every project shall maintain a charter or equivalent authorization record defining purpose, objectives, scope, success criteria, major deliverables, key milestones, assumptions, constraints, risks, budget context, sponsor, owner, and manager. | Prevents uncontrolled initiation. | Confirmed complete-scope direction | Must | Draft |
| BR-028 | Governance requirements, stage gates, review bodies, mandatory evidence, and approval paths shall be configurable by project classification. | Applies the right level of control. | Confirmed complete-scope direction | Must | Draft |
| BR-029 | Gate reviews shall support readiness criteria, evidence review, comments, conditions, approval, rejection, return for rework, waiver where authorized, and escalation. | Makes lifecycle progression controlled and auditable. | Confirmed complete-scope direction | Must | Draft |
| BR-030 | Project state, health, governance status, and delivery status shall remain distinct so that administrative state does not hide performance concerns. | Improves reporting accuracy. | Confirmed complete-scope direction | Must | Draft |

### 7.7 Scope, Requirements, Deliverables, and WBS

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-031 | Projects shall maintain approved in-scope and out-of-scope boundaries, objectives, requirements, deliverables, acceptance criteria, and assumptions. | Establishes the basis for planning and change control. | Confirmed complete-scope direction | Must | Draft |
| BR-032 | Scope shall be decomposable into a work breakdown structure, work packages, deliverables, activities, and accountable owners appropriate to the delivery model. | Enables integrated planning and control. | Confirmed complete-scope direction | Must | Draft |
| BR-033 | Requirements and deliverables shall support traceability to business objectives, contracts, work, tests, acceptance, changes, and benefits where applicable. | Prevents unverified or orphaned scope. | Confirmed complete-scope direction | Must | Draft |
| BR-034 | The organization shall distinguish approved baseline scope from proposed, forecast, superseded, cancelled, and completed scope. | Preserves baseline integrity. | Confirmed complete-scope direction | Must | Draft |

### 7.8 Schedule, Milestones, and Dependencies

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-035 | Projects shall maintain an integrated schedule covering phases, activities, tasks, milestones, deliverables, dependencies, constraints, calendars, durations, and responsible parties. | Establishes a complete delivery plan. | Confirmed complete-scope direction | Must | Draft |
| BR-036 | The schedule shall distinguish baseline, current plan, actual dates, remaining work, and forecast dates. | Enables reliable variance and forecast analysis. | Confirmed complete-scope direction | Must | Draft |
| BR-037 | Projects shall identify critical and near-critical activities, external dependencies, key constraints, and milestone exposure. | Supports proactive intervention. | Confirmed complete-scope direction | Must | Draft |
| BR-038 | Cross-project and cross-program dependencies shall be centrally visible, jointly owned, and escalated when dates or conditions are at risk. | Reduces enterprise dependency failure. | Confirmed complete-scope direction | Must | Draft |
| BR-039 | Schedule changes affecting approved commitments shall be controlled through the applicable change and governance process. | Protects approved baselines. | Confirmed complete-scope direction | Must | Draft |

### 7.9 Work, Task, Agile, and Hybrid Delivery

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-040 | The platform shall support detailed work and task management with ownership, dates, priority, status, dependencies, checklists, evidence, comments, and completion criteria. | Enables day-to-day execution within enterprise governance. | Confirmed complete-scope direction | Must | Draft |
| BR-041 | Teams shall be able to manage work through list, board, calendar, timeline, and other appropriate views without creating conflicting sources of truth. | Supports different working styles with common data. | Confirmed complete-scope direction | Should | Draft |
| BR-042 | Agile delivery shall support product backlogs, epics, features, stories, iterations or sprints, goals, estimates, boards, reviews, retrospectives, and delivery metrics where applicable. | Supports adaptive delivery. | Confirmed complete-scope direction | Must | Draft |
| BR-043 | Hybrid projects shall be able to connect Agile delivery work to governed project milestones, deliverables, budgets, risks, changes, and reporting. | Prevents separation between Agile execution and enterprise governance. | Confirmed complete-scope direction | Must | Draft |
| BR-044 | Work completion shall roll up according to defined progress methods rather than one universal calculation. | Supports different types of work and reliable progress. | Confirmed complete-scope direction | Must | Draft |

### 7.10 Resource, Capacity, Skills, and Time

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-045 | The organization shall maintain resource demand by role, skill, period, organizational unit, location, source, and project need where applicable. | Enables capacity planning. | Confirmed complete-scope direction | Must | Draft |
| BR-046 | Resource managers shall be able to compare demand, availability, allocation, actual utilization, conflicts, and future capacity. | Improves allocation decisions. | Confirmed complete-scope direction | Must | Draft |
| BR-047 | Projects shall support named and generic resource planning, assignment, replacement, delegation, and release. | Supports planning before and after staffing. | Confirmed complete-scope direction | Must | Draft |
| BR-048 | Skills, qualifications, experience, availability, and role suitability shall be usable in resource planning when authoritative data is available. | Improves resource fit. | Confirmed complete-scope direction | Should | Draft |
| BR-049 | Time entry and approval shall be supported where required, including project, task, period, category, correction, rejection, and locking controls. | Supports effort, utilization, and cost analysis. | Confirmed complete-scope direction | Should | Draft |
| BR-050 | Resource and time information shall respect employment, privacy, access, and system-of-record boundaries. | Protects sensitive workforce information. | Confirmed complete-scope direction | Must | Draft |

### 7.11 Budget, Cost, Forecast, and Earned Value

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-051 | Projects, programs, and portfolios shall maintain approved budget context, planning periods, cost categories, funding sources, and responsible financial dimensions as applicable. | Establishes financial accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-052 | The business view shall distinguish original budget, current approved budget, planned cost, commitment, obligation, actual cost, accrual where applicable, forecast, estimate to complete, and estimate at completion. | Prevents misleading financial reporting. | Confirmed complete-scope direction | Must | Draft |
| BR-053 | Financial information shall be traceable to the authoritative financial and procurement sources while supporting project-level analysis and forecasting. | Preserves source-of-truth integrity. | Confirmed complete-scope direction | Must | Draft |
| BR-054 | Projects shall monitor cost variance, forecast variance, cash-flow timing, funding constraints, and threshold breaches. | Enables timely corrective action. | Confirmed complete-scope direction | Must | Draft |
| BR-055 | Budget transfers, revisions, and forecast changes shall remain distinguishable and follow applicable approval and audit controls. | Protects financial governance. | Confirmed complete-scope direction | Must | Draft |
| BR-056 | Earned value management shall be supported for projects where it is required, using approved scope, schedule, budget, progress, and actual cost information. | Provides integrated performance measurement for suitable projects. | Confirmed complete-scope direction | Should | Draft |
| BR-057 | Portfolio and program views shall aggregate financial performance without double counting shared contracts, funding, or costs. | Ensures reliable consolidated reporting. | Confirmed complete-scope direction | Must | Draft |

### 7.12 Procurement, Contracts, Suppliers, Receipts, and Payments

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-058 | Project plans shall identify procurement needs, sourcing milestones, required approvals, dependencies, and expected contract dates. | Integrates procurement with delivery planning. | Confirmed complete-scope direction | Must | Draft |
| BR-059 | Projects shall be linkable to procurement requests, competitions, evaluations, awards, contracts, purchase orders, receipts, invoices, and payments when applicable. | Provides end-to-end commercial visibility. | Confirmed complete-scope direction | Must | Draft |
| BR-060 | Contract records shall expose relevant obligations, deliverables, milestones, values, dates, guarantees, service levels, changes, claims, penalties, renewals, and closure conditions according to access rights. | Strengthens contract control. | Confirmed complete-scope direction | Must | Draft |
| BR-061 | Supplier performance shall be measurable across delivery, timeliness, quality, responsiveness, compliance, risk, and commercial obligations. | Enables objective supplier management. | Confirmed complete-scope direction | Must | Draft |
| BR-062 | Contract and purchase-order changes shall be assessed for project scope, schedule, cost, risk, benefit, and delivery impact. | Connects commercial changes with project control. | Confirmed complete-scope direction | Must | Draft |
| BR-063 | Receipt, completion-certificate, invoice, and payment visibility shall be linked to accepted work and applicable approvals without replacing authoritative financial processes. | Reduces payment and acceptance disconnects. | Confirmed complete-scope direction | Must | Draft |
| BR-064 | Project and contract closure shall identify unresolved obligations, claims, guarantees, invoices, retention, assets, documents, and supplier actions. | Prevents premature closure. | Confirmed complete-scope direction | Must | Draft |

### 7.13 Deliverables, Quality, Review, and Acceptance

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-065 | Every material deliverable shall have an owner, producer, due date, version, acceptance criteria, reviewers, status, evidence, and contractual relationship where applicable. | Makes outputs controlled and accountable. | Confirmed complete-scope direction | Must | Draft |
| BR-066 | Deliverable review shall support submission, completeness check, review cycles, comments, rejection, return, resubmission, conditional acceptance, and final acceptance. | Provides controlled quality and acceptance. | Confirmed complete-scope direction | Must | Draft |
| BR-067 | Quality planning shall define applicable standards, methods, review points, responsibilities, evidence, and acceptance thresholds. | Prevents quality from being assessed only at the end. | Confirmed complete-scope direction | Must | Draft |
| BR-068 | Quality findings, nonconformities, observations, corrective actions, preventive actions, and retests shall be tracked to closure. | Supports quality improvement and evidence. | Confirmed complete-scope direction | Must | Draft |
| BR-069 | Completion and acceptance shall remain distinguishable; completed production work shall not automatically constitute business or contractual acceptance. | Prevents false completion. | Confirmed complete-scope direction | Must | Draft |

### 7.14 Risk, Issue, Assumption, Constraint, Dependency, and Action Management

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-070 | Projects, programs, and portfolios shall maintain governed registers for risks, issues, assumptions, constraints, dependencies, and actions. | Establishes consistent control of uncertainty and impediments. | Confirmed complete-scope direction | Must | Draft |
| BR-071 | Risks shall capture cause, event, impact, category, likelihood, consequence, exposure, response, owner, due dates, triggers, controls, residual exposure, and review history as applicable. | Enables structured risk management. | Confirmed complete-scope direction | Must | Draft |
| BR-072 | Issues shall capture impact, urgency, priority, ownership, containment, resolution, target date, escalation, and closure evidence. | Supports timely resolution. | Confirmed complete-scope direction | Must | Draft |
| BR-073 | Dependencies shall identify provider, receiver, required condition or deliverable, date, status, impact, and escalation ownership. | Makes dependency obligations explicit. | Confirmed complete-scope direction | Must | Draft |
| BR-074 | Assumptions and constraints shall be reviewed and converted to risks, issues, changes, or decisions when their status changes. | Maintains accurate planning context. | Confirmed complete-scope direction | Must | Draft |
| BR-075 | Thresholds and escalation paths shall be configurable by governance context and must not be silently inferred. | Supports proportionate and approved escalation. | Confirmed complete-scope direction | Must | Draft |
| BR-076 | Enterprise views shall identify common, systemic, correlated, or cascading risks and issues across projects. | Supports portfolio-level intervention. | Confirmed complete-scope direction | Should | Draft |

### 7.15 Change and Baseline Control

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-077 | Proposed changes shall be formally registered and classified by type, urgency, source, affected scope, and governance path. | Establishes a controlled change register. | Confirmed complete-scope direction | Must | Draft |
| BR-078 | Change assessment shall consider scope, requirements, schedule, cost, resources, procurement, contracts, quality, risk, operations, stakeholders, data, security, benefits, and dependencies as applicable. | Supports informed decisions. | Confirmed complete-scope direction | Must | Draft |
| BR-079 | Change decisions shall capture approval, rejection, deferral, return, conditions, rationale, decision authority, date, and required follow-up. | Preserves decision accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-080 | Approved changes shall update affected baselines, forecasts, plans, contracts, requirements, risks, benefits, and communications in a controlled manner. | Maintains internal consistency. | Confirmed complete-scope direction | Must | Draft |
| BR-081 | Superseded baseline values shall remain historically available and distinguishable from current approved values. | Enables audit and trend analysis. | Confirmed complete-scope direction | Must | Draft |

### 7.16 Meetings, Committees, Decisions, Communications, and Stakeholders

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-082 | Projects and governance bodies shall be able to plan and record meetings, agendas, participants, attendance, materials, minutes, decisions, actions, and follow-up. | Converts meetings into traceable governance records. | Confirmed complete-scope direction | Must | Draft |
| BR-083 | Decisions shall record the question, options, analysis, recommendation, authority, rationale, date, affected items, conditions, and resulting actions. | Preserves institutional decision history. | Confirmed complete-scope direction | Must | Draft |
| BR-084 | Actions shall have an owner, due date, priority, source, status, evidence, escalation, and closure record. | Improves accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-085 | Stakeholder management shall identify stakeholder roles, influence, interest, expectations, engagement approach, communication needs, concerns, and feedback. | Supports adoption and delivery success. | Confirmed complete-scope direction | Must | Draft |
| BR-086 | Communication plans shall define audiences, messages, channels, frequency, ownership, confidentiality, and evidence where required. | Ensures consistent communication. | Confirmed complete-scope direction | Must | Draft |
| BR-087 | Sensitive governance discussions and records shall be restricted according to approved access and classification rules. | Protects confidential decisions. | Confirmed complete-scope direction | Must | Draft |

### 7.17 Documents, Records, Templates, Search, and Knowledge

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-088 | The organization shall maintain controlled project document and record structures aligned with project type, lifecycle, classification, and records obligations. | Improves consistency and retrieval. | Confirmed complete-scope direction | Must | Draft |
| BR-089 | Documents shall support ownership, classification, version, status, review, approval, relationships, retention, archival, and authoritative-location references. | Preserves record integrity. | Confirmed complete-scope direction | Must | Draft |
| BR-090 | Approved templates shall be centrally managed, versioned, effective-dated, and applicable by project or process type. | Standardizes delivery artifacts. | Confirmed complete-scope direction | Must | Draft |
| BR-091 | Users shall be able to search authorized projects, records, decisions, risks, actions, contracts, deliverables, lessons, and related information using structured and text-based criteria. | Reduces retrieval effort and knowledge loss. | Confirmed complete-scope direction | Must | Draft |
| BR-092 | Lessons learned and reusable knowledge shall be captured throughout delivery and at closure, categorized, reviewed, and discoverable for future work. | Builds organizational capability. | Confirmed complete-scope direction | Must | Draft |
| BR-093 | Authoritative records may reside in connected enterprise repositories; the platform shall preserve clear references and ownership rather than create uncontrolled duplicates. | Maintains records and system-of-record integrity. | Confirmed complete-scope direction | Must | Draft |

### 7.18 Status Reporting, Dashboards, Analytics, Alerts, and Escalation

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-094 | Projects shall produce governed periodic and event-driven status reports covering achievements, next work, scope, schedule, cost, resources, procurement, contracts, deliverables, quality, risks, issues, changes, dependencies, decisions, and support required. | Creates a complete factual status view. | Confirmed complete-scope direction | Must | Draft |
| BR-095 | Status reports shall distinguish system-derived facts, manager assessment, narrative explanation, forecast, and decisions requested. | Improves transparency and trust. | Confirmed complete-scope direction | Must | Draft |
| BR-096 | Health indicators and thresholds shall be defined, explainable, configurable, and historically traceable. | Prevents arbitrary red-amber-green reporting. | Confirmed complete-scope direction | Must | Draft |
| BR-097 | Executive and management dashboards shall support drill-down from enterprise and portfolio summaries to the underlying project, record, transaction, evidence, or decision where authorized. | Supports actionable oversight. | Confirmed complete-scope direction | Must | Draft |
| BR-098 | Users shall be able to filter, compare, group, trend, save, export, and schedule authorized reports according to business need. | Supports analysis and recurring governance. | Confirmed complete-scope direction | Must | Draft |
| BR-099 | Alerts, reminders, and escalations shall be generated for defined deadlines, breaches, approvals, risks, issues, actions, contracts, deliverables, reports, and governance conditions. | Reduces missed obligations. | Confirmed complete-scope direction | Must | Draft |
| BR-100 | Notification recipients, channels, timing, frequency, escalation, suppression, and acknowledgment rules shall be configurable and governed. | Avoids notification overload and missed critical events. | Confirmed complete-scope direction | Must | Draft |

### 7.19 Benefits, Outcomes, Value, and Post-Project Evaluation

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-101 | Programs and projects shall define expected outputs, outcomes, benefits, disbenefits, value measures, baselines, targets, owners, dependencies, and realization dates. | Connects delivery to organizational value. | Confirmed complete-scope direction | Must | Draft |
| BR-102 | Benefit ownership shall continue beyond project closure where realization occurs later. | Prevents closure from ending value accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-103 | Benefit realization shall support planned, forecast, actual, delayed, at-risk, not realized, and no-longer-applicable states with rationale. | Enables truthful value reporting. | Confirmed complete-scope direction | Must | Draft |
| BR-104 | Post-project and post-program evaluation shall compare intended and actual outcomes, benefits, cost, schedule, quality, adoption, sustainability, and lessons. | Improves future investment and delivery decisions. | Confirmed complete-scope direction | Must | Draft |
| BR-105 | Portfolio governance shall be able to evaluate realized and forecast value across investments and use the results in future prioritization. | Creates a learning investment cycle. | Confirmed complete-scope direction | Must | Draft |

### 7.20 Closure, Transition, and Operational Readiness

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-106 | Project closure shall be governed by defined completion criteria covering scope, acceptance, contracts, finance, assets, data, documents, access, risks, issues, actions, knowledge, support, and benefits. | Prevents incomplete administrative closure. | Confirmed complete-scope direction | Must | Draft |
| BR-107 | Operational transition shall identify receiving owners, services, procedures, training, support, access, monitoring, continuity, unresolved items, and acceptance evidence. | Supports sustainable adoption. | Confirmed complete-scope direction | Must | Draft |
| BR-108 | Projects may be closed as completed, terminated, cancelled, merged, or otherwise concluded only with an authorized reason and disposition of open obligations. | Preserves accountability for non-standard closure. | Confirmed complete-scope direction | Must | Draft |
| BR-109 | Closure shall preserve an immutable historical view of baselines, actuals, decisions, changes, acceptance, outcomes, and residual obligations. | Supports audit and learning. | Confirmed complete-scope direction | Must | Draft |
| BR-110 | Reopening a closed item shall require controlled authorization, reason, scope, and audit history. | Protects historical integrity. | Confirmed complete-scope direction | Must | Draft |

### 7.21 Organization, Roles, Access, Delegation, and Audit

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-111 | The business shall define enterprise, portfolio, program, project, functional, assurance, financial, procurement, supplier, administrative, and read-only roles. | Establishes responsibility and access design. | Confirmed complete-scope direction | Must | Draft |
| BR-112 | Access shall support role, organization, portfolio, program, project, record, classification, relationship, and workflow context as applicable. | Provides appropriate data scope. | Confirmed complete-scope direction | Must | Draft |
| BR-113 | Delegation and acting assignments shall be time-bound, traceable, revocable, and limited to authorized responsibilities. | Supports continuity without uncontrolled access. | Confirmed complete-scope direction | Must | Draft |
| BR-114 | Segregation-of-duties conflicts shall be identified and governed for sensitive creation, evaluation, approval, acceptance, financial, contract, administrative, and audit activities. | Reduces fraud and control risk. | Confirmed complete-scope direction | Must | Draft |
| BR-115 | Material create, update, delete, approve, reject, delegate, export, access, configuration, and integration events shall be auditable according to approved requirements. | Establishes accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-116 | Historical records shall identify the acting user, represented role, timestamp, action, previous and new values where applicable, source, and correlation context. | Supports investigation and reconstruction. | Confirmed complete-scope direction | Must | Draft |

### 7.22 Data, Integration, Administration, and Configuration

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-117 | The organization shall define authoritative ownership and system-of-record responsibility for each major data domain. | Prevents conflicting records and duplicate maintenance. | Confirmed complete-scope direction | Must | Draft |
| BR-118 | Business data shall use controlled identifiers, classifications, reference values, effective dates, lifecycle states, quality rules, and ownership. | Improves consistency and analytics. | Confirmed complete-scope direction | Must | Draft |
| BR-119 | Integrations shall support traceable exchange, validation, reconciliation, failure visibility, recovery, and ownership. | Prevents silent data inconsistency. | Confirmed complete-scope direction | Must | Draft |
| BR-120 | The platform shall support governed configuration of project types, lifecycles, gates, forms, fields, statuses, priorities, scoring models, templates, workflows, calendars, thresholds, notifications, and reference data. | Enables controlled adaptation without uncontrolled customization. | Confirmed complete-scope direction | Must | Draft |
| BR-121 | Configuration changes shall be authorized, versioned, effective-dated, tested, and auditable. | Protects enterprise process integrity. | Confirmed complete-scope direction | Must | Draft |
| BR-122 | Business administrators shall be able to manage approved configuration within defined boundaries without unrestricted technical access. | Supports sustainable administration. | Confirmed complete-scope direction | Must | Draft |
| BR-123 | Data import, migration, correction, bulk update, and export shall follow approved validation, authorization, reconciliation, privacy, and audit controls. | Reduces data and compliance risk. | Confirmed complete-scope direction | Must | Draft |

### 7.23 User Experience, Language, Accessibility, and Collaboration

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-124 | The solution shall provide role-relevant home pages, work queues, dashboards, actions, and information priorities. | Reduces navigation and cognitive load. | Confirmed complete-scope direction | Must | Draft |
| BR-125 | The business experience shall support Arabic and English needs, including right-to-left and left-to-right behavior, terminology, dates, numbers, and mixed-language content. | Meets organizational language requirements. | Confirmed complete-scope direction | Must | Draft |
| BR-126 | The solution shall meet confirmed accessibility and inclusive-design requirements across navigation, forms, tables, charts, notifications, and interaction states. | Enables equitable and compliant use. | Confirmed complete-scope direction | Must | Draft |
| BR-127 | Users shall receive clear loading, empty, validation, error, denied, stale, conflict, success, and recovery states. | Prevents user uncertainty and data errors. | Confirmed complete-scope direction | Must | Draft |
| BR-128 | Collaboration shall support controlled comments, mentions, attachments, subscriptions, activity history, and contextual communication while preserving records and access rules. | Improves teamwork without losing governance. | Confirmed complete-scope direction | Must | Draft |

### 7.24 Intelligent and Advanced Capabilities

| ID | Requirement | Rationale / Value | Source | Priority | Status |
|---|---|---|---|---|---|
| BR-129 | The target state may support governed assistance for summarization, drafting, search, classification, extraction, anomaly detection, forecasting, risk identification, and decision support where separately justified. | Improves productivity and insight without embedding uncontrolled automation. | Confirmed complete-scope direction | Should | Draft |
| BR-130 | Intelligent outputs shall identify their source context, limitations, confidence or verification need, and accountable human decision point where applicable. | Protects decision quality and accountability. | Confirmed complete-scope direction | Must | Draft |
| BR-131 | Intelligent capabilities shall not bypass approved access, data classification, privacy, records, approval, audit, or human accountability controls. | Prevents new governance and data risks. | Confirmed complete-scope direction | Must | Draft |
| BR-132 | The organization shall be able to evaluate the accuracy, usefulness, grounding, safety, bias, failure modes, and operational performance of intelligent capabilities before and after release. | Enables controlled adoption. | Confirmed complete-scope direction | Must | Draft |

## 8. Candidate Business Rules Requiring Confirmation

The following are recommended operating rules. They are not authoritative Environment Fund rules and must not be promoted to the confirmed `RULE-*` register until reviewed by the relevant owner.

| Candidate Ref | Candidate Rule | Related Requirements | Confirmation Needed From |
|---|---|---|---|
| CBR-001 | A governed investment must have one accountable business owner and one accountable sponsor or approved equivalent. | BR-025, BR-027 | Governance owner |
| CBR-002 | A project may not enter active execution until required initiation and planning gates are satisfied or an authorized exception is recorded. | BR-028, BR-029 | PMO and governance body |
| CBR-003 | A baseline may not be overwritten; approved changes create a new controlled baseline version. | BR-034, BR-039, BR-081 | PMO and finance |
| CBR-004 | Project progress must use an approved measurement method and may not rely solely on subjective percentage completion. | BR-044, BR-094 | PMO |
| CBR-005 | A material deliverable may not be marked accepted without an authorized reviewer and retained acceptance evidence. | BR-065, BR-066, BR-069 | Business owner and contracts |
| CBR-006 | A project may not be closed while blocking contractual, financial, acceptance, operational, security, data, or records obligations remain unresolved unless an authorized disposition is recorded. | BR-064, BR-106, BR-108 | PMO, finance, procurement, operations |
| CBR-007 | Approved budget, commitment, actual, and forecast values must remain distinguishable. | BR-052, BR-055 | Finance |
| CBR-008 | A change requiring approval must not affect the active baseline before the decision is recorded. | BR-077 to BR-081 | Change authority |
| CBR-009 | Red or critical health conditions may not be manually overridden without reason, authority, and audit history. | BR-096, BR-115 | PMO and governance body |
| CBR-010 | Every risk, issue, dependency, and action above the approved threshold must have an owner and target response date. | BR-070 to BR-076 | PMO and risk owner |
| CBR-011 | Supplier completion does not by itself constitute business acceptance or financial entitlement. | BR-063, BR-065 to BR-069 | Procurement, contracts, finance, business owner |
| CBR-012 | Access to confidential projects and records must be explicitly granted and must not be inherited solely from general project roles. | BR-087, BR-112 | Security and data owner |
| CBR-013 | Delegated approval must identify the delegator, delegate, scope, validity period, and resulting decision history. | BR-113, BR-116 | Governance and HR |
| CBR-014 | Benefit ownership must be assigned before project authorization or by an approved gate, and must survive project closure. | BR-101, BR-102 | Strategy and business owner |
| CBR-015 | Cancellation or termination must record rationale, decision authority, financial and contractual impact, disposition of work, and residual obligations. | BR-013, BR-108 | Governance body |
| CBR-016 | Data synchronized from an authoritative system must not be edited locally unless an approved correction process exists. | BR-053, BR-117, BR-119 | Data owners |
| CBR-017 | Material governance decisions and approvals must not be deleted from the business history. | BR-083, BR-109, BR-115 | Records and audit |
| CBR-018 | Project templates and governance paths must be selected from approved versions applicable on the initiation date. | BR-028, BR-090, BR-120 | PMO |
| CBR-019 | A closed reporting period may be reopened only through an authorized and auditable process. | BR-049, BR-094, BR-115 | PMO and finance |
| CBR-020 | Intelligent recommendations must remain advisory unless a separately approved control permits automated action. | BR-129 to BR-132 | AI governance, security, business owner |

## 9. Business Data and Information Needs

### 9.1 Core Business Data Domains

| Data Domain | Business Purpose | Expected Ownership | Key Relationships |
|---|---|---|---|
| Strategy and objectives | Define strategic context and measures | Strategy owner — TBD | Portfolios, programs, projects, benefits |
| Demand and business case | Capture needs and investment rationale | Requesting business and PMO — TBD | Objectives, evaluations, decisions |
| Portfolio | Group and optimize investments | Portfolio owner — TBD | Programs, projects, scenarios, budgets |
| Program | Coordinate related projects and benefits | Program owner — TBD | Projects, dependencies, benefits |
| Project | Govern the delivery lifecycle | Project owner and PMO — TBD | All project records |
| Scope and requirements | Define intended work and outcomes | Business owner and project — TBD | Deliverables, WBS, tests, changes |
| Schedule and work | Plan and track execution | Project manager — TBD | Resources, deliverables, dependencies |
| Resources and time | Plan and account for effort | Functional and project owners — TBD | Projects, tasks, cost |
| Finance | Budget, commitment, actual, and forecast context | Finance — TBD | Projects, contracts, procurement |
| Procurement and contracts | Govern external sourcing and obligations | Procurement and contracts — TBD | Suppliers, deliverables, receipts |
| Deliverables and quality | Control outputs, reviews, and acceptance | Business owner and quality — TBD | Contracts, requirements, payments |
| Risks, issues, and changes | Control uncertainty and variance | Project and governance roles — TBD | Plans, decisions, actions |
| Decisions, meetings, and actions | Preserve governance history | Relevant governance owner — TBD | Projects, committees, exceptions |
| Documents and records | Preserve authoritative evidence | Records and document owner — TBD | All domains |
| Benefits and outcomes | Measure realized value | Benefit owner — TBD | Objectives, programs, projects |
| Identity and organization | Establish users, roles, and structure | HR and identity owners — TBD | Access, ownership, reporting |
| Audit and configuration | Preserve control and system history | System and audit owners — TBD | All domains |

### 9.2 Data Quality Needs

The business requires:

- unique and persistent identifiers;
- controlled reference data;
- clear ownership and stewardship;
- mandatory-field and relationship validation;
- effective dating and lifecycle status;
- duplicate detection and resolution;
- timeliness and freshness indicators;
- reconciliation with authoritative sources;
- historical traceability;
- correction without loss of original evidence;
- classification and sensitivity marking;
- retention and archival rules;
- completeness and consistency monitoring; and
- visible quality exceptions with owners and actions.

## 10. Reporting and Dashboard Needs

| ID | Report / Dashboard Need | Primary Users | Frequency / Trigger | Key Content |
|---|---|---|---|---|
| DR-001 | Enterprise portfolio dashboard | Executive management | On demand and governance cycle | Investment count, value, health, schedule, cost, risks, benefits, decisions |
| DR-002 | Portfolio composition and prioritization | Portfolio governance | Planning and review cycle | Scores, strategic fit, mandatory work, scenarios, capacity, funding |
| DR-003 | Program performance dashboard | Program management | Weekly or monthly — TBD | Component status, dependencies, outcomes, benefits, shared risks |
| DR-004 | Project one-page status | Sponsor, PMO, project manager | Reporting cycle | Scope, schedule, cost, risks, issues, changes, deliverables, decisions |
| DR-005 | Milestone and schedule variance | PMO and project managers | On demand and reporting cycle | Baseline, actual, forecast, variance, critical path, overdue milestones |
| DR-006 | Financial performance | Finance, PMO, sponsors | Financial and project cycle | Budget, commitment, actual, forecast, variance, cash flow |
| DR-007 | Procurement and contract dashboard | Procurement, contracts, PMO | On demand and reporting cycle | Requests, awards, contracts, obligations, changes, receipts, invoices |
| DR-008 | Supplier performance | Procurement, project owners | Periodic and contract milestone | Timeliness, quality, compliance, issues, penalties, evaluation |
| DR-009 | Deliverable and acceptance dashboard | Business owners, PMO | On demand | Due, submitted, under review, rejected, accepted, overdue |
| DR-010 | Risk exposure dashboard | Executives, PMO, risk owners | On demand and risk cycle | Heat map, trends, top risks, response status, residual exposure |
| DR-011 | Issue and escalation dashboard | Sponsors, PMO, managers | On demand | Critical issues, overdue resolution, decisions required |
| DR-012 | Change control dashboard | Change authority and PMO | On demand | Change count, impact, status, aging, decision, baseline effect |
| DR-013 | Resource demand and capacity | Portfolio and resource managers | Planning cycle | Demand, supply, allocation, conflicts, skills, utilization |
| DR-014 | Timesheet and effort report | Project and resource managers | Periodic | Submitted, approved, rejected, missing, effort by project and task |
| DR-015 | Governance and gate readiness | PMO and committees | Gate cycle | Required evidence, criteria, gaps, conditions, decisions |
| DR-016 | Status-report compliance | PMO | Reporting cycle | Due, submitted, reviewed, returned, overdue reports |
| DR-017 | Decisions and actions | Executives, committees, project managers | On demand | Open decisions, overdue actions, owner, source, escalation |
| DR-018 | Strategic alignment and contribution | Strategy and executives | Planning and review cycle | Objective contribution, initiative progress, investment distribution |
| DR-019 | Benefits-realization dashboard | Strategy, benefit owners, executives | Benefit measurement cycle | Baseline, target, forecast, actual, status, owner, corrective action |
| DR-020 | Project closure readiness | PMO, finance, procurement, operations | Closure event | Acceptance, contracts, finance, risks, documents, transition, benefits |
| DR-021 | Lessons and post-project evaluation | PMO and delivery community | Closure and periodic | Lessons, root causes, recommendations, outcome comparison |
| DR-022 | Data quality and integration exceptions | Data, IT, business owners | Continuous or scheduled | Failed sync, stale data, reconciliation differences, ownership |
| DR-023 | Audit and access activity | Audit, security, system owners | On demand and review cycle | Sensitive changes, approvals, access, delegation, exports |
| DR-024 | Administrative configuration report | System and business administrators | On demand | Active templates, workflows, rules, versions, effective dates |
| DR-025 | Personal work and approval dashboard | All users | Daily or on demand | Assigned tasks, approvals, reviews, actions, alerts, deadlines |

## 11. Business Exceptions and Edge Cases

| ID | Scenario | Expected Business Handling | Related Requirements |
|---|---|---|---|
| EX-001 | A request is incomplete. | Return to the requestor with missing items, due date, and retained history. | BR-005 to BR-008 |
| EX-002 | A new request duplicates an existing project or demand. | Flag, compare, and allow authorized merge, link, reject, or continue decision. | BR-007 |
| EX-003 | A mandatory project has low scoring. | Preserve mandatory rationale and allow prioritization rules to distinguish mandatory from discretionary work. | BR-012, BR-013 |
| EX-004 | A project contributes to multiple objectives or portfolios. | Support multiple relationships without duplicate project records or double counting. | BR-002, BR-015, BR-057 |
| EX-005 | Project ownership changes. | Transfer ownership with effective date, notification, handover, and retained history. | BR-025, BR-111 |
| EX-006 | A sponsor, approver, or reviewer is absent. | Use authorized delegation or escalation without bypassing control. | BR-113 |
| EX-007 | A project begins under an approved emergency exception. | Record the exception, authority, scope, expiry, missing evidence, and remediation actions. | BR-028, BR-029 |
| EX-008 | Baseline dates are missed but no change is approved. | Preserve baseline, update forecast, report variance, and trigger escalation or change assessment. | BR-036, BR-039 |
| EX-009 | A task is complete but its deliverable is rejected. | Retain task completion evidence while keeping deliverable acceptance and related milestone status unresolved. | BR-065 to BR-069 |
| EX-010 | Actual financial data is unavailable or delayed. | Show data freshness, last successful synchronization, limitation, and responsible action; do not fabricate actuals. | BR-053, BR-119 |
| EX-011 | One contract serves multiple projects. | Allocate or relate obligations and costs without double counting. | BR-057, BR-059, BR-060 |
| EX-012 | A supplier submits a deliverable after contract expiry. | Route for authorized review while exposing contractual exception and required decision. | BR-060, BR-065 |
| EX-013 | A critical risk becomes an issue. | Preserve risk history and create or link the issue, actions, escalation, and decision. | BR-070 to BR-076 |
| EX-014 | A change is approved after work has already started. | Record unauthorized or at-risk work, approval date, consequences, and baseline update without rewriting history. | BR-077 to BR-081 |
| EX-015 | Two users update the same record. | Detect conflict, preserve changes, and require controlled resolution. | BR-127 |
| EX-016 | A confidential project appears in an aggregate dashboard. | Apply approved aggregation and masking rules while restricting unauthorized drill-down. | BR-087, BR-112 |
| EX-017 | An approver has a conflict of interest. | Apply delegation, reassignment, or abstention controls and record the reason. | BR-011, BR-114 |
| EX-018 | A project is cancelled with open contracts and invoices. | Prevent normal closure until obligations are resolved or formally transferred and accepted. | BR-064, BR-108 |
| EX-019 | A project closes before benefits are realized. | Transfer benefit accountability and future measurement schedule to the benefit owner. | BR-102 |
| EX-020 | A closed project requires correction. | Use controlled reopening or a correction record without erasing historical closure. | BR-109, BR-110 |
| EX-021 | A reporting period is missed. | Escalate, retain missing status, and prevent later reports from hiding the gap. | BR-094, BR-099 |
| EX-022 | Imported data fails validation. | Reject or quarantine invalid records with error details, ownership, and reconciliation. | BR-119, BR-123 |
| EX-023 | An integration is unavailable. | Expose failure and freshness, apply approved retry or fallback, and avoid silent inconsistency. | BR-119 |
| EX-024 | A user loses access during an active assignment. | Reassign or escalate owned work while preserving audit and security controls. | BR-112, BR-113 |
| EX-025 | An intelligent recommendation is unsupported or incorrect. | Require human verification, preserve source and feedback, and prevent unauthorized automated action. | BR-129 to BR-132 |

## 12. Assumptions, Constraints, and Dependencies

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| BACD-001 | Constraint | The target scope is enterprise-wide and must not be reduced to an MVP or task-only product without an explicit documented decision. | Documentation and fit-gap must cover all capability areas. | Project governance — TBD | Confirmed |
| BACD-002 | Constraint | The business requirements remain technology-neutral until solution evaluation and architecture decisions are completed. | No product-specific design is authorized by this document. | Project governance — TBD | Confirmed |
| BACD-003 | Dependency | Authoritative current-state policies, procedures, forms, matrices, reports, and sample records are required. | Detailed As-Is, rules, roles, and approval behavior remain incomplete. | Environment Fund | Open |
| BACD-004 | Dependency | Formal business, product, PMO, finance, procurement, security, data, records, and operations owners must be confirmed. | Review, decision, and ownership fields remain provisional. | Environment Fund | Open |
| BACD-005 | Dependency | Systems of record and integration boundaries must be confirmed. | Data ownership, reconciliation, and solution boundaries remain provisional. | Business and IT owners | Open |
| BACD-006 | Dependency | Applicable government and organizational policies for project governance, procurement, finance, cybersecurity, privacy, records, accessibility, and continuity must be identified. | Controls and compliance requirements cannot be finalized. | Relevant owners | Open |
| BACD-007 | Assumption | Different project types will require proportionate governance and configurable lifecycle templates. | Configuration and rules must support variation. | PMO — TBD | To Validate |
| BACD-008 | Assumption | Oracle Fusion, OpenText ECM, enterprise identity, analytics, email, calendar, HR, and other enterprise systems may participate in the target ecosystem. | Integration analysis is required before boundaries are confirmed. | IT and business owners | To Validate |
| BACD-009 | Constraint | Authoritative financial, procurement, HR, identity, and records data must not be duplicated as uncontrolled editable master data. | System-of-record and synchronization design are required. | Data owners | To Validate |
| BACD-010 | Dependency | The organization must define project classification, thresholds, health rules, gate criteria, and approval matrices. | Workflows and validations cannot be finalized. | PMO and governance body | Open |
| BACD-011 | Dependency | The organization must define reporting cycles, calendars, periods, and executive reporting standards. | Notification, status, and reporting requirements remain incomplete. | PMO | Open |
| BACD-012 | Dependency | External supplier and consultant access requirements must be confirmed. | Identity, licensing, data scope, and collaboration design remain provisional. | Procurement, security, IT | Open |
| BACD-013 | Dependency | Historical data, migration scope, retention, and decommissioning expectations must be confirmed. | Migration and archival requirements remain incomplete. | Business, data, records, IT | Open |
| BACD-014 | Constraint | No test result, UAT outcome, compliance status, or operational readiness may be claimed during requirements documentation. | QA evidence must be recorded only after execution. | Project team | Confirmed |
| BACD-015 | Assumption | The solution will support Arabic and English business use with appropriate directional behavior. | UI, content, testing, and accessibility requirements must include both contexts. | Business owner — TBD | To Validate |

## 13. Open Questions

### 13.1 Governance and Ownership

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-001 | Who is the formal business owner, product or system owner, PMO owner, and executive governance body? | Environment Fund | All requirements | Open |
| BOQ-002 | What portfolio, program, initiative, and project governance model is currently approved? | PMO / governance | BP-01 to BP-18 | Open |
| BOQ-003 | What project classifications, value bands, complexity levels, risk tiers, and lifecycle variants are required? | PMO | BR-026 to BR-029 | Open |
| BOQ-004 | What are the authorized approval, delegation, escalation, and segregation-of-duties matrices? | Governance, HR, security | BR-111 to BR-116 | Open |
| BOQ-005 | Which committees exist, what are their terms of reference, and what decisions may each make? | Governance owner | BR-013, BR-019, BR-082 | Open |

### 13.2 Process and Policy

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-006 | What are the current intake, evaluation, prioritization, authorization, planning, reporting, change, acceptance, closure, and benefit processes? | PMO and business owners | BP-02 to BP-18 | Open |
| BOQ-007 | Which artifacts and evidence are mandatory at each lifecycle gate? | PMO and assurance owners | BR-028, BR-029 | Open |
| BOQ-008 | How is progress currently measured for different project and deliverable types? | PMO | BR-044, BR-094 | Open |
| BOQ-009 | Which quality, acceptance, completion-certificate, and payment controls apply? | Business, quality, procurement, finance | BR-063 to BR-069 | Open |
| BOQ-010 | Which benefit-management and post-project evaluation practices are required? | Strategy and business owners | BR-101 to BR-105 | Open |

### 13.3 Finance, Procurement, and Contracts

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-011 | Which financial dimensions, budget types, forecast methods, cost categories, and funding sources must be represented? | Finance | BR-051 to BR-057 | Open |
| BOQ-012 | Which Oracle Fusion or other financial and procurement objects are authoritative for each data element? | Finance, procurement, IT | BR-053, BR-059, BR-117 | Open |
| BOQ-013 | How are shared contracts, shared costs, receipts, invoices, retention, penalties, and guarantees allocated to projects? | Procurement, contracts, finance | BR-057 to BR-064 | Open |
| BOQ-014 | Which supplier-performance criteria and evaluation cycles are required? | Procurement and project owners | BR-061 | Open |
| BOQ-015 | For which project types is earned value management required, and what approved method applies? | PMO and finance | BR-056 | Open |

### 13.4 Data, Integration, Security, and Records

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-016 | What are the authoritative systems for strategy, projects, finance, procurement, contracts, HR, identity, documents, correspondence, risks, and analytics? | Business and IT owners | BR-117 to BR-123 | Open |
| BOQ-017 | What data classification, residency, privacy, retention, archival, deletion, and legal-hold requirements apply? | Data, security, records, legal | BR-087 to BR-093 | Open |
| BOQ-018 | Which users require access, including suppliers, consultants, auditors, executives, and temporary delegates? | Business, HR, security | BR-111 to BR-114 | Open |
| BOQ-019 | What historical data must be migrated, and which current tools or registers will be retired? | PMO, data, IT | BACD-013 | Open |
| BOQ-020 | What integration timeliness, reconciliation, fallback, and manual recovery expectations apply? | Business and IT owners | BR-119 | Open |

### 13.5 Reporting, Experience, and Operations

| ID | Question | Owner | Related Item | Status |
|---|---|---|---|---|
| BOQ-021 | What are the official executive, PMO, finance, procurement, risk, and project report formats and cycles? | Relevant report owners | DR-001 to DR-025 | Open |
| BOQ-022 | How are project health and threshold breaches currently defined? | PMO | BR-096 | Open |
| BOQ-023 | What Arabic, English, terminology, accessibility, device, and responsive-use requirements are mandatory? | Business, communications, accessibility owner | BR-124 to BR-128 | Open |
| BOQ-024 | What operational support, service hours, continuity, recovery, and monitoring requirements apply? | IT operations and business owner | Project Overview / NFR design | Open |
| BOQ-025 | Which intelligent capabilities are desired, and what AI governance, hosting, data, human-review, and evaluation controls apply? | Business, AI governance, security, IT | BR-129 to BR-132 | Open |

## 14. Requirement Coverage Summary

| Capability Group | Requirement Range | Requirement Count |
|---|---|---:|
| Strategy and alignment | BR-001 to BR-004 | 4 |
| Demand and intake | BR-005 to BR-008 | 4 |
| Business case and prioritization | BR-009 to BR-014 | 6 |
| Portfolio management | BR-015 to BR-020 | 6 |
| Program management | BR-021 to BR-024 | 4 |
| Initiation and governance | BR-025 to BR-030 | 6 |
| Scope and WBS | BR-031 to BR-034 | 4 |
| Schedule and dependencies | BR-035 to BR-039 | 5 |
| Work, Agile, and hybrid | BR-040 to BR-044 | 5 |
| Resources, skills, and time | BR-045 to BR-050 | 6 |
| Finance and earned value | BR-051 to BR-057 | 7 |
| Procurement and contracts | BR-058 to BR-064 | 7 |
| Deliverables and quality | BR-065 to BR-069 | 5 |
| Risks, issues, and dependencies | BR-070 to BR-076 | 7 |
| Change control | BR-077 to BR-081 | 5 |
| Meetings, decisions, and stakeholders | BR-082 to BR-087 | 6 |
| Documents, records, and knowledge | BR-088 to BR-093 | 6 |
| Reporting, analytics, and alerts | BR-094 to BR-100 | 7 |
| Benefits and evaluation | BR-101 to BR-105 | 5 |
| Closure and transition | BR-106 to BR-110 | 5 |
| Roles, access, and audit | BR-111 to BR-116 | 6 |
| Data, integration, and administration | BR-117 to BR-123 | 7 |
| UX, language, accessibility, collaboration | BR-124 to BR-128 | 5 |
| Intelligent capabilities | BR-129 to BR-132 | 4 |
| **Total** | **BR-001 to BR-132** | **132** |

## 15. Readiness Assessment

This document establishes a comprehensive baseline of business capability requirements, but it is not yet `Ready`.

It remains `Draft` because:

- authoritative current-state evidence has not been reviewed;
- formal owners and reviewers are not confirmed;
- candidate business rules are not approved;
- approval matrices, thresholds, classifications, and gate criteria are unresolved;
- systems of record and integration boundaries are provisional;
- official reports, templates, terminology, and policies are not confirmed; and
- stakeholder validation has not been performed.

The next required documentation actions are:

1. validate the current-state assessment with evidence;
2. confirm owners, roles, governance bodies, and policies;
3. review each requirement group with the accountable business area;
4. promote confirmed candidate rules into the authoritative business-rule register;
5. resolve or assign the open questions;
6. translate the confirmed business requirements into testable system requirements;
7. update the Traceability Matrix once functional and non-functional requirement IDs exist; and
8. update the Documentation Status Matrix after review.

## 16. Informative Reference Frameworks

The following external references informed the completeness review. They do not replace Environment Fund policies or confirm project-specific rules:

- ISO 21500:2021 for project, program, and portfolio management context and concepts.
- ISO 21502:2020 for project-management guidance across predictive, iterative, adaptive, and hybrid delivery.
- ISO 21503:2022 for program-management guidance.
- ISO 21504:2022 for portfolio-management guidance.
- ISO 21505:2017 for governance guidance.
- ISO 21511:2018 for work breakdown structures.
- ISO 21512:2024 for earned value management implementation guidance.
- PMI's standards for portfolio and program management and its benefits-realization practice guide.
- Oracle Fusion Cloud Project Management documentation as an informative benchmark for integrated project execution, resource, financial, contract, costing, performance-reporting, security, analytics, and integration capability coverage.

These references are informative only. The authoritative project baseline remains the confirmed Environment Fund requirements, rules, policies, decisions, and evidence recorded in this repository.

## 17. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | Template | Repository starter | Initial generic template |
| 0.2 | 2026-07-18 | AI-assisted business analysis under user direction | Replaced template with comprehensive enterprise project portfolio management business requirements baseline |
