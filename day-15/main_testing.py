import os
import random
from coffee_machine import MENU
from coffee_machine import resources


def water(coffee):
    global water_stock
    pass


def milk(coffee):
    global milk_stock
    pass


def coffee(coffee):
    global coffee_stock
    pass


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
        print(f'\nHere is your {coffee} {emote}\nEnjoy!')
    elif total < price:
        print('\nSorry that\'s not enough money. Money refunded.')
    else:
        print(f'\nHere is your {coffee} {emote}\nEnjoy!')


def money_count():
    pass


def report():
    print(f'Water\t: {water_stock}ml')
    print(f'Milk\t: {water_stock}ml')
    print(f'Coffee\t: {water_stock}g')
    print(f'Money\t: ${money_earned}')


def charge_stock(coffee):
    if coffee != 'espresso':
        milk_stock -= MENU[f'{coffee}']['ingredients']['milk']
        if milk_stock <= 0:
            print('Sorry there is not enough milk.')
            milk_stock += MENU[f'{coffee}']['ingredients']['milk']

    water_stock -= MENU[f'{coffee}']['ingredients']['water']
    if water_stock <= 0:
        print('Sorry there is not enough water.')
        water_stock += MENU[f'{coffee}']['ingredients']['water']

    coffee_stock -= MENU[f'{coffee}']['ingredients']['coffee']
    if coffee_stock <= 0:
        print('Sorry there is not enough coffee.')
        coffee_stock += MENU[f'{coffee}']['ingredients']['coffee']


money_earned = 0
water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']

os.system('cls')
user_choice = input(
    'What would you like? (espresso/latte/cappuccino) : ')
if user_choice == 'espresso':
    emote = '☕'
    price = MENU['espresso']['cost']
    insert_coin(price, user_choice, emote)
    charge_stock(user_choice)
elif user_choice == 'latte':
    emote = '🥤'
    price = MENU['latte']['cost']
    insert_coin(price, user_choice, emote)
    charge_stock(user_choice)
elif user_choice == 'cappuccino':
    emote = '🍵'
    price = MENU['cappuccino']['cost']
    insert_coin(price, user_choice, emote)
    charge_stock(user_choice)
elif user_choice == 'off':
    print('\nYou\'ve turned off the coffee machine.')
    exit()
elif user_choice == 'report':
    report()
