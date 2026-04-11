# Caesar Ciphon Course Overview

Welcome to the Caesar Ciphon Lab—a hands-on, function-first Python course where you build a working encryption tool from the ground up.

## What You'll Learn

This course teaches core programming concepts through a **CLI-first** approach:
- **Variables and data types** — storing messages and shift values
- **Loops and iteration** — processing strings character by character
- **Conditionals and validation** — handling edge cases and errors
- **Functions and modularity** — organizing reusable, testable code
- **Data structures** — lists and dictionaries for organizing complex data
- **Testing and debugging** — verifying code behavior at each step

By the end, you will have:
- A working CLI cipher tool
- Clean, testable function-based code
- An understanding of why good architecture matters
- An optional path to refactor your work into a FastAPI deployment

## 6-Phase Learning Path

### Phase 1: Foundations
Build single-character shift logic and CLI basics.  
*Learn:* variables, string indexing, wraparound logic  
*Build:* first working cipher for one letter

### Phase 2: Full Message Processing
Scale to entire messages using loops.  
*Learn:* iteration, encryption/decryption flow  
*Build:* CLI that encrypts and decrypts complete messages

### Phase 3: Validation and Branching
Add safeguards and mode branching.  
*Learn:* input validation, conditionals, random behavior  
*Build:* CLI that handles errors and optional random shifts

### Phase 4: Data Modeling
Organize multiple messages and metadata.  
*Learn:* lists, dictionaries, data separation  
*Build:* CLI that processes batch messages with metadata

### Phase 5: Function Modularization
Refactor into clean, reusable functions.  
*Learn:* single responsibility, pure functions, test design  
*Build:* core modules ready for deployment

### Phase 6: Capstone
Deliver a polished CLI product with optional class extension.  
*Learn:* integration, architecture choices  
*Build:* final cipher system with tests; optionally add class wrapper

## Scope

**This course is CLI-first.** All core learning is built and tested in the terminal. FastAPI deployment is optional and comes later in [docs/02_deployment](../../02_deployment) if you choose.

## Required vs Optional

| Path | What You Must Do | What's Optional |
|------|------------------|-----------------|
| **Core** | Phases 1–6 with function-based implementation | Deploy to FastAPI |
| **Function-First** | All phases use functions | Class wrapper in Phase 6 |
| **Advanced** | Add class automation and strategy patterns | Configure custom alphabets |

## Expected Time

Plan for **4–8 hours** total, depending on how much you explore stretch challenges.

## The Real Story Behind Caesar's Cipher

Before diving into code, understand the history. Julius Caesar used his cipher during the Gallic Wars (58–50 BCE) for sensitive military communications—and it **was never cryptanalytically compromised**. It wasn't broken by enemy codebreakers; it was betrayed by a trusted insider (Brutus, among others).

This tells us something important: **encryption secures against external eavesdropping, not against insiders with the key.** It also shows that simple, well-understood systems can be remarkably effective if designed for the right threat model.

Read [The True Story Behind Caesar's Cipher](../03_project_story/00_caesar_historical_context.md) to understand the context, geography, threats, and why this design choice mattered. Your 6-phase journey will follow Caesar's actual problem-solving arc.

## Before You Start Coding

1. Fork this repository to your own GitHub account.
2. Clone your fork locally.
3. You'll need Python 3.8+ and a text editor or IDE (VS Code, PyCharm, etc.).
4. Familiarity with the terminal/command line is helpful but not required.
5. Read the historical context (linked above) — it will make each phase more meaningful.

## How to Use These Docs

1. Start here to understand the scope and 6-phase map.
2. Head to [docs/01_instructions](../01_instructions) to begin Phase 1.
3. Follow each phase in order; each builds on the prior one.
4. At the end of each phase, reflect on the questions provided.
5. If you want more complexity, tackle a stretch challenge.
6. After Phase 6 capstone, optionally explore [docs/02_deployment](../../02_deployment) for FastAPI.

## Philosophy

This course emphasizes:
- **Learning by building**, not lecturing
- **Function-first design** before classes or patterns
- **Testable code** from the start
- **Clean boundaries** so your work is reusable and deployable
- **Reflection**, not just code—understanding *why* decisions matter

Have fun, experiment boldly, and make your fork your own!
