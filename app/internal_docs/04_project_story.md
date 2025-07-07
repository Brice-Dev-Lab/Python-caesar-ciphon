# **Technical Skills Survey Project Part 2: Exercise 4 - The Secret Emblem** of Caesar's Invitation

# The Secret Emblem of Caesar's Invitation

The secret party of Julius Caesar 🎭 is right around the corner 🗓️. As you know, Caesar has decided to use a secret emblem 🌌 on his invitations to hide the secret shift value of the Caesar Cipher 🔐. Each emblem corresponds to a specific location in Rome for the party 🏛️.

However, to add an extra layer of secrecy 🤫, the emblem isn't just a single image or symbol 🧩. It consists of a series of clues 🕵️‍♂️, and only those who can decipher them all will find the party's location 🕵️‍♀️.

Your task is to write a program 🖥️ that will decipher the emblem and reveal the party's location 🎉.

# Exercise 📋

You are given the below code:

```jsx
const emblemClue1 = "Eagle";
const emblemClue2 = "Laurel";
const emblemClue3 = 7;

```

Use the knowledge you've gained on program logic and flow to perform the following steps. Add your answers to the questions as comments where they appear.

## Step 1 🧩

Use a series of `if`, `else if`, and `else` statements to decipher the first clue.

- If `emblemClue1` is "Eagle", the location starts with "Forum".
- If `emblemClue1` is "Lion", the location starts with "Colosseum".
- Otherwise, the location starts with "Villa".

### Answer 🔑

```jsx
let locationStart = "";

if (emblemClue1 === "Eagle")
{
  locationStart = "Forum";
}
else if (emblemClue1 === "Lion")
{
  locationStart = "Colosseum";
}
else
{
  locationStart = "Villa";
}

```

## Step 2 🧩

Use boolean logic to decipher the second clue.

- If `emblemClue2` is "Laurel" AND the first location is "Forum", append " of Augustus" to the location.
- If `emblemClue2` is "Grapes" OR the first location is "Villa", append " of Pompey" to the location.

### Answer 🔑

```jsx
if (emblemClue2 === "Laurel" && locationStart === "Forum")
{
  locationStart += " of Augustus";
}
else if (emblemClue2 === "Grapes" || locationStart === "Villa")
{
  locationStart += " of Pompey";
}

```

## Step 3 🧩

Use the switch statement to decipher the third clue.

- Depending on the value of `emblemClue3`, append a direction to the location.
    - 7 is "North"
    - 3 is "South"
    - 9 is "East"
    - 4 is "West"

### Answer 🔑

```jsx
switch (emblemClue3)
{
  case 7:
    locationStart += " North";
    break;
  case 3:
    locationStart += " South";
    break;
  case 9:
    locationStart += " East";
    break;
  case 4:
    locationStart += " West";
    break;
}

```

## Question 🤔

Why is it important to be careful when using `==` (double equals) instead of `===` (triple equals) in our conditionals?

### Answer 🔑

Using `==` (double equals) performs type coercion, meaning it tries to convert the operands to the same type before making the comparison. On the other hand, `===` (triple equals) checks both the value and the type, ensuring a stricter equality check. Using `==` can lead to unexpected results in certain situations due to type coercion.

# Fun Fact 🥳

In ancient Rome, the use of cryptography wasn't just limited to Julius Caesar. The Romans were known to use other simple substitution ciphers and codes, especially in the military. One popular method was the "Scytale" where a strip of leather or parchment was wound around a rod of a specific diameter, and then a message was written down the rod's length. When unwound, the message appeared as a jumbled set of characters, but when wound around a rod of the correct diameter, the original message would appear. This early form of transposition cipher showcases how creative the ancient civilizations were when it came to keeping their secrets safe! 🏺🔍