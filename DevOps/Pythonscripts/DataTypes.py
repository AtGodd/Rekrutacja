#Strings
str1 = "alpha"
str2 = 'Beta'
str3 = '''Gamma string'''
str4 = """Delta string"""

#Numbers
num1 = 123
flt1 = 2.0

#List/Collection of multi datatype, enclosed in square brackets.
first_list = [str1, "DevOps", 47, num1, 1.5] #List is Mutable = you can edit list

#Printing a list
print(first_list)

#Tuple/ Collection of multi datatype, enclosed in round bracket
first_tuple = (str1, "DevOps", 47, num1, 1.5)    #Tuple is immutable = cannot edit tuple

print(first_tuple)

# Dictionary/ Elements in the dictionary are always in paris(Key:Value), curly brackets.
first_dictionary = {"Name":"AtGod", "Weight":75, "Exercises":["Boxing", "Running", "Swimming"]}

#Printing a Dictionary
print(first_dictionary)

print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:", type(first_dictionary))

#Boolean
x = True
y = False

#Printing Boolean
print(x)
print(y)

print("x is a ", type(x))
print("y is a ", type(y))