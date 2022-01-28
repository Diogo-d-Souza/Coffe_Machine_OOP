from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffee = CoffeeMaker()
money = MoneyMachine()
turn_off = True

while turn_off:
    choice = input(f"what would you like? ({menu.get_items()})? ")
    if choice == "off":
        turn_off = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

