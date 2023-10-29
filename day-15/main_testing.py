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


def insert_coin():
    print('Please insert coins.')
    quarters = int(input('Quarters\t: '))
    dimes = int(input('Dimes\t: '))
    nickles = int(input('Nickles\t: '))
    pennies = int(input('Pennies\t: '))


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
    pass
elif user_choice == 'latte':
    pass
elif user_choice == 'cappuccino':
    pass
elif user_choice == 'off':
    print('\nYou\'ve turned off the coffee machine.')
    exit()
elif user_choice == 'report':
    report()
