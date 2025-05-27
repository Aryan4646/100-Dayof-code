MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "milk" : 0,
            "coffee": 18
        },
        "cost" : 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk" : 150,
            "coffee": 18
        },
        "cost" : 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 5,
}

def resource_check(l):
    z = ["water","milk","coffee"]
    count = 0
    for i in z:
        if resources[i] >= MENU[l]["ingredients"][i]:
            count += 1
        else:
            return f"Sorry {i} is insufficient"
    return "e"

def trans_check(w,t):
    if MENU[w]["cost"] <= t:
        return "success"
    else:
        return "You do not have necessary funds, Money refunded."
def update_resources(w):
    resources["water"] -= MENU[w]["ingredients"]["water"]
    resources["milk"] -= MENU[w]["ingredients"]["milk"]
    resources["coffee"] -= MENU[w]["ingredients"]["coffee"]
    resources["money"] += MENU[w]["cost"]

coff = True
while coff:
    valid_input = True
    while valid_input:
        want = input("What would you like to have (espresso/latte/cappuccino): ").lower()
        if want == "espresso" or want == "latte" or want == "cappuccino":
            print(f"You would like to have: {want}")
            valid_input = False
        elif want == "report":
            print(f"Water: {resources['water']}\n"
                  f"Milk: {resources['milk']}\n"
                  f"Coffee: {resources['coffee']}\n"
                  f"Money: ${resources['money']}")
        else:
            print("Invalid input bro try again!")
            print("\n"*4)
    sufficient = resource_check(want)
    total_val = 0
    if sufficient == "e":
        quarters = int(input("Enter the number of quarters: "))
        dimes = int(input("Enter the number of dimes: "))
        nickles = int(input("Enter the number of nickels: "))
        pennies = int(input("Enter the number of pennies: "))

        total_val = (0.25*quarters) + (0.10*dimes) + (0.05* nickles) +(0.01*pennies)
    else:
        print(sufficient)
        continue
    trans = trans_check(want, total_val)
    if trans == "success":
        change = total_val - MENU[want]["cost"]
        print(f"Your change is {change}")
        update_resources(want)
        print(f"You coffee is successfully created.")
    quest = input("Is there any new customer? if not write q: ")
    if quest == "q":
        coff = False




