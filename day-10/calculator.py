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

number = [0, 0]
loop = True
i = 0
number[0] = int(input("What's the first number?\n"))
operation = input("Pick an operation. (\" + \", \" - \", \" * \", \" / \")\n")

if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Your input is invalid.")
else:
    while loop:
        if i > 0:
            operation = input(
                "\nPick an operation. (\" + \", \" - \", \" * \", \" / \")\n")
        number[1] = int(input("What's the next number?\n"))
        if operation == "+":
            result = add(number[0], number[1])
        elif operation == "-":
            result = sub(number[0], number[1])
        elif operation == "*":
            result = mul(number[0], number[1])
        else:
            result = div(number[0], number[1])
        print(f"\n{number[0]} {operation} {number[1]} = {result}")
        keep_loop = input(
            f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\nInput : ")
        number[0] = result
        i += 1
        if keep_loop == 'n':
            loop = False
