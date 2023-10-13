import os
import art


def user_input():
    name = input("What is your name?\t: ")
    bid = int(input("What's your bid?\t: $"))


bidders = {'name': [],
           'bid': []}

loop = True

os.system('cls')
print(art.logo)
print("Welcome to the secret auction program.")

while loop:
    user_input()
    keep_loop = input("Are there any other bidders? Type \"Yes\" or \"No\".\n")
    if keep_loop == 'yes' or keep_loop == 'Yes':
        keep_loop = True
        os.system('cls')
    else:
        keep_loop = False
