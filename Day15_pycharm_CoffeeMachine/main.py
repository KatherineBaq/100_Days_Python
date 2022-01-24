# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
}
money = 0
status_machine = True
def coffee_machine(resources_in,  money_in):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        return False, resources_in, money_in
    elif choice == "report":
        print(f"Water: {resources_in['water']}ml\nMilk: {resources_in['milk']}ml\nCoffee: {resources_in['coffee']}g")
        print(f"Money earned: ${money_in:0.2f}")
        return True, resources_in, money_in
    elif ((choice == "espresso") or (choice == "latte")) or (choice == "cappuccino"):
        for i in resources_in:
            if (i in MENU[choice]["ingredients"]) and ((resources_in[i] - MENU[choice]["ingredients"][i]) < 0):
                print(f"Sorry, there is not enough {i}")
                return True, resources_in, money_in

        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        money_insert = quarters*0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if money_insert < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return True, resources_in, money_in
        else:
            dif_mon = money_insert - MENU[choice]["cost"]
            money_in += money_insert
            for i in resources_in:
                if i in MENU[choice]["ingredients"]:
                    resources_in[i] -= MENU[choice]["ingredients"][i]
            print(f"Here is ${dif_mon:0.2f} in change.")
            print(f"Here is your {choice} ☕. Enjoy!")
            return True, resources_in, money_in
    else:
        return True, resources_in, money_in

while  status_machine:
    status_machine, resources_in, money = coffee_machine(resources,  money)