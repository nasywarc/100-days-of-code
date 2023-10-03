import random

# greeting and input
print("Welcome to the PyPassword Generator!")
total_letter = int(
    input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

# making blank list
password_list = []

# making list
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
symbol_list = ['!', '@', '#', '$', '%', '?', '&', '*']
letter_cap_list = []

# making capital letter and join it  with normal letter
for i in letter_list:
    letter_cap_list.append(i.upper())
letter_list += letter_cap_list

# random module
random_letter = (random.sample(letter_list, k=total_letter))
random_symbol = (random.sample(symbol_list, k=total_symbols))
random_number = (random.sample(number_list, k=total_numbers))

# output code
password_list = random_letter + random_symbol + random_number
random.shuffle(password_list)
print(f"Here is your password: {''.join(password_list)}")
