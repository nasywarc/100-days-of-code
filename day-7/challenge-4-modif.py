# Step 2 mix 3 mix 4

import random
word_list = ["kucing", "anjing", "semut", "singa", "harimau",
             "hamster", "burung", "tikus", "gajah", "jerapah",
             "angsa", "ikan", "rusa", "macan", "ular", "siput",
             "sapi", "kambing", "domba", "kelelawar", "kuda",
             "hiu", "paus", "buaya", "serigala", "marmut", "ulat",
             "bebek", "itik", "rubah", "monyet", "babi", "orangutan"]

chosen_word = list(random.choice(word_list))
print(chosen_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(
    '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
)

display = []
for letter in chosen_word:
    display.append("_")

life = 6
guess_list = []

while display != chosen_word and life > 0:
    guess = input("\nGuess a letter : ").lower()
    if guess in guess_list:
        print("\nYou've already guess that letter.")

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = (guess)
                guess_list.append(guess)
        print(f"{' '.join(display)}")

    else:
        life -= 1
        print(f"{' '.join(display)}")
        print(stages[life])

if life > 0:
    print("\nCongrats, You WIN!")
else:
    print(f"The answer is \"{' '.join(chosen_word)}\"")
    print("\nYou lose, Game Over.")
