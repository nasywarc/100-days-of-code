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

number = []
loop = True
i = 1
number[0] = int(input("What's the first number?\n"))
operation = input("Pick an operation. (\" + \", \" - \", \" * \", \" / \")\n")

if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Your input is invalid.")
else:
    while loop:
        number[i] = int(input("What's the next number?\n"))
        if operation == "+":
            result = add(number[i-1], number[i])
        elif operation == "-":
            result = sub(number[i-1], number[i])
        elif operation == "*":
            result = mul(number[i-1], number[i])
        else:
            result = div(number[i-1], number[i])
        print(f"\n{number[i-1]} {operation} {number[i]} = {result}")
        keep_loop = print(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\nInput : ")
        i += 1
        number[i-1] = result
        if keep_loop == 'n':
            loop = False
