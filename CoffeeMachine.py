
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
       "water" : 300,
       "milk" : 200,
       "coffee" : 100
      }

profit = 0

def coin_counter():
    """"This will give total money give bt the customer"""
    print("Please insert coin.")
    total = int(input("How many quarters : "))*0.25
    total += int(input("How many dimes : "))*0.1
    total += int(input("How many nickles : "))*0.05
    #total += int(input("How many pennies : "))*0.01
    print(total)
    return total

def change():
    extra = payment - coffe_cost
    clear = False

    print(f"You have given ${extra} extra money")

    while clear == False:
        print("hello")

        left = extra % 0.25
        number_0f_coin = extra // 0.25
        print(f"collect {number_0f_coin} quarters")
        clear = True

        if left == 0:
            print("Collect your money.")
            print("Enjoy your coffee.")
            clear = True

        else:
            left = left % 0.1
            number_0f_coin = left // 0.1
            print(f"collect {number_0f_coin} quarters")

            if left == 0:
                print("Collect your money.")
                print("Enjoy your coffee.")
                clear = True

            else:
                left = left % 0.05
                number_0f_coin = left // 0.05
                print(f"collect {number_0f_coin} quarters")
                print("Collect your money.")
                print("Enjoy your coffee.")


def is_transtion_successful():
    if payment > coffe_cost:
        change()


    elif payment == coffe_cost:
        print("Enjoy your coffee.")

    else:
        print(f"This is not enough money to make {choice} coffee.")

def is_resource_suffcient(ingredients):
    for item in ingredients:
        print(item)
        print(ingredients[item])
        print(resources[item])
        if ingredients[item] >= resources[item]:
            print(f"Resource of {item} is insufficient to make {choice} coffee.")
            return False
    else:
         return True


is_on = True
while is_on:
    choice = input("What would like to have (espresso/latte/cappuccino): ")
    if choice == "off" :
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['Water']}ml ")
        print(f"Milk: {resources['Milk' ]}ml")
        print(f"Coffee: {resources['Coffee']}gm")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]

        if is_resource_suffcient(drink["ingredients"]):
            coffe_cost = drink["cost"]
            print(f"The cost of {choice} coffee is : ${coffe_cost} ")
            payment = coin_counter()
            is_transtion_successful()
