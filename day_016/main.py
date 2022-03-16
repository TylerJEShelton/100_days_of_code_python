from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu_func = Menu()
coffee_pot = CoffeeMaker()
money = MoneyMachine()

while is_on:
    user_selection = input(f"What would you like? ({menu_func.get_items()}): ").lower()

    if user_selection == "off":
        is_on = False
    elif user_selection == "report":
        coffee_pot.report()
        money.report()
    else:
        chosen_item = menu_func.find_drink(user_selection)
        if coffee_pot.is_resource_sufficient(chosen_item) and money.make_payment(chosen_item.cost):
            coffee_pot.make_coffee(chosen_item)
