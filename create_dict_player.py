"""
Write a python script to create a dictionary where key values are cricket player
names and data-values are tuple of 4 elements- matches played, total runs,
half centuries and centuries. All data should be taken from user.
"""

# taking input from the user
N = int(input("Enter how players data you want to store : "))

# creating a empty dictionary
players = dict()

# adding elements in dictionary
while N != 0 :
    name = input("Enter player name : ")
    players[name] = tuple([int(input("Matches played : ")), int(input("Total runs : ")), int(input("Half centuries : ")), int(input("Centuries : ")),])
    N -= 1    

# printing dictionary
print("#####################################")
for item in players :
    print(item, players[item])
print("#####################################")