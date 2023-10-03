import random

print("Welcome to the PyPassword Generator!")
total_letter = int(
    input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

# proccess

number_list = []
password_list = []

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
symbol_list = ['!', '@', '#', '$', '%', '?', '&', '*']
letter_cap_list = []
for i in letter_list:
    letter_cap_list.append(i.upper())

letter_list += letter_cap_list
# print(letter_list)

random_letter = (random.sample(letter_list, k=total_letter))
random_symbol = (random.sample(symbol_list, k=total_symbols))
random_number = (random.sample(number_list, k=total_numbers))
random_cap_letter = (random.sample(letter_cap_list, k=total_numbers))

password_list = random_letter + random_symbol + random_number
random.shuffle(password_list)
print(password_list)

# ' '.join(password_list)
# print(' '.join(password_list))
# print(number_list)
# print(letter_list)
# print(symbol_list)
# print("Here is your password: ")
