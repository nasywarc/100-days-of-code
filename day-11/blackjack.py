import os
import art
import random


def pick_a_card():
    shuffle = random.randint(1, 12)
    card = cards[shuffle]
    return card


def play_game():
    user_first_card = computer_first_card = []
    user_first_card.append(pick_a_card())
    user_first_card.append(pick_a_card())
    print(user_first_card)
    computer_first_card.append(pick_a_card())
    computer_first_card.append(pick_a_card())
    print(computer_first_card)

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
        play_game()
    else:
        print('Your input is invalid.')
        break
    print(art.logo)
