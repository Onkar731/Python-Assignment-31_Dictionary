"""
Create a dict object where first N natural numbers are keys and 
their squares are data values
"""

# taking input from the user
N = int(input("Enter a number : "))

# creating a dict of keys and values using dict comphrension
d = {e:e**2 for e in range(1,N+1)}

# printing dictionary 
print(d)