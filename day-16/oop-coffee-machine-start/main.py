from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
order_name = Menu()
coffee_maker = CoffeeMaker()

order_name = input('Choice : ')
if order_name.get_items():
    print('menu available')
else:
    print('not available')
