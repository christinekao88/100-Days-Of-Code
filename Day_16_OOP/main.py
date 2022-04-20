from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# 此時為function，要先create object才能使用裡面的東西
moneymachine = MoneyMachine.process_coins
# print(moneymachine)

# create object(小寫+下底線) from class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    # return espresso/latte/cappuccino
    option = menu.get_items()
    choice = input(f"​What would you like? ({option}) : ").lower()
    if choice=='off':
        is_on = False
    elif choice=='report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice) # return a menuitem object

        # is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        # is_payment_successful = money_machine.make_payment(drink.cost)
        # if is_enough_ingredients and is_payment_successful:
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
