import main
from main import resources
from main import MENU


# TODO 1 - Get input from the user

# TODO 2 - Get Report
#Report function
def print_report():
    """Print the current status of the resources and money."""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {resources["profit"]}")

#Choice validity function
def is_valid_choice(choice):
    """Check if the uses's choice is valid."""
    return choice in MENU

#Ingredient Sufficiency function
def ingredients_enough(coffee_type):
    """Returns True if the ingredients are enough and False otherwise"""
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources.get(item, 0):
            print(f"Sorry {item} is not enough.")
            return False
    return True

#Coin Process Function
def coin_process():
    """Returns the total amount inserted by the user"""
    print("\nPlease insert coins.")
    quaters = int(input("How many quaters? "))  #$0.25
    dimes = int(input("How many dimes? "))      #$0.10
    nickels = int(input("How many nickels? "))  #$0.05
    pennies = int(input("How many pennies? "))  #$0.01

    total = (quaters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return round(total, 2)

#Transaction check Function
def transaction_success(payment, coffee_cost):
    if payment >= coffee_cost: 
        change = round(payment - coffee_cost, 2)
        if change > 0:
            print (f"Here is your ${change} change. Have a great day 😊...")
        resources["money"] += coffee_cost
        return True
    else:
        print ("Sorry, not enough money. Refunded ")
        return False

#Deduct Ingredient Function
def deduct_ingredients(coffee_type):
    """Deduct the ingredients from the dictionary after making the coffee"""
    coffee_content = MENU[coffee_type]["ingredients"]
    for item in coffee_content:
        resources[item] -= coffee_content[item]

    print(f"Here is your {coffee_type}. Enjoy1 🍵")


#Main Loop
def coffee_machine():
    machine_on = True
    while machine_on:
        choice = input ("""\nWhat would you like? (espresso/latte/cappuccino) or would you like to turn it (off)?\n""").lower()
        if choice == "off":
            machine_on = False
            print("Coffee Machine going off. Tschüss!")
        elif choice == "report":
            print_report()
        elif is_valid_choice(choice):
            print (f"You chose {choice}. Processing with your order...")
            if ingredients_enough(choice):
                print(f"There's enough ingredients. Making your {choice} drink... 🍵")
                payment = coin_process()
                if transaction_success(payment, MENU[choice]["cost"]):
                    print(f"Preparing your {choice}... 🍵\n")
                    deduct_ingredients(choice)
            else:
                print("Order cancelled due to insufficient ingredients")
        else:
            print ("Invalid input. Please choose again espresso/latte/cappuccino.")


coffee_machine()
