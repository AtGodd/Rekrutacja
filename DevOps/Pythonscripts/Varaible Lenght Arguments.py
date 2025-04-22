#Varaible Lenght Arguments *args(Non keywords arguments)

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    #print(args)
    for item in args:
         print(f"You have ordered: {item}")
    print("Your food will be delivered in 30mins:")
    print("Enjoy the meal")

order_food("Salad", "Pizza", "Soup", "Chicken")

