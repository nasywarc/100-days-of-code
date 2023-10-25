import os
import art
import random
from game_data import data


def pick_the_artist():
    index_pick = random.randint(0, 49)
    return index_pick


def header():
    os.system('cls')
    print(art.logo)


def right():
    global score
    header()
    score += 1
    print(f'You\'re right! Current score: {score}.')


def wrong():
    global play
    header()
    print(f'Sorry, that\'s wrong. Final score: {score}.\n')
    play = False


header()
first_artist = pick_the_artist()
second_artist = pick_the_artist()
play = True
score = 0

while play:
    print(
        f'Compare A: {data[first_artist]["name"]}, a {data[first_artist]["description"]}, from {data[first_artist]["country"]}.')
    print(art.vs)
    print(
        f'Against B: {data[second_artist]["name"]}, a {data[second_artist]["description"]}, from {data[second_artist]["country"]}.')

    user_answer = input(
        '\nWho has more followers? Type \'A\' or \'B\'.\nInput -> ').lower()

    if user_answer != 'a' and user_answer != 'b':
        header()
        print('Your input is invalid.\n')
        exit()

    if data[first_artist]['follower_count'] > data[second_artist]['follower_count']:
        if user_answer == 'a':
            first_artist = second_artist
            second_artist = pick_the_artist()
            right()
        else:
            wrong()
    else:
        if user_answer == 'b':
            first_artist = second_artist
            second_artist = pick_the_artist()
            right()
        else:
            wrong()
