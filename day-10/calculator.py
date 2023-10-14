import art
import os


def add(first, sec):
    result = first + sec
    return result


def sub(first, sec):
    result = first - sec
    return result


def mul(first, sec):
    result = first * sec
    return result


def div(first, sec):
    result = first / sec
    return result


os.system('cls')
print(art.logo)

first_num = int(input("What's the first number?\n"))
operation = input("Pick an operation. (\" + \", \" - \", \" * \", \" / \")\n")
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Your input is invalid.")
else:
    second_num = int(input("What's the next number?\n"))
    if operation == "+":
        print(f"{first_num} {operation} {second_num} = {add(first_num, second_num)}")
    elif operation == "-":
        print(f"{first_num} {operation} {second_num} = {sub(first_num, second_num)}")
    elif operation == "*":
        print(f"{first_num} {operation} {second_num} = {mul(first_num, second_num)}")
    elif operation == "/":
        print(f"{first_num} {operation} {second_num} = {div(first_num, second_num)}")
