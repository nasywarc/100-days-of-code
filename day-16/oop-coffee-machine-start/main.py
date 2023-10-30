from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def espresso():
    global name, cost, ingredients
    name = 'latte'
    cost = 2.5
    ingredients = {'water': 100, 'milk': 150, 'coffee': 24}


def latte():
    global name, cost, ingredients
    name = 'latte'
    cost = 2.5
    ingredients = {'water': 100, 'milk': 150, 'coffee': 24}


def cappuccino():
    global name, cost, ingredients
    name = 'latte'
    cost = 2.5
    ingredients = {'water': 100, 'milk': 150, 'coffee': 24}


name = ''
cost = int()
ingredients = {}

# TODO : 1. Ask user what they want
user_input = input('Choice : ')
# TODO : 2. Check resources for the order
(f'{user_input}()')
user_input_instance = CoffeeMaker()
user_input_instance.is_resource_sufficient(drink=user_input)
# TODO : 3. If resources available, ask the user for their money
# TODO : 4. If not print
# TODO : 5. If their money enough, minus the resources
# TODO : 6. If success, print to user
