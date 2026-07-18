# EF Project Starter

This repository is a documentation-first starter for Environment Fund projects.

It helps teams document, design, test, and deliver projects using a clear AI-assisted workflow before implementation starts.

## Working Approach

1. Document the project first using AI assistance.
2. Complete requirements, solution design, UI/UX, QA planning, and delivery planning.
3. Confirm documentation readiness before implementation begins; this is a review checkpoint, not a formal sign-off.
4. Start implementation through Claude Code or other development tools using Agile sprints.
5. Update Sprint Status whenever meaningful progress, testing, decisions, or blockers occur.

## Starting a New Project

1. Create a repository from this template.
2. Ask the AI tool to read `AGENTS.md` and `docs/00-Project-Index.md` before taking action.
3. Complete the Project Index and use its Documentation Status Matrix as the central readiness view.
4. Work through Requirements, Solution Design, UI/UX when applicable, QA planning, and the Product Roadmap in order.
5. Replace template placeholders with confirmed information; use `N/A` with a reason when a section does not apply.
6. Record unresolved information as an owned open question or blocker instead of guessing.
7. Review documentation readiness using the checklist in the Project Index.
8. Create the first Sprint Plan only when the selected backlog items meet the Definition of Ready.

## Main Structure

```text
AGENTS.md
CLAUDE.md
docs/
├── 00-Project-Index.md
├── 01-Requirements/
│   ├── 01-Project-Overview.md
│   ├── 02-Business-Requirements.md
│   ├── 03-System-Requirements.md
│   ├── 04-Delivery-Backlog.md
│   └── 05-Traceability-Matrix.md
├── 02-Solution-Design/
│   ├── 00-Technology-Stack.md
│   ├── 01-Solution-Overview-and-Architecture.md
│   ├── 02-Application-Architecture.md
│   ├── 03-Data-API-and-Integration-Design.md
│   ├── 04-Security-and-Access-Control.md
│   └── 05-Non-Functional-and-Operational-Design.md
├── 03-UI-UX/
│   ├── 01-UX-Foundation-and-Users.md
│   ├── 02-Information-Architecture-Flows-and-Screens.md
│   ├── 03-Wireframes-and-Interaction-Behavior.md
│   └── 04-Design-System-and-Implementation-Guidance.md
├── 04-QA-and-Testing/
│   ├── 01-QA-Strategy-and-Test-Plan.md
│   ├── 02-Test-Scenarios.md
│   ├── 03-Test-Cases.md
│   ├── 04-UAT-and-Defect-Management.md
│   └── 05-QA-Summary-and-Release-Readiness.md
└── 05-Agile-Delivery/
    ├── 01-Product-Roadmap-and-Release-Plan.md
    ├── 02-Sprint-Plan.md
    ├── 03-Sprint-Status.md
    ├── 04-Release-and-Transition-Plan.md
    └── sprints/
        └── README.md
```

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

Implementation begins after the required documentation is ready and proceeds through Agile sprints:

```text
docs/05-Agile-Delivery/
├── 01-Product-Roadmap-and-Release-Plan.md
├── 02-Sprint-Plan.md
├── 03-Sprint-Status.md
├── 04-Release-and-Transition-Plan.md
└── sprints/
    └── README.md
```

Create `docs/05-Agile-Delivery/sprints/` when implementation starts and preserve one plan and final status record per sprint, for example:

```text
docs/05-Agile-Delivery/sprints/
├── Sprint-01-Plan.md
├── Sprint-01-Status.md
├── Sprint-02-Plan.md
└── Sprint-02-Status.md
```

## QA Planning and Execution

Before implementation, define the QA strategy, scenarios, planned test cases, required environments, evidence expectations, and acceptance criteria. During each sprint, execute the applicable tests and update actual results, defects, evidence, traceability, QA readiness, and Sprint Status.

## Technology Approach

This starter does not prescribe a technology stack. Select and document the stack according to the project type, requirements, enterprise architecture, security needs, and confirmed constraints.

The template supports custom development, low-code, enterprise platforms, data and analytics, integrations, AI solutions, SaaS, and vendor-delivered projects.

## AI Usage Rule

All document outlines should be generated based on the project size, business complexity, technical complexity, UI complexity, integrations, data sensitivity, and delivery approach.

Do not use a fixed detailed outline for every project.
Keep small projects lightweight and expand medium or large projects only as needed.

## Documentation Quality

Pull requests automatically validate Markdown structure, required template files, internal documentation references, and retired paths. Run the same checks locally with:

```bash
npx --yes markdownlint-cli2 '*.md' 'docs/**/*.md' '#node_modules'
python scripts/validate_docs.py
```
