# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(word_list))

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")
# guess = input("Guess a letter : ").lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# for position in range(len(chosen_word)):
#     if guess == chosen_word[position]:
#         display[position] = (guess)
    # else:
    #     display[position] = ["_"]

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)

life = 11
while display != chosen_word and life > 0:
    guess = input("Guess a letter : ").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = (guess)
    else:
        life -= 1
        print(f"Your life is : {life}")

    print(display)

if life > 0:
    print("\nYou WIN!")
else:
    print("\nGame Over.")

# print(type(display))
# print(type(chosen_word))
