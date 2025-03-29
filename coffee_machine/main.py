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


# TODO: 4. Check resources sufficient?

    elif coffee_order == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            print("You can drink an espresso.")
        else:
            print("Sorry! There is not enough resources.")

    elif coffee_order == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
            print("You can drink a latte.")
        else:
            print("Sorry! There is not enough resources.")

    elif coffee_order == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
                print("You can drink a cappuccino.")
        else:
            print("Sorry! There is not enough resources.")


# TODO: 5. Process coins.
    if coffee_order in MENU:
        cost = MENU[coffee_order]["cost"]
        print(f"The cost of {coffee_order} is ${cost} Please insert coins.")

        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        total_inserted = quarters + dimes + nickles + pennies


# TODO: 6. Check transaction successful?
        if total_inserted >= cost:
            change = round(total_inserted - cost, 2)
            print(f"Transaction successful! Here is your drink. Your change is ${change}")
            resources["money"] += cost  # Add the cost to the resources
        else:
            print(f"Sorry, that's not enough money, ${total_inserted} refunded.")


main_function()
