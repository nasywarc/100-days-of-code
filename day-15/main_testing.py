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


def money_count():
    pass


def report():
    pass


money_earned = 0
water_stock = resources['water']
milk_stock = resources['milk']
coffee_stock = resources['coffee']

os.system('cls')
user_choice = input(
    'What would you like? (espresso/latte/cappuccino)\nInput -> ')
if user_choice == 'espresso':
    pass
elif user_choice == 'latte':
    pass
elif user_choice == 'cappuccino':
    pass
elif user_choice == 'off':
    print('You\'ve turned off the coffee machine.')
    exit()
elif user_choice == 'report':
    report()
