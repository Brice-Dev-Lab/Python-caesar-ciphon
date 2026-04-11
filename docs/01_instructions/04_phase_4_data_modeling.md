# Phase 4: Data Modeling (Lists and Dictionaries)

## Phase Title and Why It Matters

Organize multiple invitations and related metadata cleanly. This phase teaches data structures—lists for collections and dictionaries for organizing information around a single item. You'll move from processing one message at a time to handling batches, and you'll learn to separate data from logic.

## Teaching Goals

- Use lists to store collections of messages
- Use dictionaries to organize per-message metadata (recipient, shift, message)
- Separate data storage from cipher transformation logic
- Display batch results in a readable CLI format, like a table

## Story Context

Caesar now coordinates invitations to many guests: Brutus, Cicero, Antony, and others. Each invitation needs its own shift and may have special metadata. He wants to prepare all of them at once and see a summary of what was prepared.

## Build Tasks

1. **Create a list of message dictionaries**
   - Build a list where each item is a dictionary with fields:
     ```python
     messages = [
         {"recipient": "Brutus", "message": "Garden at sunset", "shift": 3},
         {"recipient": "Cicero", "message": "Forum near steps", "shift": 5},
         {"recipient": "Antony", "message": "Temple at dawn", "shift": 7},
     ]
     ```
   - You can hardcode this for Phase 4, or accept it from user input

2. **Loop through the list and encrypt each message**
   - For each message dictionary in the list:
     - Extract the message text and shift
     - Apply your Phase 2 encrypt logic
     - Store the encrypted result back in the dictionary (add a new field like "encrypted")

3. **Display batch results in a readable format**
   - Print a summary for each message showing:
     - Recipient name
     - Original message
     - Shift used
     - Encrypted result
   - Format it clearly, like a table or indented section per recipient

## Completion Check

Show a batch run with **at least three messages** processed and displayed:

**Example output:**
```
Processing 3 invitations...

1. Brutus
   Original: Garden at sunset
   Shift: 3
   Encrypted: Jdughq dw vxqvhw

2. Cicero
   Original: Forum near steps
   Shift: 5
   Encrypted: Ksvym sidu yjuxt

3. Antony
   Original: Temple at dawn
   Shift: 7
   Encrypted: Altnsl ha iamf

All invitations ready for delivery.
```

## Reflection Questions

1. **Which fields belong in metadata vs computed output?** For example, is "shifted value used" metadata, or is "encrypted result" computed output? Why does the distinction matter?

2. **What data structure choice improved readability the most?** Did dictionaries with named keys feel clearer than tuples or lists of values? Why?

3. **What parts feel hardest to test as complexity grows?** For example, if you have 100 invitations, how would you verify they're all correct without reading through every one?

## Stretch Challenge

**Add optional JSON input/output while keeping cipher functions pure.**

Add a feature that reads messages from a JSON file and writes encrypted results to another JSON file:
```json
// input.json
[
  {"recipient": "Brutus", "message": "Garden at sunset", "shift": 3},
  {"recipient": "Cicero", "message": "Forum near steps", "shift": 5}
]
```

Your cipher functions don't change—they still take a message and shift and return encrypted text. But your CLI layer now reads JSON, loops through items, encrypts each one, and writes the result to `output.json`.

This prepares you for Phase 5, where you'll separate CLI logic from core cipher logic even more cleanly.

## Next Phase Bridge

Excellent progress! You now manage complex data and process multiple items. In **Phase 5**, you'll refactor all your code into clean, focused functions: some for cipher logic (pure functions that just transform text), and some for CLI orchestration. This separation will make your code testable and reusable—and ready for deployment later.
