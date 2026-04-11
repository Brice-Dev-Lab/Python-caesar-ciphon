# **Technical Skills Survey** Project Part 2: Exercise 7 - Meeting Again with Caesar's Best Friend

# Previously on Springboard

In the heart of ancient Rome 🏛️, Julius Caesar had a secret 🤫. Not just about gladiators 🗡️ or gold 💰, but about... a party 🍾! This year, he would host a secret party only for his closest friends. This party was the talk of the town 🙊! There were magical fairies ✨, dancing peacocks 🦚, melodious harps 🎵, and sparkling fountains ⛲.

However, there was a problem 😲! Uninvited guests 🥷 would crash the party because the location 🗺️ would get leaked by spies 🕵️‍♂️.

Caesar needed a plan 💡! He thought, "I'll send out the invites encrypted 🔐. That way, only my true friends 🤝 will know when and where the party is!".

So, he came up with a cunning plan 🦊. Instead of writing the party location of the invitation directly 🏞️, he would shift each letter in by a fixed number 🔢. So, for example, if he decided to shift by 3:

- A would become D 🔄
- B would become E 🔄
- C would become F 🔄
- ... and so on.

If the invite said "GARDEN" 🌳, he would write "JDUGHQ" 🤯.

When Brutus received the letter 📜, he knew about this secret code 🗝️. He would shift the letters back by the same number and decode "JDUGHQ" to "GARDEN" 🌳. Mmm, clever 🧠!

However, any nosy Romans 👀 intercepting the message would be baffled 😶‍🌫️! "JDUGHQ? What kind of place is that?" they would wonder 🤷‍♂️.

Thanks to the "Caesar Cipher" 🔐, Caesar's secret party remained exclusive 😼, magical 🌌, and crasher-free 🥳!

And while history 📖 might tell you that Brutus wasn't the most trustworthy of friends, at least in our story, he kept the party's secret 🎉 and never gave away the magical location 🌳! 😉🤫

# Exercise 📋

You are given the below code.

```jsx
const friend = "BRUTUS"
const shiftValue = 3;
```

Your objective is to encrypt the name "BRUTUS" using the Caesar Cipher technique and loops. Remember, we did it once for "B". Now, it's time to apply all letters.

Use the following steps in a JavaScript file, placing the given code at the top. Place your answers to the questions as comments where they appear.

## Step 1 🧩

Recall the Latin alphabet variable from the previous exercise.

### Answer 🔑

```jsx
const alphabet = "abcdefghijklmnopqrstuvwxyz";
```

## Step 2 🧩

Use a loop to iterate through each letter of "BRUTUS". Employ the Caesar Cipher technique to shift each letter by the given value. Store the encrypted name in a variable.

### Hints 💡

- Use a `for` loop to traverse each letter of the name.
- Remember to handle cases where the shift might go beyond "z".

### Answer 🔑

```jsx
let encryptedName = "";

for (let i = 0; i < friend.length; i++)
{
  const currentLetter = friend[i];
  const currentIndex = alphabet.indexOf(currentLetter.toLowerCase());
  const newIndex = (currentIndex + shiftValue) % alphabet.length;
  encryptedName += alphabet[newIndex].toUpperCase();
}
```

## Question 1 🤔

What advantage does using a loop provide over manually encrypting each letter?

### Answer 🔑

Using a loop provides automation, enabling us to process each letter of the name consecutively without redundant code. It ensures consistent encryption and can easily adapt to names of any length.

## Question 2 🤔

Explain the role of `% alphabet.length` in our loop. How does it aid in the encryption process?

### Answer 🔑

The modulus operator, `%`, ensures that if the sum of the current index and the shift value surpasses the alphabet's length, it wraps around to the start. Thus, after "z", we return to "a", guaranteeing continuous encryption.

# Fun Fact 🥳

Did you know? Ancient Romans employed various means to send confidential messages, one of which was the "tessera." A tessera was a token, usually made of metal or stone, given to someone as a sign of recognition. This token could be presented to gain entry into secret meetings or events. It's fascinating to think that they had their own version of "password-protected entry" over two millennia ago! 🏛️🔐🎟️