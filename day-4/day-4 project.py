import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

user__choice = input('''
==============================
=  ROCK PAPER SCISSORS GAME  =
==============================
What do you choose?
Type \"0\" for Rock
Type \"1\" for Paper
Type \"2\" for Scissors
Input : '''
                     )

chances = ["rock", "paper", "scissors"]
computer__choice = (random.sample(chances, k=1))

print("\nYou chose :")
if user__choice == '0':
    user__choice = 'rock'
    print(rock)
if user__choice == '1':
    user__choice = 'paper'
    print(paper)
if user__choice == '2':
    user__choice = 'scissors'
    print(scissors)

print("Computer chose : ")
if computer__choice == ['rock']:
    computer__choice = 'rock'
    print(rock)
if computer__choice == ['paper']:
    computer__choice = 'paper'
    print(paper)
if computer__choice == ['scissors']:
    computer__choice = 'scissors'
    print(scissors)

result = (user__choice + '_' + computer__choice)

user_win = ['rock_scissors', 'paper_rock', 'scissors_paper']
user_lose = ['rock_paper', 'paper_scissors', 'scissors_rock']
draw = ['rock_rock', 'paper_paper', 'scissors_scissors']

probability = [user_win, user_lose, draw]

if result == probability[0][0] or result == probability[0][1] or result == probability[0][2]:
    print('\nYou WIN!')

if result == probability[1][0] or result == probability[1][1] or result == probability[1][2]:
    print('\nYou Lose.')

if result == probability[2][0] or result == probability[2][1] or result == probability[2][2]:
    print('Draw.')

print('==============================')
