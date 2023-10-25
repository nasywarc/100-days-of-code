import art
import os
from game_data import data
import random


def pick_the_artist():
    index_pick = random.randint(0, 24)
    return index_pick


def right():
    return score + 1


def wrong():
    pass


def header():
    os.system('cls')
    print(art.logo)


header()

first_artist = pick_the_artist()
second_artist = pick_the_artist()
play = True
score = 0

while play:
    print(
        f'Compare A: {data[first_artist]["artist"]}, a {data[first_artist]["occupation"]}, from {data[first_artist]["born"]}.')
    print(art.vs)
    print(
        f'Against B: {data[second_artist]["artist"]}, a {data[second_artist]["occupation"]}, from {data[second_artist]["born"]}.')

    user_answer = input(
        '\nWho has more followers? Type \'A\' or \'B\'.\nInput -> ').lower()
    if user_answer != 'a' and user_answer != 'b':
        print('Your input is invalid.')
        exit()

    if data[first_artist]['followers'] > data[second_artist]['followers']:
        if user_answer == 'a':
            header()
            score += 1
            print(f'You\'re right! Current score: {score}.')
            first_artist = second_artist
            second_artist = pick_the_artist()
        else:
            header()
            print(f'Sorry, that\'s wrong. Final score: {score}.\n')
            play = False
    else:
        if user_answer == 'b':
            header()
            score += 1
            print(f'You\'re right! Current score: {score}.')
            first_artist = second_artist
            second_artist = pick_the_artist()
        else:
            header()
            print(f'Sorry, that\'s wrong. Final score: {score}.\n')
            play = False
