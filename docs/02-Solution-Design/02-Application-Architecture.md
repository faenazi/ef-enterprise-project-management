# Application Architecture

## Purpose

Define the internal application structure needed to implement or configure the solution. This file supports custom development, low-code, enterprise platforms, SaaS configuration, data applications, and hybrid solutions.

## Required Context

1. `docs/01-Requirements/03-System-Requirements.md`
2. `docs/01-Requirements/04-Delivery-Backlog.md`
3. `docs/02-Solution-Design/00-Technology-Stack.md`
4. `docs/02-Solution-Design/01-Solution-Overview-and-Architecture.md`
5. `docs/03-UI-UX/` when a user interface is in scope

## AI Instructions

- Tailor sections to the solution type; do not force frontend/backend structures onto configuration-only projects.
- Organize implementation around business capabilities or features where practical.
- Define boundaries and responsibilities before proposing folders, classes, packages, or platform objects.
- Do not add frameworks, patterns, or abstractions without a demonstrated need.
- Link implementation areas to requirements and backlog items.

## 1. Application Structure

Describe modules, features, layers, platform objects, services, jobs, reports, or configuration areas and their responsibilities.

| Area / Module | Responsibility | Related Requirements | Related Backlog Items | Notes |
|---|---|---|---|---|
| {{AREA}} | {{RESPONSIBILITY}} | {{FR_IDS}} | {{BI_IDS}} | {{NOTES}} |

## 2. User Interface Architecture — If Applicable

Document routes, pages, features, reusable components, forms, validation, state management, API clients, localization, accessibility, and loading/empty/error/success states.

## 3. Service and Business Logic Architecture — If Applicable

Document endpoints or service interfaces, commands and queries, business services, validation, authorization enforcement, background jobs, transactions, error handling, and audit behavior.

## 4. Platform Configuration Architecture — If Applicable

Document modules, configuration objects, workflows, extensions, reports, roles, scheduled processes, and boundaries between standard configuration and customization.

## 5. Data and Analytics Application Structure — If Applicable

Document pipelines, semantic models, transformations, notebooks, datasets, reports, model-serving components, prompts, agents, or retrieval components as applicable.

## 6. Cross-Cutting Concerns

- Authentication and authorization enforcement
- Validation and error handling
- Logging, tracing, and correlation
- Localization and accessibility
- Caching and performance
- Configuration and secrets
- Feature toggles where justified
- Retry and idempotency where justified

## 7. Implementation Conventions

Record naming, organization, dependency direction, package rules, testing boundaries, generated-code rules, and platform-specific conventions confirmed for the project.

## 8. Open Questions

| ID | Question | Owner | Impacted Area | Status |
|---|---|---|---|---|
| AAQ-001 | {{QUESTION}} | {{OWNER}} | {{AREA}} | Open |

## 9. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
