# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(word_list))
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

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
