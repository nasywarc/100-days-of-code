import random

print("Welcome to the PyPassword Generator!")
total_letter = int(
    input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

# proccess

number_list = []
password_list = []

for i in range(0, 10):
    number_list.append(i)
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
symbol_list = ['!', '@', '#', '$', '%', '?', '&', '*']

random_letter = (random.sample(letter_list, k=total_letter))
random_symbol = (random.sample(symbol_list, k=total_symbols))
random_number = (random.sample(number_list, k=total_numbers))

password_list.append(random_letter)
password_list.append(random_symbol)
password_list.append(random_number)
print(str(password_list))
# print(number_list)
# print(letter_list)
# print(symbol_list)
# print("Here is your password: ")
