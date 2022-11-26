"""
from random import randint

user_choice = int(input("choose number."))

# pc_choice = random.randint(a, b)
pc_choice = randint.(1, 50) # I imported this.

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higher!")

"""

distance = 0

while distance < 20:
    print("I'm running:", distance, "km")
    distance = distance + 1


