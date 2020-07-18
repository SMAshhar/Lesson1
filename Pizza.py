pizzaOptions = ["small", "medium", "large"]
pizzaToppings = ["pepperoni", "mushroom", "green pepper","cheese", "extra cheese"]
order = []
toppings = []

print("""
        We are now offering unlimited toppings... !!!
        """)
input()
print("""
        Sizes available are :
        1. Small
        2. Medium
        3. Large
        """)
PO = input("Please enter pizza size (Q to quite)").lower()
thisOrder = 1
if PO == "q":
    a = 0
elif PO in pizzaOptions:
    order.append(PO)
    while  thisOrder == 1:
        print("""
        Toppings available are:
        1. Pepperoni            2. Mushroom
        3. Green Pepper         3. Cheese
        4. Extra Chees
        """)
        PT = input("Enter Toppings (enter Q to quite) : ").lower()
        if PT == "q":
            thisOrder = 0
            break
        elif PT in pizzaToppings:
            toppings.append(PT)
        else:
            print(f"{PT} is not available")
else:
    print("The said is not in options")

print(f"""
        YOur Order is a {order[0].title()} pizza with following toppings: 
        """)
for a in toppings:
    print(f"\t{a.title()}")
