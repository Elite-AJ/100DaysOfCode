from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machineState = True
while machineState:
    drinkName = input("What would you like ? (espresso/latte/cappuccino): ").lower
