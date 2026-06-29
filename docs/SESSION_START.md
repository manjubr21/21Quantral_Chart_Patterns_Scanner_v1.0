# 21Quantral Chart Patterns Scanner

## Repository

* Repository: https://github.com/manjubr21/21Quantral_Chart_Patterns_Scanner_v1.0
* Branch: feature/infrastructure

---

## Current Status

Current Milestone:
M05.3 Complete

Next Milestone:
M06 – Pattern Detection Framework

Current Version:
v0.5.3

Current Commit:
417aadf

Last Successful Milestone:
M05.3 Complete RSI/ATR Production Implementation


---

## Completed Milestones

* Project structure
* Git repository
* GitHub remote
* Data Provider architecture
* Yahoo Finance provider
* Indicator Framework
* Indicator Engine
* Indicator Registry
* Indicator Cache
* Indicator Key Generator
* SMA
* EMA
* RSI
* ATR
* Unit Tests
* Logging
* Documentation Framework

---

## Architecture

```
app/
    data/
    indicators/
    logs/
    scanner/
    patterns/
    utils/

tests/
docs/
scripts/
```

Indicators are calculated only through Indicator Engine.

Indicators are registered using Indicator Registry.

Indicator results are cached using Indicator Cache.

---

## Coding Standards

* Python 3.13+
* Full type hints
* PEP 8
* Google-style docstrings
* Production-quality code only
* No temporary code
* No duplicate implementations
* Backward compatibility must be maintained

---

## Testing

Run before every commit:

pytest

---

## Git Workflow

git status

pytest

git add .

git commit -m "Meaningful milestone message"

git push

---

## Rules for Development

* Never rewrite working production code unnecessarily.
* Always modify the existing architecture.
* Provide complete production-ready files only.
* Every new module must include unit tests.
* Keep architecture modular and scalable.
* Commit after every completed milestone.
* Update PROJECT_STATUS.md after every milestone.

---

## Starting a New Chat

Read:

* docs/SESSION_START.md
* docs/PROJECT_STATUS.md
* docs/ROADMAP.md

Continue from the next unfinished milestone.

Never restart the architecture unless explicitly requested.

---

## Milestone Workflow

For every milestone:

1. Read existing code before modifying it.
2. Preserve backward compatibility.
3. Implement production-ready code only.
4. Add or update unit tests.
5. Run pytest.
6. Update PROJECT_STATUS.md.
7. Update CHANGELOG.md.
8. Commit.
9. Push.

---
