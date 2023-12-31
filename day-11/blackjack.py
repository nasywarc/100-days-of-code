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
    computer_first_card.append(pick_a_card())
    computer_first_card.append(pick_a_card())
    user_score = computer_score = 0

    for score in user_first_card:
        user_score += score

    for score in computer_first_card:
        computer_score += score

    print(f'Your cards : {user_first_card}, current score : {user_score}')
    print(f'Computer first card : {computer_first_card[0]}')

    while play:

        if user_score < 21:
            user_choice = input(
                '\nType \'y\' to get another card or \'n\' to pass.\nInput -> ').lower()
            if user_choice == 'y':
                user_first_card.append(pick_a_card())
                user_score += user_first_card[len(user_first_card)-1]

        if user_score > 21:
            play = False
            print(
                f'\nYour final hand : {user_first_card}, current score : {user_score}')
            print(
                f'Computer\'s final hand : {computer_first_card}, current score : {computer_score}\n')
            print('You lose. BUST. 😭\n')
            break

        if computer_score < 21:
            computer_choice = random.randint(0, 1)
            if computer_choice == 1:
                computer_first_card.append(pick_a_card())
                computer_score += computer_first_card[len(
                    computer_first_card)-1]

        print(f'Your cards : {user_first_card}, current score : {user_score}')
        print(f'Computer first card : {computer_first_card[0]}')

        if user_score > 21 or computer_score == 21:
            play = False
            print(
                f'\nYour final hand : {user_first_card}, current score : {user_score}')
            print(
                f'Computer\'s final hand : {computer_first_card}, current score : {computer_score}\n')
            print('You lose. 😭\n')
        elif computer_score > 21 or user_score == 21:
            play = False
            print(
                f'\nYour final hand : {user_first_card}, current score : {user_score}')
            print(
                f'Computer\'s final hand : {computer_first_card}, current score : {computer_score}\n')
            print('You win. 😎\n')


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
