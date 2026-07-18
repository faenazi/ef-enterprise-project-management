# Data, API, and Integration Design

## Purpose

Define how information is modeled, stored, exchanged, validated, secured, synchronized, migrated, and exposed across solution components and connected systems.

## Required Context

1. `docs/01-Requirements/03-System-Requirements.md`
2. `docs/02-Solution-Design/00-Technology-Stack.md`
3. `docs/02-Solution-Design/01-Solution-Overview-and-Architecture.md`
4. `docs/02-Solution-Design/02-Application-Architecture.md`

## AI Instructions

- Trace data objects, interfaces, and integrations to documented requirements.
- Separate business data requirements from physical implementation design.
- Do not invent source-system fields, endpoints, credentials, frequencies, or ownership.
- Define contracts and failure behavior explicitly enough for implementation and testing.
- Use `N/A` with a reason for sections not applicable to the project.

## 1. Data Ownership and Sources

| Data Domain / Object | System of Record | Owner | Consumers | Sensitivity | Related Requirements |
|---|---|---|---|---|---|
| {{DATA_OBJECT}} | {{SYSTEM_OF_RECORD}} | {{OWNER}} | {{CONSUMERS}} | {{CLASSIFICATION}} | {{FR_IDS}} |

## 2. Logical Data Model

Document entities, attributes, relationships, identifiers, reference data, lifecycle states, quality rules, and audit requirements.

## 3. Physical Data Design — If Applicable

Document tables or stores, fields, data types, keys, constraints, indexes, partitioning, audit fields, soft deletion, retention, archival, and reporting considerations.

## 4. API and Service Contracts — If Applicable

| API / Service ID | Operation | Consumer | Authentication | Request / Response Reference | Related Requirement |
|---|---|---|---|---|---|
| API-001 | {{OPERATION}} | {{CONSUMER}} | {{AUTHENTICATION}} | {{CONTRACT_REFERENCE}} | FR-001 |

For each contract, define validation, status codes or outcomes, error format, pagination, filtering, sorting, versioning, idempotency, rate limits, and correlation identifiers where applicable.

## 5. Integration Catalog

| Integration ID | Source | Target | Purpose | Method | Direction | Frequency | Owner | Criticality |
|---|---|---|---|---|---|---|---|---|
| INT-001 | {{SOURCE}} | {{TARGET}} | {{PURPOSE}} | API / Event / File / Other | {{DIRECTION}} | {{FREQUENCY}} | {{OWNER}} | {{CRITICALITY}} |

## 6. Data Mapping and Transformation

| Mapping ID | Source Field | Target Field | Transformation / Rule | Required | Validation | Notes |
|---|---|---|---|---|---|---|
| MAP-001 | {{SOURCE_FIELD}} | {{TARGET_FIELD}} | {{RULE}} | Yes / No | {{VALIDATION}} | {{NOTES}} |

## 7. Synchronization and Failure Handling

Document synchronous or asynchronous behavior, sequencing, retries, timeouts, deduplication, idempotency, reconciliation, dead-letter handling, alerting, manual recovery, and fallback behavior.

## 8. Data Migration — If Applicable

Document scope, sources, cleansing, mapping, transformation, reconciliation, mock loads, cutover, validation, rollback, ownership, and evidence requirements.

## 9. Data Security and Privacy

Document classification, minimization, encryption, masking, access restrictions, secrets, retention, deletion, residency, and logging limitations. Reference the security design rather than duplicating controls.

## 10. Open Questions

| ID | Question | Owner | Related Data / Interface | Status |
|---|---|---|---|---|
| DIQ-001 | {{QUESTION}} | {{OWNER}} | {{REFERENCE}} | Open |

## 11. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 0.1 | {{DATE}} | {{AUTHOR}} | Initial draft |
