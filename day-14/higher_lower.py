import art
import os
from game_data import data
import random


def pick_the_artist():
    # index_pick = random.randint(0, 24)
    index_pick = random.randint(0, 24)
    artist_choice = data[index_pick]['artist']
    print(artist_choice)


os.system('cls')
print(art.logo)

print('Compare A: Dwayne Johnson, a Actor and professional wrestler, from United States.')
print(art.vs)
print('Against B: FC Barcelona, a Football club, from Spain.')

print(len(data))
pick_the_artist()
# input('\nWho has more followers? Type \'A\' or \'B\'.\nInput -> ')

# if right => You're right! Current score: {score}.
# if wrong => Sorry, that's wrong. Final score: {score}.
