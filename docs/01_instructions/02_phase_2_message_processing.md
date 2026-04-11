# Phase 2: Full Message Processing (Loops)

## Phase Title and Why It Matters

Scale your letter-shifting logic to entire invitation messages. This phase teaches iteration and the power of loops—applying the same operation repeatedly to build complex behavior from simple steps. You'll also implement decryption, the reverse process.

## Teaching Goals

- Apply shift logic repeatedly across a full string using loops
- Preserve non-alphabet characters (spaces, punctuation) without corruption
- Implement matching encrypt and decrypt behavior in CLI workflow
- Understand the symmetry between encrypt and decrypt operations

## Story Context

Caesar now needs to encrypt complete invitation lines like "Garden at sunset" or "Forum near the steps", not just single symbols. He also needs a way to decrypt—to reverse a shift—so recipients can read the message.

## Build Tasks

1. **Build the encrypt loop**
   - Prompt user for a full message (not just one letter)
   - Loop through each character in the message
   - For alphabetic characters, apply your Phase 1 shift logic
   - For non-alphabetic characters (spaces, punctuation, numbers), leave them unchanged
   - Collect results into an encrypted message and display it

2. **Build the decrypt loop**
   - Prompt user for an encrypted message and a shift amount
   - Use a reverse shift (subtract instead of add) to undo encryption
   - Apply the same logic: only shift alphabetic characters
   - Verify: decrypt(encrypt(X)) == X

3. **Add CLI mode selection**
   - Prompt user: "Encrypt or Decrypt?"
   - Call the appropriate function based on their choice
   - Handle both uppercase and lowercase input for their mode choice

## Completion Check

Run your program and show output for at least **two end-to-end encrypt/decrypt cycles**:

**Example 1:**
```
Mode: Encrypt
Message: hello world
Shift: 3
Result: khoor zruog

Mode: Decrypt
Message: khoor zruog
Shift: 3
Result: hello world
```

**Example 2:**
```
Mode: Encrypt
Message: Meet at the forum!
Shift: 5
Result: rjjy f ymj yjwrd!

Mode: Decrypt
Message: rjjy f ymj yjwrd!
Shift: 5
Result: Meet at the forum!
```

Verify that punctuation and spaces stay in the same position and aren't corrupted.

## Reflection Questions

1. **How did you avoid code duplication between encrypt and decrypt?** Did you consider using a helper function, or did you write the shift logic twice? What trade-off did you make?

2. **What should happen to punctuation, numbers, and spaces?** Why leave them unchanged instead of encrypting them too? What breaks if you do encrypt them?

3. **Which loop design simplified debugging?** Did you test character-by-character first, or did you build the whole loop at once? What helped you spot where things went wrong?

## Stretch Challenge

**Add configurable alphabet mode and describe the constraints.**

Right now you shift lowercase and uppercase separately within their ranges (a–z and A–Z). What if someone wanted to use a different alphabet? For example:
- Only lowercase (a–z)
- Only uppercase (A–Z)
- Include digits (a–z plus 0–9)

Design (but don't necessarily implement) how you'd support this. What parts of your code would need to change? What constraints does each mode have? Bonus: implement one alternate mode and test it.

## Next Phase Bridge

Excellent! You've built a working message encryptor/decryptor. In **Phase 3**, you'll add robustness: validate user inputs, handle errors gracefully, and optionally randomize the shift value for stronger secrecy. You'll also make your CLI more reliable and user-friendly.
