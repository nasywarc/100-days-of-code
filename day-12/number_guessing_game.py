import random
import art
import os

attempts = 10
random_int = random.randint(1, 100)
play = True


def hard():
    return attempts - 5


os.system('cls')
print(art.logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
level_choice = input(
    'Choose a difficulty. Type \'easy\' or \'hard\'.\nInput -> ')

if level_choice == 'hard':
    attempts = hard()
elif level_choice != 'easy':
    print('Your input is invalid.')
    exit()

while play:
    print(f'\nYou have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess : '))
    if random_int == guess:
        print(f'\nYou got it! The answer was {random_int}.')
        play = False
    elif random_int > guess:
        print('Too low.\nGuess again.')
        attempts -= 1
    elif attempts == 0:
        print('\nYou\'ve run out of guesses, you lose.')
        play = False
    else:
        print('Too high.\nGuess again.')
        attempts -= 1
