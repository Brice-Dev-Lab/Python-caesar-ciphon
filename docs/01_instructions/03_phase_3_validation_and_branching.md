# Phase 3: Validation and Branching (Control Flow)

## Phase Title and Why It Matters

Prevent invalid states and improve CLI reliability. This phase teaches validation and branching—using conditionals to check inputs before processing them and to handle different scenarios. It also introduces optional randomized shift behavior for stronger secrecy.

## Teaching Goals

- Validate user input before processing (shift range, message type, etc.)
- Use branching to handle multiple CLI modes and recovery scenarios
- Add clear, helpful error messages that guide users to fix mistakes
- Optionally implement bounded random shift generation for security variety

## Story Context

Caesar wants a system that's safe and forgiving. If a recipient enters an invalid shift, the program should explain the problem and ask again, not crash. He also wants the ability to vary the shift occasionally to make his cipher harder to break.

## Build Tasks

1. **Add shift validation**
   - Define acceptable shift ranges (e.g., 1–25 for standard alphabet)
   - Before encrypting/decrypting, check that shift is in range
   - Display a clear error message if shift is invalid
   - Ask the user to re-enter the shift

2. **Add message validation**
   - Check that message is not empty
   - Optionally check for unsupported character types
   - Display helpful guidance if input is rejected

3. **Add CLI error recovery**
   - When validation fails, re-prompt the user instead of crashing
   - Loop until valid input is received
   - Use clear language: "Shift must be between 1 and 25. Try again:"

4. **Add optional random shift mode**
   - Offer the user a choice: "Use fixed shift or random shift?"
   - If random, generate a shift value in a safe range (e.g., 1–25) using `random.randint()`
   - Display the shift value so the recipient knows how to decrypt
   - Show that random shifts work differently each run

## Completion Check

Show output for **at least three scenarios**: one valid run, one invalid-shift recovery, and one random shift:

**Example 1 (Valid with fixed shift):**
```
Enter mode (encrypt/decrypt): encrypt
Enter message: hello
Enter shift (1-25): 5
Result: mjqqt
```

**Example 2 (Invalid shift, recovery):**
```
Enter mode (encrypt/decrypt): encrypt
Enter message: hello
Enter shift (1-25): 100
Error: Shift must be between 1 and 25. Try again.
Enter shift (1-25): 5
Result: mjqqt
```

**Example 3 (Random shift):**
```
Enter mode (encrypt/decrypt): encrypt
Enter message: hello
Use fixed shift or random? (1 for fixed, 2 for random): 2
Random shift selected: 12
Result: tsvvc
```

## Reflection Questions

1. **Which validation catches the most common learner mistakes?** Did your error messages help users self-correct, or did they stay confused?

2. **When should the app stop execution vs ask for a retry?** For example, should an empty message stop the program, or retry the prompt? Why did you make that choice?

3. **How does random shift mode affect reproducibility and testing?** If you want to test your code, can you rely on random shifts, or do you need to make randomness optional?

## Stretch Challenge

**Add a run-summary output that shows the operation at a glance.**

After encrypting or decrypting, display a summary like:
```
===== RUN SUMMARY =====
Operation: Encrypt
Input length: 5
Shift used: 5
Output: mjqqt
```

Or for random mode:
```
===== RUN SUMMARY =====
Operation: Encrypt
Input length: 5
Shift used: 12 (random)
Output: tsvvc
```

This summary helps users trust the output and prepares them for batch processing in the next phase.

## Next Phase Bridge

Perfect! Your CLI is now robust and user-friendly. In **Phase 4**, you'll organize multiple messages and their metadata using lists and dictionaries. You'll process several invitations at once and display results in a structured way, preparing for larger-scale operation.
