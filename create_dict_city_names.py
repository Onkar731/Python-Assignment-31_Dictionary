"""
Write a python script to create a dict object from a list of city names in such a way
that alphabets are keys of the dictionary and list of city names starting from that
alphabet will be its data value.
"""

# creating a list of city names
cities = ['Aurangabad', 'Bhopal', 'Allhabad', 'Agartala', 'Warangal', 'Banaras', 'calicat', 'bangluru', 'pune', 'mumbai']

# creating a empty dictionary 
city_dict = dict()

# adding city names in dictionary
for e in cities:
    city_dict[e[0]] = [c_name for c_name in cities if e[0] == c_name[0]]

# printing dictionary
for k,v in city_dict.items() :
    print(k, v)