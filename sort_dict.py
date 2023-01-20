"""
Write a python script to sort a dictionary by its keys in descending order
"""

# creating a dictionary of keys as natrual numbers and data values are their squares
d = {1:1, 7:49, 2:4, 3:9, 4:16, 5:25, 6:36, 8:64, 9:81, 10:100,}

# sorting dictionary by its keys in descending order
print("Sorted in reverse order :")
for e in sorted(d, reverse=True) :
    print(e, d[e])

