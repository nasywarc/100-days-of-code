import random  # untuk menggunakan random func
import hangman_art  # untuk mengambil var logo dan var stages
import hangman_words  # untuk mengambil var word_list
import os  # untuk mengakses file kita, dalam ini clear screen

# menghapus semua tulisan agar layar bersih saat program dijalankan
os.system('cls')

print(hangman_art.logo)
user_choice = int(input("1. Animal\n2. Fruit\n3. Snack\nChoose game theme : "))
theme = ['Animal', 'Fruit', 'Snack']
print(f"Theme : {theme[user_choice-1]}")

chosen_word = list(random.choice(
    hangman_words.my_word_list[user_choice-1][0]))  # memilih tema game
display = []
for letter in chosen_word:
    display.append("_")

life = 6
guess_list = []
os.system('cls')
# print(f"Hint : {''.join(chosen_word)}")  # testing code
print(hangman_art.logo)
while display != chosen_word and life > 0:
    print(f"Theme : {theme[user_choice-1]}")
    guess = input("\nGuess a letter : ").lower()
    os.system('cls')  # fungsi untuk clear screen
    print(hangman_art.logo)
    print(f"Theme : {theme[user_choice-1]}\n")

    if guess in guess_list:
        print(f"You've already guessed {guess}")

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = (guess)
                guess_list.append(guess)

    else:
        life -= 1
        guess_list.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"{' '.join(display)}")
    print(hangman_art.stages[life])

if life > 0:
    print("\nYou WIN!")
else:
    print(
        f"You lose. The word you couldn't cope with was \"{''.join(chosen_word)}\".")
