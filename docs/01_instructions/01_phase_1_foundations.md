# Phase 1: Foundations (Single-Character Cipher)

## Phase Title and Why It Matters

Build the first working cipher behavior by shifting one letter safely. This phase teaches the core idea behind Caesar's cipher and gets your first CLI working, giving you confidence and momentum for the phases ahead.

## Teaching Goals

- Explain what Caesar shifting does and why alphabet wraparound is necessary
- Use clear variables to hold message character and shift value
- Produce deterministic, correct output for single-character input
- Understand alphabet indexing and modulo arithmetic for cycling

## Story Context

Caesar faced an urgent military challenge during the Gallic Wars (58–50 BCE): how could he send secret orders to generals across vast distances without enemies intercepting and exploiting them?

His solution was elegant: a simple but consistent letter-shift pattern that only recipients who knew the shift value could decipher. 

During the Gallic Wars, Caesar's military campaigns spanned hundreds of miles. Brutus, Cicero, Antony, and other commanders needed coordinated orders. A captured message with no encryption could mean a lost battle. But a message that looked like gibberish to an enemy? That gave him the security he needed.

This phase is where you build that first core unit: **the single-letter shift**—the engine that makes Caesar's cipher work. It's simple, but it was effective for over a century because no one had yet developed the mathematical tools to crack it.

## Build Tasks

1. **Create a CLI prompt** that asks the user for a single letter and a shift amount
   - Save the letter to a variable (e.g., `letter`)
   - Save the shift to a variable (e.g., `shift`)

2. **Implement lowercase shift logic**
   - Convert the letter to its position in the alphabet (0–25)
   - Add the shift value
   - Use modulo (%) to wrap around: if result is past 'z', cycle back to 'a'
   - Convert the result back to a letter

3. **Add wraparound handling**
   - Test with boundary letters: 'x' + 3 should give 'a', not an error
   - Test with 'z' + 1 should give 'a'
   - Confirm your modulo logic handles all 26 letters

## Completion Check

Run your program and show output for **at least three test cases**, including edge letters:
- Normal letter: 'a' + 3 = 'd'
- Boundary wrap: 'x' + 3 = 'a'
- Another wrap: 'z' + 1 = 'a'

**What clean output looks like:**
```
Enter a letter: a
Enter shift amount: 3
Result: d

Enter a letter: x
Enter shift amount: 3
Result: a
```

## Reflection Questions

1. **Which part of the wraparound logic was hardest to reason about?** Did the modulo operator surprise you at first, or did it click right away?

2. **What variable names made your code easiest to read?** Did you consider alt names like `encrypted_char` vs `result`? Why did one feel clearer?

3. **What boundary case revealed a bug first?** Did your wraparound work for all 26 letters, or did certain combinations break your first attempt?

## Stretch Challenge

**Support uppercase letters without duplicating logic.**

Right now you shift lowercase 'a' through 'z'. Extend your code to also handle 'A' through 'Z' with the same shift amount. Challenges:
- How do you detect if input is uppercase vs lowercase?
- How do you find the position of uppercase letters in a similar way to lowercase?
- Can you reuse the same modulo wraparound logic?

Try to solve this without copying your entire algorithm twice.

## Next Phase Bridge

Great start! You've built a working single-letter cipher and understand wraparound. In **Phase 2**, you'll loop this logic over entire messages so Caesar can encrypt full invitation lines, not just symbols. You'll also implement decryption—the reverse process.
