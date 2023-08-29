# cli-games/bnc.py

input = input("Greetings, what is your name? > ")
print("Greetings", input)

player = input("Bear, Ninja, or Cowboy? >")
print (player)

import random 
print (random ("Bear, Ninja, Cowboy"))


from random import randint 
roles = ["Bear, Ninja, Cowboy"]

computer = roles[randint(0,2)]

print (computer)