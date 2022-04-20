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


# Check resources sufficient?
def check_resources(coffee_type):
    for ingredient in resources:
        if resources[ingredient] <= MENU[coffee_type]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        resources[ingredient] -= MENU[coffee_type]['ingredients'][ingredient]
        # print(f"{ingredient} remain {resources[ingredient]}")
    return True

money = 0

def pay(coffee_type):
    print("Please insert coins.")
    pay = int(input("how many quarters?: "))*0.25
    pay += int(input("how many quarters?: "))*0.1
    pay += int(input("how many quarters?: "))*0.05
    pay += int(input("how many quarters?: "))*0.01
    price = MENU[coffee_type]["cost"]
    change = pay - price
    if price >= pay:
        print(f"Sorry that's not enough money. Money refund")
        return False
    else:
        print(f"Your payment is ${round(pay,2)}. Here is ${round(change,2)} in change.")
        global money
        money+=price
        return True

keeping = True
while keeping:
    coffee_type = input("​What would you like? (espresso/latte/cappuccino) : ").lower()
    if coffee_type == 'off':
        keeping = False
    elif coffee_type == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}")
    else:
        if check_resources(coffee_type) :
            pay(coffee_type)
            print(f"Here is your {coffee_type} ☕️. Enjoy!")
