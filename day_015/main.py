MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

is_on = True


def print_report():
    '''This function prints the current resources in the machine'''

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    if "money" in resources:
        print(f'Money: ${resources["money"]}')


def collect_payment():
    '''This function asks the user how many of each coin they are inserting and returns the total dollar value'''

    print("Please insert your coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)


def check_payment(user_money, item_price):
    '''This function checks to see that the user entered more money than the cost of the selected item
    and returns the change or returns False if there was not enough money'''

    if user_money > item_price:
        user_change = user_money - item_price
        return user_change
    else:
        return False


def check_resources(ingredients):
    '''This function checks to see if the required resources are in the machine.
    It returns the name of the ingredient that is short.'''

    if resources["water"] < ingredients["water"]:
        return "water"
    if "milk" in ingredients:
        if resources["milk"] < ingredients["milk"]:
            return "milk"
    if resources["coffee"] < ingredients["coffee"]:
        return "coffee"


while is_on:
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_selection == "off":
        is_on = False
    elif user_selection == "print":
        print_report()
    elif user_selection == "espresso":
        short_ingredient = check_resources(MENU[user_selection]["ingredients"])
        if not short_ingredient:
            money = collect_payment()
            revenue = MENU[user_selection]["cost"]
            change = check_payment(money, revenue)
            if change:
                print(f"Here is your change: ${round(change, 2)}.")
                resources["money"] += revenue
                resources["water"] -= MENU[user_selection]["ingredients"]["water"]
                resources["coffee"] -= MENU[user_selection]["ingredients"]["coffee"]
                print(f"Here is your {user_selection} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {short_ingredient}.")
    elif user_selection == "latte":
        short_ingredient = check_resources(MENU[user_selection]["ingredients"])
        if not short_ingredient:
            money = collect_payment()
            revenue = MENU[user_selection]["cost"]
            change = check_payment(money, revenue)
            if change:
                print(f"Here is your change: ${round(change, 2)}.")
                resources["money"] += revenue
                resources["water"] -= MENU[user_selection]["ingredients"]["water"]
                resources["milk"] -= MENU[user_selection]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_selection]["ingredients"]["coffee"]
                print(f"Here is your {user_selection} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {short_ingredient}.")
    elif user_selection == "cappuccino":
        short_ingredient = check_resources(MENU[user_selection]["ingredients"])
        if not short_ingredient:
            money = collect_payment()
            revenue = MENU[user_selection]["cost"]
            change = check_payment(money, revenue)
            if change:
                print(f"Here is your change: ${round(change, 2)}.")
                resources["money"] += revenue
                resources["water"] -= MENU[user_selection]["ingredients"]["water"]
                resources["milk"] -= MENU[user_selection]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_selection]["ingredients"]["coffee"]
                print(f"Here is your {user_selection} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {short_ingredient}.")
    else:
        print("Invalid selection!")

