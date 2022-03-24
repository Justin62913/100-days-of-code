# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]  # List of words
chosen_word = random.choice(word_list)  # The word the player needs to guess

# Testing code
print(f'Pssst, the solution is {chosen_word}.')  # Testing Code

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.

display = []  # An empty list to store user guesses
hint_list = ["_"] * len(chosen_word)  # Replaces the characters in a string with "_"

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

while "".join(hint_list) != chosen_word:  # Loops until the game is complete
    guess = input("Guess a letter: ").lower()  # prompts player to enter a guess

    display.append(guess)  # stores players guess in a list (display)

    found_indices = [i for i, x in enumerate(chosen_word) if x == guess]  # finds the index occurance of the users guess

    for i in found_indices:  # Replaces the "_" with the users guess
        hint_list[i] = guess

    print(f"All guesses so far: {display}")
    print(f"Current hint list: {hint_list}")

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(f"\n You did it! The word is {chosen_word}")
