import art
print(art.logo)

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

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.


def main_function():
    coffee_order = input("Hello, what would you like to order? \n").lower()
    if coffee_order == "off":
        return

# TODO: 3. Print report.
    elif coffee_order == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}\n")


