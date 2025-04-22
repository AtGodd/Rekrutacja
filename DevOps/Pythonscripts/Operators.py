# Arithmetic Operators
"""
x = 2
y = 7
total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = y/x
print(total)

total = y % x
print(total)

total = y**x
print(total)
"""
'''
#Comparison Operator
a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)

#Assignment operators

c = 0
d = 1

#c+=d # c = c+d
#print(c)

c-=d # c = c-d
print(c)

#Logical Operators

# and
# or

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (a > b) or (x < y)
print(out)

out = (a > b) or (x > y)
print(out)

out = (a > b) and (x < y)
print(out)

out = (a < b) and (x < y)
print(out)

out = not(x < y)
print(out)
'''
#Membership operator
first_tuple = ("str1", "DevOps", 47, "num1", 1.5)
ans = "DevOps" in first_tuple
print(ans)

ans = "DevOps" not in first_tuple
print(ans)

ans = 67 in first_tuple
print(ans)

ans = 47 not in first_tuple
print(ans)

#Identity Operators

a = 12
b = 15

result = a is b
print(result)

result = a is not b
print(result)