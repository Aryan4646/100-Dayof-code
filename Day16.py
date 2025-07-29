# Day 16 of 100 day of code
# import turtle
#
# timmy = turtle.Turtle()
# screen = turtle.Screen()
# print(timmy)
# timmy.forward(100)
# print(screen.canvheight)
# screen.exitonclick()

from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
obj = CoffeeMaker()
money = MoneyMachine()
m = Menu()
while is_on:
    options = m.get_items()
    user_input = input(f"What would you like? {options}:").lower()
    if user_input == "report":

        print(f"Resources are as follows:")
        obj.report()
        money.report()
    elif user_input == "off":
        is_on = False
    else:
        drink = m.find_drink(user_input)
        print(f"You would like to have: {user_input}")
        if obj.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                obj.make_coffee(drink)



