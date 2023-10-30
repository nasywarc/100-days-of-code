from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

program = True
latte = MenuItem('latte', 200, 150, 24, 2.5)
# latte = MenuItem(name='latte', water=200, milk=150, coffee=24, cost=2.5)

while program:
    user_choice = str(input('Espresso, latte, cappuccino? '))
    if user_choice == latte.name:
        print(f'{latte.name}\n{latte.cost}')
