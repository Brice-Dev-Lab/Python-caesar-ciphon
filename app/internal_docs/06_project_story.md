# **Technical Skills Survey** Project Part 2: Exercise 6 - Caesar's VIP Guest Directory

# Caesar's VIP Guest Directory

As Caesar's annual party 🎉 grew in prominence, attendees included dignitaries and VIPs from various regions. To manage this extensive list and maintain the event's exclusivity, Caesar needed a more sophisticated system.

He contemplated using objects 📦 in JavaScript, as they allowed him to store detailed profiles of each guest, including their titles, regions, dietary preferences, and the gifts they'd bestowed upon him.

However, as with any VIP list, there were occasional changes. Some dignitaries fell out of favor and had to be discreetly removed from the list.

# Exercise 📋

Start with this initial guest directory:

```jsx
const guests = {
  ANTONY: {
    title: "General",
    region: "Rome",
    dietaryPreference: "Vegetarian",
    pastGifts: ["Golden Laurel", "Chariot"]
  },
  CICERO: {
    title: "Orator",
    region: "Arpinum",
    dietaryPreference: "Omnivore",
    pastGifts: ["Scroll of Proverbs", "Quill"]
  }
};

```

Follow the steps below and write your answers. Remember to place your responses as comments where they appear in the exercise.

## Step 1 🧩

Add "BRUTUS" to the guest directory. He's a "Senator" from "Rome", prefers "Vegan" food, and in the past, he has gifted Caesar a "Silver Dagger" and a "Marble Bust".

### Answer 🔑

```jsx
guests.BRUTUS = {
  title: "Senator",
  region: "Rome",
  dietaryPreference: "Vegan",
  pastGifts: ["Silver Dagger", "Marble Bust"]
};

```

## Step 2 🧩

Update CICERO's past gifts to include a "Golden Lyre".

### Answer 🔑

```jsx
guests.CICERO.pastGifts.push("Golden Lyre");

```

## Step 3 🧩

Retrieve the region of "ANTONY".

### Answer 🔑

```jsx
const antonyRegion = guests.ANTONY.region;
```

## Step 4 🧩

Due to unforeseen political events, "CICERO" needs to be discreetly removed from the guest list.

### Hint 💡

- Use the `delete` keyword to remove properties from an object.

### Answer 🔑

```
delete guests.CICERO;
```

## Step 5 🧩

Assign ANTONY's profile to a new variable named `generalProfile`. Then, using this new variable, change the `region` of ANTONY to "Egypt".

### Answer 🔑

```jsx
const generalProfile = guests.ANTONY;
generalProfile.region = "Egypt";
```

## Question 1 🤔

After executing Step 5, what will be the region of ANTONY in the original `guests` object?

### Answer 🔑

The region of ANTONY in the original `guests` object will be "Egypt". This is because objects in JavaScript are reference types. When we assign the object to a new variable, we're not creating a new copy of the object. Instead, both variables point to the same object in memory. Thus, changes made through one variable are reflected in the other.

# Fun Fact 🥳

The act of deleting or discreetly removing names from public records and inscriptions in ancient Rome was known as "Damnatio memoriae" (condemnation of memory). It was a form of dishonor that could be passed by the Roman Senate on traitors or those who brought discredit to Rome. Their statues might be destroyed, their names obliterated from inscriptions, and even their faces chiseled off from mosaics. In our modern times, while we simply use a `delete` keyword in programming, in ancient Rome, it was a much more laborious and symbolic act! 🗿🔨