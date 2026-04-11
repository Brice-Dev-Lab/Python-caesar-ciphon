# **Technical Skills Survey Project Part 2: Exercise 2 - Meeting with Caesar's Best Friend**

# Meeting with Caesar's Best Friend

In the captivating world of ancient Rome 🏛️, Julius Caesar's life was not just about ruling the empire or conquering new lands. He had personal moments, too. One of them was the highly anticipated meeting with his best friend, Brutus. Although history has painted Brutus in various shades, in our tale, he's Caesar's trusted confidant.

Caesar decided to meet Brutus at a secret location 🗺️ to discuss matters of the heart and reminisce about old times. But, with spies 🕵️‍♂️ lurking around every corner, how could he ensure that the meeting details remained confidential?

Caesar had an ingenious plan 💡. He would use a code to communicate the meeting spot to Brutus, ensuring that only the two of them understood the message. He decided to employ the "Caesar Cipher" 🔐, a simple yet effective method of encryption.

To ensure Brutus could decode the message, Caesar gave him a hint: "Remember our childhood game, where A became D, B became E, and so on?". Brutus smiled, understanding the reference.

Now, let's dive into the mechanics of this cipher, which played a pivotal role in their secret rendezvous.

# Exercise 📋

You are given the below code.

```jsx
const friend = "BRUTUS"
const shiftValue = 3;
```

Please incorporate the following steps into a single JavaScript file, placing the provided code at the top. Insert your answers to the questions as comments where they appear.

## Step 1 🧩

Store the Latin alphabet in a variable with all letters in lowercase.

### Answer 🔑

```jsx
const alphabet = "abcdefghijklmnopqrstuvwxyz";
```

## Step 2 🧩

Find the index of the first letter of Ceaser's friend. Store it in a variable.

### Hints 💡

- Access the first letter of Ceaser's friend.
- Ceaser's friend's is given in upper-case, but the alphabet was built in lower-case. Convert the case of the first letter.
- Use a method on the alphabet to find indexes of given strings.

### Answer 🔑

```
const firstLetter = friend[0];
const index = alphabet.indexOf(firstLetter.toLowerCase());

```

## Question 1 🤔

Oh, I know B is the 2nd letter of the alphabet. Then, why the result is 1 instead of 2?

### Answer 🔑

JavaScript uses zero-based indexing, which means the first item of a string is accessed using 0.

## Step 3 🧩

Use the Caesar Cipher technique to shift the first letter of Caesar's friend by the given shift value, which is 3 positions. Find and store the encrypted letter in a variable.

### Hints 💡

- Once you find the index of the letter, add the shift value to it to find the new index.

### Answer 🔑

```
const newIndex = index + shiftValue;
const encryptedFirstLetter = alphabet[newIndex];

```

## Question 2 🤔

If we continue shifting letters and go beyond the last letter, "z", which operator could help us to wrap around and continue from the beginning of the alphabet?

### Answer 🔑

The modulus operator, `%`, helps us wrap around the alphabet. If we try to access an index beyond the length of our alphabet, the modulus operator ensures that the result wraps around starting from 0. For instance, accessing the 28th position (which doesn't exist) would give us an index of 2, corresponding to the third letter, "c". This operator ensures we always get a valid index within the bounds of the alphabet.

## Step 4 🧩

Determine the length of the alphabet.

### Hints 💡

- Use a specific property of strings in JavaScript to get their length.

### Answer 🔑

```
const alphabetLength = alphabet.length;

```

## Step 5 🧩

Use the Caesar Cipher technique to shift the first letter of Caesar's friend by the given shift value, ensuring the shift wraps around the alphabet if it exceeds.

### Hints 💡

- Use the modulus operator to handle wrapping around the alphabet based on its length.

### Answer 🔑

```
const alphabetLength = alphabet.length;
const newIndex = (index + shiftValue) % alphabetLength;
const encryptedFirstLetter = alphabet[newIndex];

```

## Step 6 🧩

Caesar remembers that Brutus is particularly fond of challenges. Before sending the encrypted message, Caesar decides to send only a part of it as a teaser. Extract the first 3 characters from the encrypted message using the `slice` method. (Assume that the encrypted message is "EUXWXV".)

### Hints 💡

- The `slice` method extracts a section of a string and returns it as a new string without modifying the original string.
- It accepts two parameters: the starting index (inclusive) and the ending index (exclusive).

### Answer 🔑

```
const encryptedMessage = "EUXWXV";
const teaserMessage = encryptedMessage.slice(0, 3);

```

# Fun Fact 🥳

The Caesar Cipher, while historically significant, is easily cracked in today's digital age. If you delve deeper into the world of cryptography, you'll encounter more advanced encryption techniques that are used to secure data in modern times.