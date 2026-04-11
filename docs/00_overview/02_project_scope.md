# Caesar Cipher Project Scope (Updated)

## Phase 1 — Core Character Shifting (Foundation)
- Shift alphabetic characters
- Preserve:
  - Uppercase/lowercase
  - Non-alphabet characters (unchanged)
- Handle:
  - Negative shifts
  - Large shifts using % 26

---

## Phase 2 — Encryption Function

Function:
encrypt(message: str, shift: int) -> str

Responsibilities:
1. Shift each valid character
2. Track processed letters (not symbols)
3. After every 2 valid letters:
   - Insert a random lowercase letter
4. Reset counter and continue

Rules:
- Only count letters, not spaces/punctuation
- Random letters must come from:
  "abcdefghijklmnopqrstuvwxyz"

---

## Phase 3 — Decryption Function

Function:
decrypt(encrypted_message: str, shift: int) -> str

Responsibilities:
1. Reverse the shift
2. Track letter positions
3. After every 2 real letters:
   - Skip the next character (random noise)

Key Insight:
- Decryption must both remove noise and reverse transformation

---

## Phase 4 — Shared Helper Function

Function:
shift_char(char: str, shift: int) -> str

Responsibilities:
- Shift a single character correctly
- Handle wrap-around (z → a)
- Preserve case

---

## Phase 5 — State Management

Use a counter:

count = 0

Encryption:
- Increment when processing a letter
- When count == 2:
  - Insert random character
  - Reset count

Decryption:
- Increment when processing real letters
- When count == 2:
  - Skip next character
  - Reset count

---

## Phase 6 — Testing

Test Cases:
- "abc" → "def"
- "xyz" → "abc"
- "Hello, World!" (preserved formatting)
- Encryption adds noise (longer output)
- Decryption restores original message
- Large shift (42 == 16)
- Negative shifts

---

## Suggested Structure

caesar_cipher/
├── cipher.py
├── test_cipher.py
└── README.md

---

## Definition of Done

- encrypt() correctly adds noise
- decrypt() reconstructs original message
- No duplicated shift logic
- Edge cases handled
- Code is clean and readable

---

## What This Project Tests

- Loop state management
- Reversible transformations
- Clean function design
