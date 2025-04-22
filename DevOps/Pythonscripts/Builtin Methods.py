# String build in methods/functions

message = "corona vaccine is ready to use, 90per effective"
print(message)
print(message.capitalize())
Message=message.capitalize()
print(Message)

"""
#dir() function
print(dir(""))
print("SPACER1")
print(dir([]))
print("SPACER2")
print(dir(()))
print("SPACER3")
print(dir({}))
print("SPACER4")


print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("ready"))
print(message[18:24])
print(message.find("not"))
"""
"""
seq1 = ("192", "168", "40", "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))
"""
"""
mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountains)

mountains.append("Orgeon mount")
print(mountains)

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2,"Mt Abu")
print(mountains)

mountains.pop()
print(mountains)

mountains.pop(5)
print(mountains)
"""

cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
print (cntr_emp1.keys())
print (cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
