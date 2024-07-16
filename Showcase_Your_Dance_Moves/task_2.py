# Ask the user how they feel today
mood = input("How do you feel today? ")

# Evaluate the user's mood
if mood() == "happy":
    print("That's great to hear!")
elif mood() == "sad":
    print("I hope your day gets better!")

