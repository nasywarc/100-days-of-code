import os
import art
import random


def pick_a_card():
    shuffle = random.randint(1, 12)
    card = cards[shuffle]
    return card


def play_game():
    play = True
    user_first_card = computer_first_card = []
    user_first_card.append(pick_a_card())
    user_first_card.append(pick_a_card())
    user_score = computer_score = 0

    while play:

        for score in user_first_card:
            user_score += score

        print(f'Your cards : {user_first_card}, current score : {user_score}')

        computer_first_card.append(pick_a_card())
        computer_first_card.append(pick_a_card())

        print(f'Computer first card : {computer_first_card[0]}')
        for score in computer_first_card:
            computer_score += score

        if user_score < 21:
            user_choice = input(
                'Type \'y\' to get another card or \'n\' to pass.\nInput -> ').lower()
            if user_choice == 'y':
                user_first_card.append(pick_a_card())

        if computer_score < 21:
            computer_choice = random.randint(0, 1)
            if computer_choice == 1:
                computer_first_card.append(pick_a_card())

        if user_choice >= 21:
            play = False
            print('You lose.')
        elif computer_choice >= 21:
            play = False
            print('You win.')


# def take_or_no(first_num, sec_num):
#     while first_num + sec_num < 21:
#         computer_choice = random.randint(0, 1)
#         if computer_choice == 1:
#             play_game()[1].append(pick_a_card())
#         choice = input(
#             'Type \'y\' to get another card or \'n\' to pass.\nInput -> ').lower()
#         if choice == 'y':
#             play_game()[0].append(pick_a_card())

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
