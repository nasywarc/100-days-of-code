from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
coffee_maker = CoffeeMaker()

user_input = input('Choice : ')

coffee_maker.is_resource_sufficient(user_input)
