import art
import os


def add(first, sec):
    result = first + sec
    return result


os.system('cls')
print(art.logo)

first_num = int(input("What's the first number?\n"))
operation = input("Pick an operation. (\" + \", \" - \", \" * \", \" / \")\n")
second_num = int(input("What's the next number?\n"))
if operation == "+":
    print(f"{first_num} {operation} {second_num} = {add(first_num, second_num)}")
elif operation == "-":
    print(f"{first_num} {operation} {second_num} = {add(first_num, second_num)}")
elif operation == "*":
    print(f"{first_num} {operation} {second_num} = {add(first_num, second_num)}")
elif operation == "/":
    print(f"{first_num} {operation} {second_num} = {add(first_num, second_num)}")
