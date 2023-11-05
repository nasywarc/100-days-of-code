from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()

user_input = input('Choice : ')

drinks.find_drink(user_input)
drinks.get_items()
