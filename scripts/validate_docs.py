#!/usr/bin/env python3
"""Validate the required documentation structure and internal references."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "docs/00-Project-Index.md",
    "docs/01-Requirements/01-Project-Overview.md",
    "docs/01-Requirements/02-Business-Requirements.md",
    "docs/01-Requirements/03-System-Requirements.md",
    "docs/01-Requirements/04-Delivery-Backlog.md",
    "docs/01-Requirements/05-Traceability-Matrix.md",
    "docs/02-Solution-Design/00-Technology-Stack.md",
    "docs/02-Solution-Design/01-Solution-Overview-and-Architecture.md",
    "docs/02-Solution-Design/02-Application-Architecture.md",
    "docs/02-Solution-Design/03-Data-API-and-Integration-Design.md",
    "docs/02-Solution-Design/04-Security-and-Access-Control.md",
    "docs/02-Solution-Design/05-Non-Functional-and-Operational-Design.md",
    "docs/03-UI-UX/01-UX-Foundation-and-Users.md",
    "docs/03-UI-UX/02-Information-Architecture-Flows-and-Screens.md",
    "docs/03-UI-UX/03-Wireframes-and-Interaction-Behavior.md",
    "docs/03-UI-UX/04-Design-System-and-Implementation-Guidance.md",
    "docs/04-QA-and-Testing/01-QA-Strategy-and-Test-Plan.md",
    "docs/04-QA-and-Testing/02-Test-Scenarios.md",
    "docs/04-QA-and-Testing/03-Test-Cases.md",
    "docs/04-QA-and-Testing/04-UAT-and-Defect-Management.md",
    "docs/04-QA-and-Testing/05-QA-Summary-and-Release-Readiness.md",
    "docs/05-Agile-Delivery/01-Product-Roadmap-and-Release-Plan.md",
    "docs/05-Agile-Delivery/02-Sprint-Plan.md",
    "docs/05-Agile-Delivery/03-Sprint-Status.md",
    "docs/05-Agile-Delivery/04-Release-and-Transition-Plan.md",
    "docs/05-Agile-Delivery/sprints/README.md",
}
RETIRED_TEXT = ("05-Delivery-and-Execution", "Work-Package-or-Iteration-Plan")
REFERENCE_PATTERN = re.compile(
    r"`((?:docs/|README\.md)[^`{}]*?(?:\.md|/))`"
)


def main() -> int:
    errors: list[str] = []
    markdown_files = [
        *sorted(ROOT.glob("*.md")),
        *sorted((ROOT / "docs").rglob("*.md")),
    ]

    for relative_path in sorted(REQUIRED_FILES):
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    for file_path in markdown_files:
        text = file_path.read_text(encoding="utf-8")
        relative_path = file_path.relative_to(ROOT)
        h1_count = len(re.findall(r"^# [^#]", text, flags=re.MULTILINE))
        if h1_count != 1:
            errors.append(f"{relative_path}: expected exactly one H1, found {h1_count}")

        for retired in RETIRED_TEXT:
            if retired in text:
                errors.append(f"{relative_path}: contains retired text '{retired}'")

        for reference in REFERENCE_PATTERN.findall(text):
            target = ROOT / reference
            if not target.exists():
                errors.append(f"{relative_path}: missing internal reference '{reference}'")

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Documentation validation passed: {len(markdown_files)} Markdown files, "
        f"{len(REQUIRED_FILES)} required files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
