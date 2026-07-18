# AI Operating Instructions

## Purpose

This repository follows a documentation-first, technology-neutral, Agile sprint delivery methodology for Environment Fund projects.

These instructions apply to every AI assistant, coding agent, human contributor, and delivery tool working in this repository. They are the canonical operating rules. Tool-specific instruction files may reference this file but must not redefine or contradict it.

## Core Method

```text
Understand the project
→ Complete and review the required documentation
→ Confirm documentation readiness without formal sign-off
→ Select Ready backlog items for one sprint
→ Implement and verify only that sprint
→ Update evidence, traceability, and sprint status
→ Preserve sprint history and create a pull request
```

Documentation and planning precede implementation. Implementation proceeds through controlled Agile sprints.

## Mandatory Starting Sequence

Before taking action:

1. Read this file.
2. Read `docs/00-Project-Index.md`.
3. Identify the current project phase, current task, document statuses, and material blockers.
4. Determine whether the request is documentation, readiness review, sprint planning, implementation, QA, or release work.
5. Read only the source documents required for that task and the references they explicitly depend on.

Do not read or modify the entire repository by default. Expand context only when a dependency, inconsistency, risk, or unresolved question requires it.

## Source of Truth and Precedence

Use information in this order:

1. The user's current explicit instruction
2. Confirmed project facts and decisions in the documentation
3. The active Sprint Plan for implementation scope
4. Current implementation, configuration, tests, and recorded evidence
5. Clearly labeled assumptions or recommendations

An assumption, recommendation, placeholder, example row, or AI-generated suggestion is not a confirmed requirement or decision.

When sources conflict, do not choose silently. Record the conflict, identify the affected IDs and artifacts, and request or document the required resolution.

## Universal Rules

- Do not invent requirements, business rules, owners, dates, budgets, technologies, APIs, data fields, permissions, service levels, acceptance criteria, or test results.
- Keep confirmed facts, proposed decisions, assumptions, risks, gaps, and open questions distinguishable.
- Preserve repository-wide identifiers and use the identifier standard in the Traceability Matrix.
- Use `N/A` with a short reason when a section does not apply.
- Keep small projects lightweight and expand documentation only when scope, risk, or complexity requires it.
- Preserve the existing language of each document and support Arabic, English, RTL, and LTR requirements where applicable.
- Never expose credentials, secrets, tokens, personal data, production data, or sensitive configuration.
- Do not claim that work, testing, review, readiness, deployment, or evidence exists unless it is recorded and verifiable.
- Readiness is an evidence-based project state, not a formal approval, signature, or sign-off.

## Documentation Mode

When the current task is project documentation:

1. Do not implement code or production configuration.
2. Work through the documentation flow defined in the Project Index.
3. Use the `Required Context` and `AI Instructions` sections of the active document.
4. Derive content only from supplied evidence, existing project documents, and confirmed user input.
5. Record missing information as an owned open question, assumption, dependency, risk, or blocker.
6. Update related documents when a confirmed change affects scope, requirements, design, backlog, tests, or traceability.
7. Update the Documentation Status Matrix after material document changes.

The normal documentation sequence is:

1. Project Overview
2. Business Requirements
3. System Requirements
4. Delivery Backlog and Traceability Matrix
5. Technology Stack and Solution Design
6. UI/UX when applicable
7. QA strategy, scenarios, and planned test cases
8. Product Roadmap and Release Plan

QA execution results, defects, and evidence are not fabricated during documentation. They are recorded when testing is performed during delivery.

## Documentation Readiness

Do not begin implementation merely because documents exist.

Before sprint implementation, verify that the selected scope satisfies the Documentation Readiness Checklist in `docs/00-Project-Index.md` and the Definition of Ready in `docs/05-Agile-Delivery/01-Product-Roadmap-and-Release-Plan.md`.

If a material requirement, rule, decision, dependency, acceptance criterion, security control, data contract, or test expectation is unresolved:

- mark the affected scope `Not Ready`;
- record the blocker and its owner;
- explain the implementation impact; and
- stop work on the affected scope until it is resolved.

