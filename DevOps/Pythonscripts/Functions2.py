#Keywords arguments
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

#vac_feedback("Pfizer", 95)
#vac_feedback("Unkown", 45)
vac_feedback(efficancy=34, vac="Unkown")
