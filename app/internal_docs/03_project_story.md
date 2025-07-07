# **Technical Skills Survey Project Part 2: Exercise 3 - Creating a Secret Shift Value for Caesar**

# Creating a Secret Shift Value for Caesar

Amidst the bustling streets of ancient Rome 🏛️, Julius Caesar heard of a new method to improve his secret cipher. The fixed shift was too predictable! "What if," he pondered, "the shift value itself was a secret, and it changed every time? 🤔"

He decided that every invite to his secret party 🍾 would not only be encrypted but would also use a random shift value between 3 and 33. This would make the cipher even more mysterious and harder to crack!

However, the challenge was ensuring that both the sender (Caesar) and the receiver (his trusted friends) knew this secret shift value. He decided to hide the shift value in a secret emblem 🌌 on the invitation. Only those who knew where to look could find it and decrypt the message.

Intrigued by this new method, Brutus eagerly awaited his invitation to see if he could uncover the secret shift value and decode Caesar's message.

# Exercise 📋

Follow the steps below and write your answers. Place your responses as comments where they appear in the exercise.

## Step 1 🧩

Generate a decimal number between 0 (inclusive) and 1 (exclusive) using JavaScript's `Math` functions.

### Answer 🔑

```jsx
const randomDecimal = Math.random();
const range = 33 - 3 + 1; // 31
const randomInRange = randomDecimal * range; // Adjusts the range to get a number between 0 (inclusive) and the value of 'range' (exclusive).
const randomInt = Math.floor(randomInRange); // Convert the decimal number to an integer to get values between 0 and (range - 1).
const shiftValue = randomInt + 3; // Shift the range to get an integer between 3 and 33
```

## Step 2 🧩

Determine the desired range of numbers for our secret shift value, which is between 3 and 33.

### Answer 🔑

```jsx
const range = 33 - 3 + 1; // 31
```

## Question 1 🤔

Why did we add 1 to the difference between 33 and 3?

### Answer 🔑

We added 1 to ensure we include both endpoints of our range, 3 and 33, so we have a total of 31 possible numbers (from 3 to 33 inclusive).

## Step 3 🧩

Using the random decimal number generated in Step 1, adjust its value to fit within the desired range determined in Step 2.

### Answer 🔑

```jsx
const randomInRange = randomDecimal * range;
```

## Question 2 🤔

How does multiplying `randomDecimal` by `range` help us get a number within our desired range?

### Answer 🔑

Multiplying the `randomDecimal` (which is between 0 and 1) by the `range` scales the decimal to fall within the range of 0 to `range`. This means we'll get a decimal number that's between 0 (inclusive) and the value of `range` (exclusive), thus fitting it within our desired range.

## Step 4 🧩

Round down the decimal number obtained in Step 3 to get a whole integer.

### Answer 🔑

```jsx
const randomInt = Math.floor(randomInRange);
```

## Question 3 🤔

Why do we use the `Math.floor()` function instead of other rounding methods like `Math.round()`?

### Answer 🔑

We use `Math.floor()` to ensure we always round down to the nearest whole number, giving us an integer between 0 and `range - 1`. Using `Math.round()` could potentially round up, causing us to exceed our desired range.

## Step 5 🧩

Adjust the integer obtained in Step 4 to fit within the range of 3 to 33, inclusive.

### Answer 🔑

```jsx
const shiftValue = randomInt + 3;
```

## Question 4 🤔

How does adding 3 to `randomInt` ensure that our final `shiftValue` is between 3 and 33?

### Answer 🔑

Since `randomInt` is a number between 0 and `range - 1` (which is 30 in this case), adding 3 shifts this range upward, resulting in numbers between 3 and 33 inclusive.

# Fun Fact 🥳

A random shift adds a layer of complexity, but it's still not super secure by today's standards.