from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MenuItem()
# Menu()
# CoffeeMaker()
# MoneyMachine()

user_input = input("Choice : ")

if user_input == 'latte':
    print(user_input.menu([2]))

user_input = Menu()
