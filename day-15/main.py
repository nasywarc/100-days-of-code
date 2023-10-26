import os
import random
from coffee_machine import MENU
from coffee_machine import resources


def water():
    remain_water = int()
    if user_choice == 'espresso':
        remain_water = resources['water'] - \
            MENU['espresso']['ingredients']['water']
    elif user_choice == 'latte':
        remain_water = resources['water'] - \
            MENU['latte']['ingredients']['water']
    elif user_choice == 'cappuccino':
        remain_water = resources['water'] - \
            MENU['cappuccino']['ingredients']['water']
    return remain_water


def milk():
    remain_milk = int()
    if user_choice == 'espresso':
        remain_milk = resources['milk']
    elif user_choice == 'latte':
        remain_milk = resources['milk'] - MENU['latte']['ingredients']['milk']
    elif user_choice == 'cappuccino':
        remain_milk = resources['milk'] - \
            MENU['cappuccino']['ingredients']['milk']
    return remain_milk


def coffee():
    remain_coffee = int()
    if user_choice == 'espresso':
        remain_coffee = resources['coffee'] - \
            MENU['espresso']['ingredients']['coffee']
    elif user_choice == 'latte':
        remain_coffee = resources['coffee'] - \
            MENU['latte']['ingredients']['coffee']
    elif user_choice == 'cappuccino':
        remain_coffee = resources['coffee'] - \
            MENU['cappuccino']['ingredients']['coffee']
    return remain_coffee


def print_all():
    print(water())
    print(milk())
    print(coffee())


user_choice = input(
    'What would you like? (espresso/latte/cappuccino)\nInput -> ')
if user_choice == 'espresso':
    print_all()
elif user_choice == 'latte':
    print_all()
elif user_choice == 'cappuccino':
    print_all()
elif user_choice == 'off':
    pass
elif user_choice == 'report':
    pass
