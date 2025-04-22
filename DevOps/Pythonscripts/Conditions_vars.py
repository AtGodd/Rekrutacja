"""
Testing knowledge on condtions and different datatypes.
"""

print("This IT Org has various skill sets")
print("Find out your best")

print("Enter Capitalised values: ")

Devops = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1024}

usr_skill = input("Enter your desired skill:  ")
#print(usr_skill)

#Check in database if we have this skill
if usr_skill in Devops:
    print(f"We have {usr_skill} in Devops Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employess with {usr_skill} skill.")
else:
    print("Skill not found")
    print("Check skills by captlized letters")