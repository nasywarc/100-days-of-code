from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

menu_object = Menu()
coffee_object = CoffeeMaker()
money_object = MoneyMachine()
off = False

os.system('cls')
while not off:
    user_input = input(f'What would you like? {menu_object.get_items()} : ')
    if user_input == 'off':
        off = True
    elif user_input == 'report':
        coffee_object.report()
        money_object.report()
    else:
        find = menu_object.find_drink(user_input)
        if find:
            if (coffee_object.is_resource_sufficient(find)):
                if money_object.make_payment(find.cost):
                    coffee_object.make_coffee(find)
