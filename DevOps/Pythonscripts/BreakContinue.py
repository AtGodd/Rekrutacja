# Break statement
"""
for i in "Devops":
    print(i)
    if i == "o":
        print("Found my data")
        break

print("Out of loop")
"""
"""
# Continue statement
for i in "Devops":
    print(i)
    if i == "o":
        print("Found my data")
        continue
    print(f"Value of i is {i}")

print("Out of loop")
"""
"""
import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "Covaxin", "AstraZenca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"***TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("#################")
        print(f"{LUCKY} Vaccine, Test Succesful")
        print("#################")
        print()
        break
    print("XXXXXXXXXX")
    print("Test failed")
    print("XXXXXXXXXX")
    print()
"""

import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "Covaxin", "AstraZenca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"***TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("#################")
        print(f"{LUCKY} Vaccine, Test Succesful")
        print("#################")
        print()
        continue
    print("XXXXXXXXXX")
    print("Test failed")
    print("XXXXXXXXXX")
    print()