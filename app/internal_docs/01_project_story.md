# The Story of Caesar's Traditional Secret Party

In the heart of ancient Rome 🏛️, Julius Caesar had a secret 🤫. Not just about gladiators 🗡️ or gold 💰, but about... a party 🍾! This year, he would host a secret party only for his closest friends. This party was the talk of the town 🙊! There were magical fairies ✨, dancing peacocks 🦚, melodious harps 🎵, and sparkling fountains ⛲.

However, there was a problem 😲! Uninvited guests 🥷 would crash the party because the location 🗺️ would get leaked by spies 🕵️‍♂️.

Caesar needed a plan 💡! He thought, "I'll send out the invites encrypted 🔐. That way, only my true friends 🤝 will know when and where the party is!".

So, he came up with a cunning plan 🦊. Instead of writing the party location of the invitation directly 🏞️, he would shift each letter in by a fixed number 🔢. So, for example, if he decided to shift by 3:

- A would become D 🔄
- B would become E 🔄
- C would become F 🔄
- ... and so on.

If the invite said "GARDEN" 🌳, he would write "JDUGHQ" 🤯.

When Brutus (Caesar's friend turned enemy) received the letter 📜, he knew about this secret code 🗝️. He would shift the letters back by the same number and decode "JDUGHQ" to "GARDEN" 🌳. Mmm, clever 🧠!

However, any nosy Romans 👀 intercepting the message would be baffled 😶‍🌫️! "JDUGHQ? What kind of place is that?" they would wonder 🤷‍♂️.

Thanks to the "Caesar Cipher" 🔐, Caesar's secret party remained exclusive 😼, magical 🌌, and crasher-free 🥳!

And while history 📖 might tell you that Brutus wasn't the most trustworthy of friends, at least in our story, he kept the party's secret 🎉 and never gave away the magical location 🌳! 😉🤫


# Exercise 📋

## Question 1 🤔

Based on the story of Julius Caesar's secret party and the Caesar Cipher, identify potential variables you would need. Please ensure you use appropriate variable naming conventions in JavaScript.

### Answer 🔑

- `partyLocation`
- `shiftValue`
- `encryptedMessage`
- `decryptedMessage`
- `isPartySafe`

Note: You can give different names to the same variables and even introduce additional variables. This is just for fun and understanding the concepts.

## Question 2 🤔

After identifying the variables from the story, specify their primitive data types in JavaScript. Also, provide these variables with some initial values.

### Answer 🔑

```
let partyLocation = "GARDEN"; // String
let shiftValue = 3; // Number
let encryptedMessage = ""; // String
let decryptedMessage = ""; // String
let isPartySafe = false; // Boolean

```

## Question 3 🤔

From the variables you've identified, determine which ones should be declared using `const` and which ones should use `let`.

### Answer 🔑

```
let partyLocation = "GARDEN"; // As the message might change.
const shiftValue = 3; // Since the shift value remains constant throughout.
let encryptedMessage = ""; // This will change when we encode the message with the original party location.
let decryptedMessage = ""; // This will change when we decode the encrypted message to reveal the party location.
let isPartySafe = false; // Hopefully, this doesn't change.

```

## Question 4 🤔

Given the variable `shiftValue`, write a piece of code to check if its value is an integer.

### Answer 🔑

```
const shiftValue = 3;
Number.isInteger(shiftValue);

```

The `Number.isInteger()` method determines whether the passed value is an integer. If `shiftValue` is an integer, it will return `true`; otherwise, it will return `false`.

# Fun Fact 🥳

The [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is one of the earliest known and simplest ciphers. It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.