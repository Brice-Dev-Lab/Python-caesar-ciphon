# **Technical Skills Survey Project Part 2: Exercise 5 - Caesar's Party Guest List**

# Caesar's Party Guest List

Following the success of his secret party, Julius Caesar decided to make it an annual event 🎉. Every year, a grand party would be held in a mysterious location, and Caesar needed to keep track of his guests 🤔.

This year, he wanted to use the Caesar Cipher again 🔐, but he had so many guests that he decided to use arrays to keep everything organized 📦. His scribe provided him with a list of names 📜, but Caesar realized he could use some of the array methods he had been studying to ensure the list was perfect 🧐.

# Exercise 📋

Given the initial array of guests:

```jsx
const guests = ["ANTONY", "CICERO", "CASSIUS", "CLEOPATRA"];
```

Follow the steps below and write your answers. Remember to place your responses as comments where they appear in the exercise.

## Step 1 🧩

Caesar remembers he forgot to add his best friend "BRUTUS" to the list. Add him to the beginning of the list.

### Hint 💡

- There's a method to add elements to the beginning of an array.

### Answer 🔑

```
guests.unshift("BRUTUS");

```

## Question 1 🤔

How can you verify that "BRUTUS" was added to the beginning of the array?

### Answer 🔑

You can check the first element of the `guests` array using `guests[0]`.

## Step 2 🧩

A herald announced the arrival of "AUGUSTUS" and "LUCIA". Add them to the end of the guest list.

### Hint 💡

- There's a method to add elements to the end of an array.

### Answer 🔑

```
guests.push("AUGUSTUS", "LUCIA");

```

## Step 3 🧩

Caesar is curious. He wants to know if "SPARTACUS" has been invited. Check if he's on the list and find out at which position.

### Hint 💡

- Use the right method to find a specific name in the list and its position.

### Answer 🔑

```
const spartacusIndex = guests.indexOf("SPARTACUS");

```

## Question 2 🤔

What would the value of `spartacusIndex` be if "SPARTACUS" wasn't invited?

### Answer 🔑

If "SPARTACUS" wasn't invited, the `indexOf` method would return `-1`.

## Step 4 🧩

Oops! Caesar just received a message that "CASSIUS" won't be able to make it. Remove him from the list.

### Hint 💡

Find the index of the guest and use the appropriate method to remove him from the list.

### Answer 🔑

```jsx
const indexToRemove = guests.indexOf("CASSIUS");
guests.splice(indexToRemove, 1);

```

## Step 5 🧩

Caesar wants to send a special invite to the first three guests on the list. Extract these names into a new array.

### Hint 💡

- Use the appropriate method to get a portion of the array.

### Answer 🔑

```jsx
const specialGuests = guests.slice(0, 3);

```

## Step 6 🧩

Caesar decides he wants the guest list in alphabetical order. Sort the array. However, Caesar wants his most honored guest (the one added first) to remain at the top of the list. Can you think of a way to sort the guests but keep the honored ones at the top?

### Answer 🔑

```jsx
const honoredGuests = guests.slice(0, 1); // Extracts honored guests.
const otherGuests = guests.slice(1); // Extracts the rest of the guests.
otherGuests.sort(); // Sorts the other guests.
const sortedGuests = honoredGuests.concat(otherGuests); // Combines both arrays. 
```

# Fun Fact 🥳

While we use digital tools and programming languages like JavaScript today to manage and manipulate lists, ancient Romans used wax tablets and styluses for lists, note-taking, and other everyday writing tasks. These tablets consisted of a wooden frame filled with wax. Users would write on the wax surface and could easily "erase" by smoothing out the wax. Imagine Caesar managing his guest list on one of those! 📜🕯️