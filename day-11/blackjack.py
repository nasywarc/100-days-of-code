import os

os.system('cls')
loop = False
play_or_no = input(
    'Do you want to play a game of Blackjack? Type \'y\' or \'n\'.\n').lower()
if play_or_no == 'y':
    loop = True
    print('Hi.')
elif play_or_no == 'n':
    exit()
else:
    print('Your input is invalid.')
