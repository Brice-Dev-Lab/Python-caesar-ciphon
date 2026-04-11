# Project Structure: Understanding the Layout

This document shows how your project is organized and how it grows as you progress through the 6 phases.

## Current Project Structure

Here's what the repository looks like when you first fork it:

```plaintext
caesar_ciphon_template/
├── README.md
├── pyproject.toml
├── src/
│   └── caesar_ciphon/
│       └── main.py
└── docs/
    ├── 00_overview/
    │   ├── 00_course_overview.md
    │   └── 01_project_structure.md (this file)
    ├── 01_instructions/
    │   ├── 01_phase_1_foundations.md
    │   ├── 02_phase_2_message_processing.md
    │   ├── 03_phase_3_validation_and_branching.md
    │   ├── 04_phase_4_data_modeling.md
    │   ├── 05_phase_5_function_modularization.md
    │   └── 06_phase_6_capstone.md
    ├── 02_deployment/
    │   └── (under development)
    └── 03_project_story/
        ├── 00_caesar_historical_context.md
        └── resources/
            ├── 01_project_story.md
            ├── 02_project_story.md
            ├── 03_project_story.md
            ├── 04_project_story.md
            ├── 05_project_story.md
            ├── 06_project_story.md
            ├── 07_project_story.md
            ├── 08_project_story.md
            └── 09_project_story.md
```

## Proposed Structure (End of Course)

After completing all 6 phases, your project will have this structure:

```plaintext
caesar_ciphon_template/
├── README.md
├── pyproject.toml
├── src/
│   └── caesar_ciphon/
│       ├── __init__.py
│       ├── main.py                    # CLI entry point
│       │
│       ├── practice/                  # Learner experimentation (Phases 1-4)
│       │   ├── __init__.py
│       │   ├── phase_1_shift_char.py
│       │   ├── phase_2_message_loop.py
│       │   ├── phase_3_validation.py
│       │   └── phase_4_batch_data.py
│       │
│       ├── core/                      # Production-ready logic (Phases 5-6)
│       │   ├── __init__.py            # Exports public interface
│       │   ├── cipher.py              # encrypt(), decrypt() functions
│       │   ├── validation.py          # validate_shift(), validate_message()
│       │   ├── errors.py              # CaesarCipherError, InvalidShiftError, etc.
│       │   ├── alphabet.py            # Alphabet helpers and constants
│       │   └── tests/
│       │       ├── __init__.py
│       │       ├── test_cipher.py
│       │       ├── test_validation.py
│       │       └── test_edge_cases.py
│       │
│       ├── optional/                  # Advanced patterns (Phase 6 extension)
│       │   ├── __init__.py
│       │   └── cipher_class.py        # CaesarCipher class wrapper
│       │
│       └── api/                       # FastAPI layer (docs/02_deployment)
│           ├── __init__.py
│           ├── app.py                 # FastAPI app instance
│           ├── routes.py              # Endpoint definitions
│           ├── models.py              # Pydantic request/response models
│           └── config.py              # API settings
│
├── tests/
│   ├── __init__.py
│   └── integration/
│       └── test_cli_flow.py           # End-to-end CLI tests
│
├── docs/
│   ├── 00_overview/
│   ├── 01_instructions/
│   ├── 02_deployment/
│   └── 03_project_story/
│       ├── 00_caesar_historical_context.md
│       └── resources/
│
└── .gitignore
```

## What Each Folder Does

### `src/caesar_ciphon/`
The main Python package. Your cipher logic and CLI live here.

