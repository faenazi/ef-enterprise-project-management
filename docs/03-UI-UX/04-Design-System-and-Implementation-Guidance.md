# Design System and Implementation Guidance

## Purpose

Define the visual foundations, reusable components, content conventions, accessibility rules, implementation guidance, and design-to-development mapping needed for a consistent interface.

This document replaces a separate UI/UX handoff by keeping implementation guidance with the design system itself.

## Required Context

1. `docs/02-Solution-Design/00-Technology-Stack.md`
2. `docs/02-Solution-Design/02-Application-Architecture.md`
3. `docs/03-UI-UX/01-UX-Foundation-and-Users.md`
4. `docs/03-UI-UX/02-Information-Architecture-Flows-and-Screens.md`
5. `docs/03-UI-UX/03-Wireframes-and-Interaction-Behavior.md`

## AI Instructions

- Follow the Environment Fund's approved brand identity and existing design assets when provided.
- Do not invent logos, fonts, colors, patterns, or brand rules.
- Keep design tokens independent of a specific frontend framework unless the technology is confirmed.
- Reuse components before defining new ones.
- Specify all meaningful component variants, states, RTL behavior, accessibility, and implementation boundaries.

## 1. Visual and Brand Foundations

Document approved logo usage, colors, typography, spacing, radii, elevation, iconography, imagery, grids, and patterns by referencing authoritative brand sources.

## 2. Design Tokens

| Token Category | Token | Value / Reference | Usage | RTL / Accessibility Notes |
|---|---|---|---|---|
| Color / Typography / Spacing / Other | {{TOKEN}} | {{VALUE}} | {{USAGE}} | {{NOTES}} |

## 3. Layout and Responsive System

Document containers, grids, spacing rhythm, page templates, navigation layouts, density, breakpoints or layout modes, and Arabic/English directional behavior.

## 4. Component Catalog

| Component ID | Component | Purpose | Variants | States | Used By Screens | Accessibility Notes |
|---|---|---|---|---|---|---|
| UICMP-001 | {{COMPONENT}} | {{PURPOSE}} | {{VARIANTS}} | {{STATES}} | {{SCREEN_IDS}} | {{ACCESSIBILITY}} |

For each material component, define anatomy, content rules, variants, sizes, states, interactions, validation, permissions, RTL behavior, responsive behavior, accessibility, and examples of correct and incorrect use.

## 5. Content and UX Writing

Document terminology, labels, action verbs, confirmation wording, validation messages, error messages, empty states, dates, numbers, bilingual content, truncation, and tone.

## 6. Accessibility Rules

Document minimum expectations for semantic structure, keyboard support, focus visibility, labels, contrast, error association, status announcements, motion, touch targets, non-color cues, and testing.

## 7. Design-to-Implementation Mapping

| Design Reference | Component / Screen | Implementation Area | Data / API Dependency | Requirements | Backlog Items | Status |
|---|---|---|---|---|---|---|
| {{DESIGN_REFERENCE}} | {{COMPONENT_OR_SCREEN}} | {{IMPLEMENTATION_AREA}} | {{DEPENDENCY}} | {{FR_IDS}} | {{BI_IDS}} | Planned |

## 8. Implementation Guidance

- Reuse strategy and component ownership
- Styling and token-consumption approach
- Form and validation implementation
- Localization and RTL strategy
- Accessibility verification
- Loading, empty, error, success, and permission-state implementation
- Responsive and device testing
- Asset formats and optimization
- Boundaries between shared and feature-specific components

## 9. Design QA Checklist

- [ ] All planned screens map to requirements and backlog items.
- [ ] All actions and states are specified.
- [ ] Arabic, English, RTL, and LTR behavior is defined where applicable.
- [ ] Accessibility requirements are represented in design and implementation guidance.
- [ ] Components use approved tokens and brand rules.
- [ ] Responsive behavior is documented.
- [ ] Data and API dependencies are identified.
- [ ] Open questions are visible and assigned.

## 10. Open Questions

| ID | Question | Related Component / Screen | Owner | Status |
|---|---|---|---|---|
| DSQ-001 | {{QUESTION}} | {{REFERENCE}} | {{OWNER}} | Open |

## 11. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
