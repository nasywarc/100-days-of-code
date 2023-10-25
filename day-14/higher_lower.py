import art
import os
from game_data import data
import random


def pick_the_artist():
    index_pick = random.randint(0, 24)
    # artist_choice = data[index_pick]
    # return artist_choice
    return index_pick


os.system('cls')
print(art.logo)

first_artist = pick_the_artist()
second_artist = pick_the_artist()
print(
    f'Compare A: {data[first_artist]["artist"]}, a {data[first_artist]["occupation"]}, from {data[first_artist]["born"]}.')
print(art.vs)
print(
    f'Against B: {data[second_artist]["artist"]}, a {data[second_artist]["occupation"]}, from {data[second_artist]["born"]}.')

input('\nWho has more followers? Type \'A\' or \'B\'.\nInput -> ')

# if right => You're right! Current score: {score}.
# if wrong => Sorry, that's wrong. Final score: {score}.
