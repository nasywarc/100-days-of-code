from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()

user_input = input('Choice : ')

item.find_drink(user_input)
item.get_items()
