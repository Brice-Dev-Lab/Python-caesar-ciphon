# **Technical Skills Survey** Project Part 2: Exercise 8 - Caesar's Cipher Reloaded

# Caesar's Cipher Reloaded

In ancient Rome 🏛️, Julius Caesar was impressed by the effectiveness of his cipher. But as the secret parties grew more popular 🎉, manually shifting each letter became tedious. It was time for automation! Caesar summoned his best scribes and mathematicians 📜 to design a system - a system that could encrypt and decrypt messages at will!

# Exercise 📋

You are given the below code:

```jsx
const friend = "BRUTUS";
const shiftValue = 3;
const alphabet = "abcdefghijklmnopqrstuvwxyz";
```

Incorporate the following steps into a single JavaScript file, placing the provided code at the top. Insert your answers to the questions as comments where they appear.

## Step 1 🧩

Create a function named `encryptLetter` that takes a letter and a shift value as parameters. This function should return the encrypted version of the letter.

### Hint 💡

- Inside the function, find the index of the letter in the alphabet.
- Add the shift value to this index.
- Use the modulus operator to ensure wrapping around the alphabet if necessary.
- Return the encrypted letter.

### Answer 🔑

```jsx
function encryptLetter (letter, shift)
{
  const index = alphabet.indexOf(letter.toLowerCase());
  const newIndex = (index + shift) % alphabet.length;
  return alphabet[newIndex];
}
```

## Step 2 🧩

Create a function named `encryptMessage` that takes a word and a shift value as parameters. This function should return the encrypted version of the entire word.

### Hint 💡

- Use a loop to iterate over each letter in the word.
- For each letter, call the `encryptLetter` function.
- Construct the encrypted message.
- Return the encrypted message.

### Answer 🔑

```jsx
function encryptMessage (word, shift)
{
  let encryptedMessage = "";
  for (let i = 0; i < word.length; i++)
  {
    encryptedMessage += encryptLetter(word[i], shift);
  }
  return encryptedMessage;
}
```

## Step 3 🧩

Create a function named `decryptLetter` that takes an encrypted letter and a shift value as parameters. This function should return the decrypted version of the letter.

### Hint 💡

- Inside the function, find the index of the letter in the alphabet.
- Subtract the shift value from this index.
- Use the modulus operator to ensure wrapping around the alphabet if necessary. Remember to handle negative values correctly.
- Return the decrypted letter.

### Answer 🔑

```jsx
function decryptLetter (letter, shift)
{
  const index = alphabet.indexOf(letter.toLowerCase());
  const newIndex = (index - shift + alphabet.length) % alphabet.length;
  return alphabet[newIndex];
}
```

## Step 4 🧩

Create a function named `decryptMessage` that takes an encrypted word and a shift value as parameters. This function should return the decrypted version of the entire word.

### Hint 💡

- Use a loop to iterate over each letter in the word.
- For each letter, call the `decryptLetter` function.
- Construct the decrypted message.
- Return the decrypted message.

### Answer 🔑

```jsx
function decryptMessage (word, shift)
{
  let decryptedMessage = "";
  for (let i = 0; i < word.length; i++)
  {
    decryptedMessage += decryptLetter(word[i], shift);
  }
  return decryptedMessage;
}
```

## Question 🤔

If Caesar encrypts the word "BRUTUS" using our `encryptMessage` function and then decrypts the result using our `decryptMessage` function, will he get "BRUTUS" back? Why or why not?

### Answer 🔑

Yes, Caesar will get "BRUTUS" back. The decryption function is the inverse of the encryption function. When applied sequentially, they cancel each other out, restoring the original message.

# Fun Fact 🥳

While the Caesar Cipher was groundbreaking in its time, today's encryption standards are far more sophisticated. One would need more than a simple shift in the alphabet to decode modern encrypted communications. In fact, modern encryption algorithms, when used correctly, can take billions of years to crack, even with today's most advanced computers!