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

def pour_selection(drink_choice):
    for ingredient in MENU[drink_choice]["ingredients"]:
        resource_left = (resources[ingredient] - MENU[drink_choice]["ingredients"][ingredient])
        resources[ingredient] = resource_left

def can_pour(drink_choice):
    for ingredient in MENU[drink_choice]["ingredients"]:
        if MENU[drink_choice]["ingredients"][ingredient] > resources[ingredient]:
            return False
    return True

def insert_coins(drink_choice):
    print(f"{drink_choice} costs {MENU[drink_choice]["cost"]}. Please insert coins.")
    quarters = int(input("How many quarters?"))
    amount_inserted = (quarters * 0.25)
    if amount_inserted > MENU[drink_choice]["cost"]:
        print(f"Your change is {amount_inserted - (MENU[drink_choice]["cost"])}")
        print(f"Thank you! Your {drink_choice} is served!")
    elif amount_inserted < MENU[drink_choice]["cost"]:
        print(f"Oops! You did not insert enough coins, you are short {MENU[drink_choice]["cost"] - amount_inserted}.")
        print("Lets insert a few more.")
    else:
        print(f"Thank you! Your {drink_choice} is served!")

def run_report():
    print(f"Current levels: \n")
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient]}")

def make_coffee():
    selection = input("What would you like to drink? (espresso/latte/cappuccino): ")
    working_machine = True
    while working_machine:
        can_pour(selection)
        if can_pour(selection) is False:
            print("Sorry there are not enough ingredients")
            working_machine = False
        else:
            pour_selection(selection)
            insert_coins(selection)
            more_coffee = input("Would you like to make another coffee?")
            if more_coffee == "yes":
                make_coffee()
            power = input("Would you like to turn the coffee maker off?")
            if power == "yes":
                print("See you next time.")
                working_machine = False
            else:
                report = input("Would you like to run a report?")
                if report == "yes":
                    run_report()
                    more_coffee = input("Would you like to make another coffee?")
                    if more_coffee == "yes":
                        make_coffee()
                    else:
                        working_machine = False
                        print("See you next time.")
                else:
                    make_coffee()

make_coffee()
