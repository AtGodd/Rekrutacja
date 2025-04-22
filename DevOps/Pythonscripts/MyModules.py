import random

def vac_feedback(vac, efficancy):
    print(f"{vac} Vaaccine is having {efficancy} % efficancy")
    if (efficancy > 50) and (efficancy <= 75):
        print("Seems okayish")
    elif (efficancy > 75) and (efficancy <= 90):
        print("Its Great")
    elif  efficancy >= 90:
        print("its almost perfect")
    else:
        print("Its weak")

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    #print(args)
    for item in args:
         print(f"You have ordered: {item}")
    print("Your food will be delivered in 30mins:")
    print("Enjoy the meal")

def time_activity(*args,**kwargs):
    """
    Input: Multiple values for mintues, key=value pair activity
    Output: Return sum of minutes + random minute spect on a random activity
    """
    #print(args)
    #print(kwargs)
    min = sum(args) + random.randint(0,60)
    #print(min)
    choice = random.choice(list(kwargs.keys()))
    #print(choice)
    print(f"You have to spend {min} minutes for {kwargs[choice]}")