import os
import art
import random


def pick_a_card():
    shuffle = random.randint(0, 12)
    card = cards[shuffle]
    return card


def play_game():
    play = True
    user_first_card = []
    computer_first_card = []

    user_first_card.append(pick_a_card())
    user_first_card.append(pick_a_card())
    print(f'ini user{user_first_card}')
    computer_first_card.append(pick_a_card())
    computer_first_card.append(pick_a_card())
    print(f'ini user lagi{user_first_card}')
    print(f'ini computer{computer_first_card}\n\n')
    user_score = computer_score = 0

    for score in user_first_card:
        user_score += score

    for score in computer_first_card:
        computer_score += score

    while play:

        print(
            f'Your cards : {user_first_card}, current score : {user_score}')
        print(f'Computer first card : {computer_first_card[0]}')

        if user_score < 21:
            user_choice = input(
                'Type \'y\' to get another card or \'n\' to pass.\nInput -> ').lower()
            if user_choice == 'y':
                user_first_card.append(pick_a_card())
                user_score += user_score[len(user_score)-1]

        if computer_score < 21:
            computer_choice = random.randint(0, 1)
            if computer_choice == 1:
                computer_first_card.append(pick_a_card())

        if user_score > 21:
            play = False
            print('You lose.\n')
        elif computer_score > 21:
            play = False
            print('You win.\n')


os.system('cls')
loop = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while loop:
    play_or_no = input(
        'Do you want to play a game of Blackjack? Type \'y\' or \'n\'.\nInput -> ').lower()
    if play_or_no == 'n':
        break
    elif play_or_no == 'y':
        os.system('cls')
        print(art.logo)
        play_game()
    else:
        print('Your input is invalid.')
        break
