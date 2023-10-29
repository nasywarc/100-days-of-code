import os
import random
from coffee_machine import MENU
from coffee_machine import resources


def water():
    pass


def milk():
    pass


def coffee():
    pass


def insert_coin(price, coffee):
    print('Please insert coins.')
    quarters = float(input('Quarters: '))
    dimes = float(input('Dimes\t: '))
    nickles = float(input('Nickles\t: '))
    pennies = float(input('Pennies\t: '))
    total = (0.25 * quarters) + (0.1 * dimes) + \
        (0.05 * nickles) + (0.01 * pennies)
    if total > price:
        price(f'Here is ${total-price} in change.')
    elif total < price:
        print('Sorry that\'s not enough money. Money refunded.')
    else:
        price(f'Here is your {coffee}, enjoy!')


def money_count():
    pass


def report():
    print(f'Water\t: {water_stock}ml')
    print(f'Milk\t: {water_stock}ml')
    print(f'Coffee\t: {water_stock}g')
    print(f'Money\t: ${money_earned}')


money_earned = 0
water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']

os.system('cls')
user_choice = input(
    'What would you like? (espresso/latte/cappuccino) : ')
if user_choice == 'espresso':
    price = MENU['espresso']['cost']
    insert_coin(price, user_choice)
elif user_choice == 'latte':
    price = MENU['latte']['cost']
    insert_coin(price, user_choice)
elif user_choice == 'cappuccino':
    price = MENU['cappuccino']['cost']
    insert_coin(price, user_choice)
elif user_choice == 'off':
    print('\nYou\'ve turned off the coffee machine.')
    exit()
elif user_choice == 'report':
    report()
