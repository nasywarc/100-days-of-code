from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_object = Menu()
coffee_object = CoffeeMaker()
money_object = MoneyMachine()

user_input = input(f'What would you like? {menu_object.get_items()} : ')
if user_input == 'off':
    print('off')
elif user_input == 'report':
    print('report')
else:
    find = menu_object.find_drink(user_input)
    if find:
        print('yes')
    else:
        print('no')
