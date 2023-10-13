import os
import art


def user_input():
    name = input("What is your name?\t: ")
    bid = int(input("What's your bid?\t: $"))
    bidders['name'].append(name)
    bidders['bid'].append(bid)


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
        loop = False

os.system('cls')
max_bid = max(bidders['bid'])
winner_index = bidders['bid'].index(max_bid)
print(
    f"The winner is {bidders['name'][winner_index]} with a bid of ${bidders['bid'][winner_index]}.")
