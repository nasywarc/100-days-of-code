from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
order_name = Menu()
coffee_maker = CoffeeMaker()

choice = 'latte'

if order_name.find_drink(choice) == True:
    print('right')
else:
    print('wrong')
