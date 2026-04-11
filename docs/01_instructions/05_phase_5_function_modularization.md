# Phase 5: Function Modularization and Clean Refactor

## Phase Title and Why It Matters

Transform working code into maintainable, reusable architecture. This phase teaches you to refactor: extracting repeated logic into functions, isolating pure cipher logic from CLI interaction, and creating testable modules. This is where your code goes from "working" to "professional."

## Teaching Goals

- Extract small, single-responsibility functions from monolithic scripts
- Separate pure cipher logic from CLI orchestration code
- Design function interfaces that are easy to test
- Build clean boundaries so core logic can be reused (e.g., for FastAPI later)
- Write and run tests for core functions without needing interactive input

## Story Context

Caesar has a working system, but as complexity grows, duplicated code and tangled logic are becoming a liability. He needs a reliable tool that can be maintained, tested, and extended. This is where professional architecture comes in.

## Build Tasks

1. **Extract cipher functions into a `core` module**
   - Create a new file: `src/caesar_ciphon/core/cipher.py`
   - Move your single-character shift logic into a function (e.g., `shift_char(char, shift)`)
   - Move your message encryption logic into a function (e.g., `encrypt(message, shift)`)
   - Move your message decryption logic into a function (e.g., `decrypt(message, shift)`)
   - These functions should:
     - Take only the data they need as parameters
     - Return only the result, no side effects
     - Be testable without user input

2. **Extract validation functions**
   - Create `validate_shift(shift)` — returns True if shift is valid, raises exception if not
   - Create `validate_message(message)` — returns True if message is OK, raises exception if not
   - Use clear exception names so callers know why validation failed

3. **Keep CLI logic in `main.py`**
   - `main.py` prompts for user input, validates it, calls core functions, and displays results
   - `main.py` imports and uses your core functions, but doesn't implement cipher logic itself
   - Example structure:
     ```python
     from caesar_ciphon.core import cipher, validation
     
     def main():
         mode = input("Encrypt or Decrypt? ")
         message = input("Enter message: ")
         shift = int(input("Enter shift: "))
         
         validation.validate_shift(shift)
         result = cipher.encrypt(message, shift)
         print(f"Result: {result}")
     ```

4. **Add tests for core functions**
   - Create `src/caesar_ciphon/core/test_cipher.py`
   - Write tests that call core functions directly (no user input needed)
   - Test at least:
     - Normal case: encrypt 'a' with shift 1 = 'b'
     - Wraparound: encrypt 'z' with shift 1 = 'a'
     - Spaces and punctuation: encrypt 'Hello, World!' with shift 3 = 'Khoor, Zruog!'
     - Decrypt reverses encrypt: decrypt(encrypt(X)) == X
   - Run tests without prompting for input

## Completion Check

Show the results of:
1. **Imported core functions** running under tests:
   ```
   python -m pytest src/caesar_ciphon/core/test_cipher.py
   
   test_shift_char_normal PASSED
   test_shift_char_wraparound PASSED
   test_encrypt_message PASSED
   test_decrypt_reverses_encrypt PASSED
   ```

2. **CLI still works** by calling core functions:
   ```
   python src/caesar_ciphon/main.py
   Encrypt or Decrypt? encrypt
   Enter message: hello
   Enter shift: 3
   Result: khoor
   ```

## Reflection Questions

1. **Which extracted function improved clarity the most?** Was it obvious what each function should do, or did you refactor multiple times before settling on clean boundaries?

2. **Where did refactoring remove the most duplication?** For example, did you have encrypt and decrypt logic that were nearly identical before extraction?

3. **Which boundary protects core logic from CLI coupling?** How do you ensure that core functions don't accidentally depend on user input or print statements?

## Stretch Challenge

**Add batch command mode that reuses the same core functions.**

Enhance your CLI to support a batch mode:
```
python src/caesar_ciphon/main.py --batch messages.json
```

This mode:
- Reads a JSON file of messages and shifts
- Calls your core `encrypt()` function for each one
- Writes results to an output JSON file

The key: your core cipher functions don't change. You're just building a new CLI wrapper around them. This shows the power of clean separation.

## Next Phase Bridge

Perfect! You've transformed your code into a professional, testable system. In **Phase 6 (Capstone)**, you'll finalize your CLI experience, ensure comprehensive test coverage, and optionally add a class wrapper that makes repeated configurations easier while still delegating to your same core functions.
