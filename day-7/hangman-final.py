import random  # untuk menggunakan random func
import hangman_art  # untuk mengambil var logo dan var stages
import hangman_words  # untuk mengambil var word_list
import os  # untuk mengakses file kita, dalam ini clear screen

print(hangman_art.logo)

chosen_word = list(random.choice(hangman_words.word_list))
print(f"Hint : {''.join(chosen_word)}")

display = []
for letter in chosen_word:
    display.append("_")

life = 6
guess_list = []

while display != chosen_word and life > 0:
    guess = input("\nGuess a letter : ").lower()
    os.system('cls')  # fungsi untuk clear screen
    if guess in guess_list:
        print(f"\nYou've already guessed {guess}")

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = (guess)
                guess_list.append(guess)

    else:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"{' '.join(display)}")
    print(hangman_art.stages[life])

if life > 0:
    print("\nCongrats, You WIN!")
else:
    print(f"The answer is \"{''.join(chosen_word)}\"")
    print("\nYou lose, Game Over.")
