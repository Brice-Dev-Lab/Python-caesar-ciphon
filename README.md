# Caesar Ciphon

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![Package Manager](https://img.shields.io/badge/uv-package%20manager-5C6AB7?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-learning%20module-orange?style=flat-square)
![Phases](https://img.shields.io/badge/phases-6-blueviolet?style=flat-square)
![CLI](https://img.shields.io/badge/interface-CLI--first-brightgreen?style=flat-square)
![FastAPI](https://img.shields.io/badge/future-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

> *"The cipher was never cryptanalytically broken. It was betrayed by someone with the key."*

A hands-on, function-first Python learning module where you build a working Caesar cipher encryption tool from scratch — one phase at a time, following the actual path Julius Caesar used during the Gallic Wars (58–50 BCE).

---

## The Story Behind the Code

In 58 BCE, Julius Caesar needed to send battle orders across hundreds of miles without enemies reading them. His solution was elegant, practical, and — against all odds — **was never broken by cryptanalysis**. It fell because he trusted someone named Brutus.

That's your first lesson before writing a single line of code: **encryption protects against external eavesdroppers, not insiders with the key.**

Read the full history in [`docs/03_project_story/00_caesar_historical_context.md`](docs/03_project_story/00_caesar_historical_context.md) before you start. It will make every phase more meaningful.

---

## What You'll Build

By the end of this course you will have:

- A fully working **CLI cipher tool** that encrypts and decrypts messages
- Clean, **testable function-based code** with proper separation of concerns
- A real understanding of why **architecture decisions matter**
- A codebase ready for optional **FastAPI deployment** (see [v2 below](#version-2-fastapi-coming-soon))

---

## 6-Phase Learning Path

Each phase mirrors a real decision Caesar made — from a single-letter prototype to a complete, resilient field cipher.

| Phase | Title | What You Build | Historical Parallel |
|-------|-------|----------------|---------------------|
| 1 | **Foundations** | Single-character shift logic and CLI basics | Caesar's first prototype — a shift his commanders could memorize |
| 2 | **Full Message Processing** | Loop-based encryption/decryption for complete messages | Scaling from markers to full battle orders |
| 3 | **Validation and Branching** | Input validation, error handling, random shift mode | Handling multiple recipients, fallback plans if messages were lost |
| 4 | **Data Modeling** | Batch messages with metadata using lists and dicts | Tracking Brutus, Cicero, Antony — different clearances, same system |
| 5 | **Function Modularization** | Refactor into clean, reusable `core/` modules | Professionalizing the cipher so other officers could execute it |
| 6 | **Capstone** | Polished CLI product with tests; optional class wrapper | Caesar's final, fully deployed secure communication system |

---

## What You'll Learn

- **Variables and data types** — storing messages and shift values
- **Loops and iteration** — processing strings character by character
- **Conditionals and validation** — handling edge cases and errors
- **Functions and modularity** — single-responsibility, testable code
- **Data structures** — lists and dictionaries for complex message batches
- **Testing and debugging** — verifying behavior at every step

---

## Project Structure

The project grows as you progress through the phases:

```plaintext
caesar_ciphon/
├── README.md
├── pyproject.toml
├── src/
│   └── caesar_ciphor/
│       ├── main.py                    # CLI entry point
│       ├── practice/                  # Your experimental code (Phases 1-4)
│       │   ├── phase_1_shift_char.py
│       │   ├── phase_2_message_loop.py
│       │   ├── phase_3_validation.py
│       │   └── phase_4_batch_data.py
│       ├── core/                      # Production-ready logic (Phases 5-6)
│       │   ├── cipher.py              # encrypt(), decrypt()
│       │   ├── validation.py          # validate_shift(), validate_message()
│       │   ├── errors.py              # Custom exceptions
│       │   └── tests/
│       └── optional/                  # Advanced: class wrapper (Phase 6)
│           └── cipher_class.py
└── docs/
    ├── 00_overview/        # Course overview and scope
    ├── 01_instructions/    # Phase-by-phase instructions
    ├── 02_deployment/      # FastAPI deployment guides
    └── 03_project_story/   # Historical context
```

**Core design rule:** `core/` never imports from `main.py`, `optional/`, or `api/`. This lets you reuse it from CLI, class wrapper, or API without touching the logic.

---

## Getting Started

**Requirements:** Python 3.12+, `uv` (recommended), any IDE or text editor.

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/caesar_ciphon.git
cd caesar_ciphon

# 2. Create a virtual environment and install dependencies
uv sync

# 3. Run the starter CLI
uv run python -m caesar_ciphor.main
```

Then open [`docs/00_overview/00_course_overview.md`](docs/00_overview/00_course_overview.md) and follow the 6-phase path.

---

## Docs

| Document | Description |
|----------|-------------|
| [`docs/00_overview/00_course_overview.md`](docs/00_overview/00_course_overview.md) | Start here — full course map |
| [`docs/00_overview/01_project_structure.md`](docs/00_overview/01_project_structure.md) | How the project grows phase by phase |
| [`docs/00_overview/02_project_scope.md`](docs/00_overview/02_project_scope.md) | Feature scope and cipher mechanics |
| [`docs/01_instructions/`](docs/01_instructions/) | Phase-by-phase build instructions |
| [`docs/03_project_story/00_caesar_historical_context.md`](docs/03_project_story/00_caesar_historical_context.md) | The real history behind the cipher |

---

## Version 2: FastAPI (Coming Soon)

Once you complete the 6-phase CLI course, an optional deployment path expands your working cipher into a REST API.

**Planned endpoints:**

```
POST /encrypt   — Encrypt a message with a given shift
POST /decrypt   — Decrypt a message with a given shift
GET  /health    — API health check
```

The `core/` modules you build in Phases 5–6 will plug directly into the FastAPI layer with zero changes — that's the payoff for building with clean architecture from the start.

Deployment guides will live in [`docs/02_deployment/`](docs/02_deployment/) when ready.

---

## Philosophy

This course teaches by building, not lecturing:

- **Function-first** before classes or patterns
- **Testable code** from Phase 1 onward
- **Clean boundaries** so your work is reusable and deployable
- **Reflection**, not just syntax — understanding *why* decisions matter

Plan for **4–8 hours** total, depending on how deep you go on stretch challenges.

---

## Contributing

This is a learning module. Found a bug in the docs, a broken phase instruction, or a stretch challenge idea? Open an issue or PR — improvements are welcome.

---

## License

MIT — use it, fork it, teach with it.
