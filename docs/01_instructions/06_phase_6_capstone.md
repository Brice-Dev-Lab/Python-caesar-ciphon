# Phase 6: Capstone (Function-First, Optional Class Extension)

## Phase Title and Why It Matters

Deliver a polished CLI cipher product and evaluate architecture choices. This capstone consolidates everything you've learned: clean functions, robust validation, batch processing, and excellent test coverage. You'll also explore when a class wrapper adds value versus unnecessary complexity.

## Teaching Goals

- Complete an end-to-end function-first CLI cipher workflow from prompt to results
- Demonstrate robust test coverage for happy paths, edge cases, and error scenarios
- Establish clear, maintainable module boundaries and interfaces
- Evaluate when class abstraction improves code versus when it adds noise
- Prepare your codebase for optional future deployment (FastAPI or otherwise)

## Story Context

Final mission: Caesar needs a reliable, complete cipher system that handles realistic message complexity, preserves data integrity, and scales to many recipients. The system must be trustworthy, understandable, and ready for whatever comes next—whether that's additional features, API deployment, or handoff to others.

## Build Tasks

### Required Path: Function-First Capstone
1. **Finalize CLI behavior**
   - Single-message mode: encrypt/decrypt one message at a time
   - Batch mode: process multiple messages from a file
   - Clear prompts and user-friendly error recovery
   - Informative output (summary, results, next steps)

2. **Implement comprehensive tests**
   - Test encrypt/decrypt for normal cases, boundary cases, and edge cases
   - Test validation (invalid shifts, empty messages, etc.)
   - Test that validation exceptions are raised with clear messages
   - Test batch processing with mixed message types
   - Ensure decryption strictly reverses encryption
   - Target: at least 90% code coverage of core functions

3. **Document your interface**
   - Add docstrings to core functions explaining:
     - What the function does
     - What parameters it expects
     - What it returns
     - Any exceptions it raises
   - Example:
     ```python
     def encrypt(message, shift):
         """Encrypt a message using Caesar cipher.
         
         Args:
             message (str): Text to encrypt
             shift (int): Shift amount (1-25)
         
         Returns:
             str: Encrypted message
         
         Raises:
             ValueError: If shift is outside valid range
         """
     ```

4. **Create a polished main CLI entry**
   - Clear menu system (encrypt, decrypt, batch, exit)
   - Graceful error handling and recovery
   - Informative messages and confirmations
   - Optional run summaries showing input size, operation, and result snippet

### Optional Path: Class Wrapper (Advanced)
If you choose to add a class, create a thin wrapper around core functions:

```python
class CaesarCipher:
    def __init__(self, shift, alphabet="lowercase"):
        """Initialize cipher with a fixed shift value.
        
        This wraps core functions to reduce parameter repetition
        for scenarios where the same shift is used many times.
        """
        self.shift = shift
        self.alphabet = alphabet
    
    def encrypt(self, message):
        """Encrypt using stored shift value."""
        return core.encrypt(message, self.shift, self.alphabet)
    
    def decrypt(self, message):
        """Decrypt using stored shift value."""
        return core.decrypt(message, self.shift, self.alphabet)
```

Key principles:
- The class delegates to core functions; it doesn't duplicate logic
- Tests for the class call the same core tests under the hood
- The class is optional and not required for capstone completion
- Use the class only if it reduces meaningful repetition

## Completion Check

### Required path acceptance checklist:
- ✓ CLI runs without crashes for normal inputs
- ✓ Tests pass: `pytest src/caesar_ciphon/core/test_cipher.py` shows green
- ✓ Batch mode processes multiple messages correctly
- ✓ Invalid inputs trigger clear error messages with retry prompts
- ✓ Decrypt strictly reverses encrypt (verified by tests)
- ✓ Core functions have docstrings
- ✓ Main menu is clear and navigation is intuitive

### Optional class path acceptance checklist:
- ✓ CaesarCipher class and core functions produce identical outputs
- ✓ Class tests pass with no regression in core behavior
- ✓ Class docstrings clarify when it's useful vs unnecessary

### Example output:
```
===== Caesar Cipher CLI =====
1. Encrypt single message
2. Decrypt single message
3. Batch process (file)
4. Exit

Choose option: 1
Enter message: Meet at the forum!
Enter shift (1-25): 5
Result: Rjjy fy ymj yjwrd!

===== RUN SUMMARY =====
Input: 18 characters
Shift: 5
Output: Rjjy fy ymj yjwrd!

Continue? (y/n): n
Thank you for using Caesar Cipher.
```

## Reflection Questions

1. **Why was function-first sufficient for the core requirements?** Did you feel the need for classes, or did pure functions handle everything cleanly?

2. **If you added a class wrapper, what repetition did it reduce?** For example, did you find yourself specifying the same shift over and over, making a class a useful convenience?

3. **What is the first refactor you would make before API deployment?** For example, would you add input streaming, support for custom alphabets, or better error categorization? Why that first?

## Stretch Challenge

**Add configurable strategy mode while maintaining backward-compatible CLI behavior.**

Introduce a "cipher strategy" system:
```
Choose cipher strategy:
1. Standard Caesar (shift only, a-z + A-Z)
2. Digits included (a-z + A-Z + 0-9)
3. Custom (user defines alphabet)
```

Requirements:
- CLI still works for users who just want standard Caesar
- Strategy can be selected at runtime or via command-line argument
- Core functions remain unchanged; strategy is applied at the CLI layer
- Tests verify each strategy works independently

This demonstrates how clean architecture supports feature extension without breaking existing functionality.

## Deployment Readiness

After this capstone, your code is ready for:
- **Further extension**: add features or strategies without rewriting core
- **Deployment**: FastAPI refactor in [docs/02_deployment](../../02_deployment)
- **Handoff**: other developers can read and extend cleanly

If you wish to deploy to FastAPI, proceed to [docs/02_deployment](../../02_deployment) for the optional refactor guide.

## Final Reflection

Congratulations! You've built a complete cipher system from scratch. You've learned:
- Core programming concepts through a real project
- How clean architecture makes code reliable and reusable
- The difference between quick prototypes and production-ready systems
- When abstractions (functions, classes, strategies) add clarity vs complexity

Well done. Now go experiment, extend, and share your work!