| Folder | Purpose | When You Use It |
|--------|---------|-----------------|
| **practice/** | Experimental, learning-focused code | Phases 1–4: Building and testing ideas |
| **core/** | Clean, testable, reusable functions | Phases 5–6: Refactoring and finalizing |
| **optional/** | Advanced patterns (classes) | Phase 6 extension: Optional class wrapper |
| **api/** | HTTP endpoints and FastAPI setup | docs/02_deployment: If deploying to API |

### Key Relationship

```
practice/ ──(refactor)──▶ core/ ──(wrap)──▶ optional/
                          ▲
                          │
                          └─(reuse)──▶ api/
```

**Workflow:**
1. **Phases 1–4**: Write messy, experimental code in `practice/`
2. **Phase 5**: Extract reusable logic into `core/` with tests
3. **Phase 6**: Optional: wrap core functions in a class in `optional/`
4. **docs/02_deployment**: Optional: expose core functions via FastAPI in `api/`

## Full Directory Tree (Fully Built Out)

Here's what a complete project looks like with all phases and files:

```plaintext
caesar_ciphon_template/
│
├── README.md
├── pyproject.toml
├── .gitignore
│
├── src/
│   └── caesar_ciphon/
│       ├── __init__.py
│       │   # Exports: from caesar_ciphon.core import encrypt, decrypt
│       │
│       ├── main.py
│       │   # CLI entry point
│       │   # Contains: main() function with user prompts and mode selection
│       │
│       ├── practice/
│       │   ├── __init__.py
│       │   ├── phase_1_shift_char.py
│       │   │   # shift_char(char, shift) -> str
│       │   │   # Notes and exploratory code from Phase 1
│       │   │
│       │   ├── phase_2_message_loop.py
│       │   │   # encrypt_message(message, shift) -> str
│       │   │   # decrypt_message(message, shift) -> str
│       │   │   # Exploratory code from Phase 2
│       │   │
│       │   ├── phase_3_validation.py
│       │   │   # validate_shift(shift) -> bool
│       │   │   # Error handling and retry logic from Phase 3
│       │   │
│       │   └── phase_4_batch_data.py
│       │       # Batch processing with lists/dicts from Phase 4
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   │   # Exports:
│       │   │   #   from caesar_ciphon.core import encrypt, decrypt
│       │   │   #   from caesar_ciphon.core import InvalidShiftError, CaesarCipherError
│       │   │
│       │   ├── cipher.py
│       │   │   # encrypt(message: str, shift: int) -> str
│       │   │   # decrypt(message: str, shift: int) -> str
│       │   │   # shift_char(char: str, shift: int, alphabet: str) -> str
│       │   │
│       │   ├── validation.py
│       │   │   # validate_shift(shift: int) -> bool
│       │   │   # validate_message(message: str) -> bool
│       │   │   # Raises InvalidShiftError, InvalidMessageError
│       │   │
│       │   ├── errors.py
│       │   │   # CaesarCipherError (base)
│       │   │   # InvalidShiftError
│       │   │   # InvalidMessageError
│       │   │
│       │   ├── alphabet.py
│       │   │   # LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
│       │   │   # UPPERCASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
│       │   │   # get_alphabet(case: str) -> str
│       │   │
│       │   ├── types.py
│       │   │   # Type hints and constants
│       │   │   # VALID_SHIFT_RANGE = (1, 25)
│       │   │
│       │   └── tests/
│       │       ├── __init__.py
│       │       │
│       │       ├── test_cipher.py
│       │       │   # test_shift_char_normal()
│       │       │   # test_shift_char_wraparound()
│       │       │   # test_encrypt_message()
│       │       │   # test_decrypt_reverses_encrypt()
│       │       │
│       │       ├── test_validation.py
│       │       │   # test_validate_shift_valid()
│       │       │   # test_validate_shift_invalid()
│       │       │   # test_exception_messages()
│       │       │
│       │       └── test_edge_cases.py
│       │           # test_empty_message()
│       │           # test_punctuation_preservation()
│       │           # test_mixed_case()
│       │           # test_unicode_handling()
│       │
│       ├── optional/
│       │   ├── __init__.py
│       │   │
│       │   └── cipher_class.py
│       │       # class CaesarCipher:
│       │       #     def __init__(self, shift: int, alphabet: str = "lowercase")
│       │       #     def encrypt(self, message: str) -> str
│       │       #     def decrypt(self, message: str) -> str
│       │       #     (All methods delegate to core functions)
│       │
│       └── api/
│           ├── __init__.py
│           │
│           ├── app.py
│           │   # FastAPI application setup
│           │   # CORS, middleware config
│           │
│           ├── routes.py
│           │   # @app.post("/encrypt")
│           │   # @app.post("/decrypt")
│           │   # @app.get("/health")
│           │
│           ├── models.py
│           │   # class EncryptRequest(BaseModel)
│           │   # class DecryptRequest(BaseModel)
│           │   # class EncryptResponse(BaseModel)
│           │   # class ErrorResponse(BaseModel)
│           │
│           └── config.py
│               # API_TITLE = "Caesar Cipher API"
│               # API_VERSION = "1.0.0"
│               # DEBUG = False
│
├── tests/
│   ├── __init__.py
│   │
│   └── integration/
│       ├── __init__.py
│       │
│       └── test_cli_flow.py
│           # Integration tests for end-to-end workflows
│           # test_single_encrypt_decrypt()
│           # test_batch_processing()
│           # test_error_recovery()
│
├── docs/
│   ├── 00_overview/
│   │   ├── 00_course_overview.md
│   │   └── 01_project_structure.md (this file)
│   │
│   ├── 01_instructions/
│   │   ├── 01_phase_1_foundations.md
│   │   ├── 02_phase_2_message_processing.md
│   │   ├── 03_phase_3_validation_and_branching.md
│   │   ├── 04_phase_4_data_modeling.md
│   │   ├── 05_phase_5_function_modularization.md
│   │   └── 06_phase_6_capstone.md
│   │
│   ├── 02_deployment/
│   │   ├── 00_deployment_overview.md (under development)
│   │   ├── 01_refactor_checklist.md
│   │   └── 02_fastapi_setup.md
│   │
│   └── 03_project_story/
│       ├── 00_caesar_historical_context.md
│       └── resources/
│           ├── 01_project_story.md
│           ├── 02_project_story.md
│           ├── 03_project_story.md
│           ├── 04_project_story.md
│           ├── 05_project_story.md
│           ├── 06_project_story.md
│           ├── 07_project_story.md
│           ├── 08_project_story.md
│           └── 09_project_story.md
│
└── .gitignore
    # Python standard ignores:
    # __pycache__/
    # *.pyc
    # .pytest_cache/
    # .venv/
    # dist/
    # build/
```

## Phase Progression and File Creation

### Phases 1–4 (Learning Phase)
Files you create in `practice/`:
- Phase 1: `phase_1_shift_char.py` — first working shift logic
- Phase 2: `phase_2_message_loop.py` — message encryption
- Phase 3: `phase_3_validation.py` — error handling
- Phase 4: `phase_4_batch_data.py` — list/dict organization

### Phase 5 (Refactor Phase)
Extract from `practice/` into `core/`:
- `cipher.py` — clean, reusable functions
- `validation.py` — input validation
- `errors.py` — exception definitions
- `tests/` — test coverage

### Phase 6 (Capstone Phase)
Complete in `core/`, optionally extend in `optional/`:
- Finalize `core/` functions and tests
- Optionally: add `optional/cipher_class.py`
- Ensure `main.py` calls only `core/` functions

### Deployment (docs/02_deployment)
When ready to deploy to FastAPI:
- Create `api/` folder with FastAPI adapter layer
- `api/` imports only from `core/` (one-way dependency)
- No changes needed in `core/` to support `api/`

## Important Design Principles

### 1. **Separation of Concerns**
```
main.py (CLI orchestration)
  ↓
core/ (cipher logic)
  ├── cipher.py (transformation)
  ├── validation.py (guards)
  └── errors.py (exceptions)

optional/ (convenience wrapper)
  └── cipher_class.py (delegates to core)

api/ (HTTP adapter)
  ├── routes.py (delegates to core)
  └── models.py (Pydantic validation)
```

### 2. **One-Way Dependencies**
- `main.py` imports from `core/`
- `optional/` imports from `core/`
- `api/` imports from `core/`
- **But `core/` never imports from any of the above**

This ensures `core/` can be used in any context (CLI, class, API, testing) without modification.

### 3. **Test Proximity**
Tests live in `core/tests/` alongside the modules they test, so they're easy to find and run in isolation.

## Quick Reference: Where to Work

| Phase | Primary File | Secondary Files |
|-------|--------------|-----------------|
| 1 | `practice/phase_1_shift_char.py` | `main.py` for prompts |
| 2 | `practice/phase_2_message_loop.py` | — |
| 3 | `practice/phase_3_validation.py` | — |
| 4 | `practice/phase_4_batch_data.py` | — |
| 5 | `core/cipher.py`, `core/validation.py`, `core/tests/` | `core/errors.py` |
| 6 | `core/` (finalize), `optional/cipher_class.py` (if extending) | `tests/integration/test_cli_flow.py` |

---

Ready to start? Begin with [Phase 1: Foundations](../01_instructions/01_phase_1_foundations.md).
