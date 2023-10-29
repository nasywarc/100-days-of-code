import os
from coffee_machine import MENU, resources


def insert_coin(price, coffee, emote):
    print('Please insert coins.')
    quarters = float(input('Quarters: '))
    dimes = float(input('Dimes\t: '))
    nickles = float(input('Nickles\t: '))
    pennies = float(input('Pennies\t: '))
    total = (0.25 * quarters) + (0.1 * dimes) + \
        (0.05 * nickles) + (0.01 * pennies)
    if total > price:
        print(f'\nHere is ${round(total-price, 2)} in change.')
        print(f'\nHere is your {coffee} {emote}\nEnjoy!\n')
        return True
    elif total < price:
        print('\nSorry that\'s not enough money. Money refunded.\n')
        return False
    else:
        print(f'\nHere is your {coffee} {emote}\nEnjoy!\n')
        return True


def money_count(coffee):
    global money_earned
    money_earned += MENU[f'{coffee}']['cost']


def report():
    print(f'Water\t: {water_stock}ml')
    print(f'Milk\t: {milk_stock}ml')
    print(f'Coffee\t: {coffee_stock}g')
    print(f'Money\t: ${money_earned}\n')


def checking_stock(coffee):
    if water_stock - MENU[f'{coffee}']['ingredients']['water'] >= 0:
        if coffee != 'espresso':
            if milk_stock - MENU[f'{coffee}']['ingredients']['milk'] >= 0:
                if coffee_stock - MENU[f'{coffee}']['ingredients']['coffee'] >= 0:
                    return 'ready'
                else:
                    return 'coffee'
            else:
                return 'milk'
        else:
            if coffee_stock - MENU[f'{coffee}']['ingredients']['coffee'] >= 0:
                return 'ready'
    else:
        return 'water'


def charge_stock(coffee):
    global water_stock, milk_stock, coffee_stock
    check_stock = True

    water_stock -= MENU[f'{coffee}']['ingredients']['water']
    if coffee != 'espresso' and check_stock:
        milk_stock -= MENU[f'{coffee}']['ingredients']['milk']
    if check_stock:
        coffee_stock -= MENU[f'{coffee}']['ingredients']['coffee']

    return check_stock


def step(choice):
    if checking_stock(choice) == 'ready':
        if insert_coin(price, user_choice, emote):
            charge_stock(choice)
            money_count(choice)
    else:
        print(f'Sorry there is not enough {checking_stock(choice)}.\n')


money_earned = 0
program = True
water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']
os.system('cls')

while program:
    user_choice = input(
        'What would you like? (espresso/latte/cappuccino) : ')

    if user_choice == 'espresso':
        emote = '☕'
        price = MENU['espresso']['cost']
        step(user_choice)
    elif user_choice == 'latte':
        emote = '🥤'
        price = MENU['latte']['cost']
        step(user_choice)
    elif user_choice == 'cappuccino':
        emote = '🍵'
        price = MENU['cappuccino']['cost']
        step(user_choice)
    elif user_choice == 'off':
        print('\nYou\'ve turned off the coffee machine.')
        program = False
    elif user_choice == 'report':
        report()
    else:
        print('\nYour input is invalid.')
        program = False