Unrelated Ready scope may continue when it can be implemented and tested independently.

## Sprint Planning

- Plan one sprint at a time using `docs/05-Agile-Delivery/02-Sprint-Plan.md`.
- Include only backlog items that meet the Definition of Ready.
- Link each item to its requirements, acceptance criteria, design references, and test scope.
- Define a clear Sprint Goal, in-scope items, out-of-scope items, dependencies, execution sequence, and expected evidence.
- Do not use the sprint to introduce undocumented scope or silently resolve open decisions.
- Preserve the sprint plan under `docs/05-Agile-Delivery/sprints/`.

## Implementation Mode

Implementation is allowed only when the user explicitly requests implementation and an active sprint scope is Ready.

During implementation:

1. Read the active Sprint Plan.
2. Read only the requirements, designs, UI/UX specifications, contracts, and test references linked to the selected backlog items.
3. Inspect the existing implementation and project-specific instructions before editing.
4. Implement only the active sprint scope.
5. Follow the confirmed technology stack, architecture, security model, data contracts, design system, and engineering conventions.
6. Prefer the smallest coherent change that fully satisfies the documented acceptance criteria.
7. Do not weaken security, validation, auditability, accessibility, observability, or test coverage to make a change pass.
8. Stop and record a blocker when implementation requires an undocumented material decision.

Technology-specific commands, package managers, frameworks, build tools, and deployment methods must come from the project's confirmed Technology Stack and repository configuration. Do not assume a default stack.

## Testing and Evidence

- Test the changed scope in proportion to its risk and documented QA plan.
- Run applicable unit, component, integration, contract, system, UI, accessibility, security, performance, data, or AI evaluations.
- Record actual commands, environment or build, results, failures, defects, and evidence references.
- Never mark a test Passed without an executed result.
- Never delete or overwrite failed-test, defect, or retest history to present a cleaner outcome.
- If a required test cannot run, record why, its impact, owner, and next action.
- Update test cases, traceability, QA readiness, and Sprint Status when evidence changes.

Before completing documentation or implementation changes, run:

```bash
npx --yes markdownlint-cli2 '*.md' 'docs/**/*.md' '#node_modules'
python scripts/validate_docs.py
```

Also run the confirmed project-specific build, lint, test, security, or validation commands relevant to the changed scope.

## Traceability and Change Control

Maintain the chain:

```text
Objective → BR / Rule → FR / NFR → Backlog Item → Design → Test → Release / Sprint
```

When a confirmed change affects this chain:

- update the authoritative source document;
- update downstream backlog, design, test, and traceability references;
- record the reason and impact;
- identify invalidated implementation or evidence; and
- do not silently change scope inside code, tests, or Sprint Status.

## Sprint Status and Closure

Update `docs/05-Agile-Delivery/03-Sprint-Status.md` after meaningful implementation, testing, decisions, scope changes, or blockers.

Before closing a sprint:

- verify completed items against acceptance criteria and Definition of Done;
- record changed artifacts and test evidence;
- record defects, limitations, residual risks, and incomplete work;
- return incomplete items to the Delivery Backlog or identify a future sprint;
- update the Traceability Matrix and relevant documentation;
- preserve the final status under `docs/05-Agile-Delivery/sprints/`; and
- do not mark partially completed work as complete.

## Git and Pull Request Workflow

- Do not commit directly to `main`.
- Use a focused branch for each documentation change, sprint, or coherent fix.
- Preserve unrelated user changes and do not use destructive Git operations.
- Keep commits scoped and messages descriptive.
- Review the complete diff and run applicable validation before publishing.
- Create a pull request that summarizes scope, linked backlog or requirement IDs, implementation or documentation changes, testing, known gaps, and residual risks.
- Do not merge a pull request unless the user explicitly authorizes it.

## Completion Standard

A task is complete only when:

- requested scope is delivered;
- documentation and implementation remain consistent;
- required validation has run and actual results are reported;
- traceability and status records are current;
- blockers, failed checks, limitations, and unverified areas are visible; and
- the handoff clearly states what changed and what remains.

If these conditions cannot be met, report the task as partial or blocked rather than complete.
