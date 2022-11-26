
from random import randint

print("Welcom to Python Casino")
# pc_choice = randint(1, 50) # I imported this.
pc_choice = randint(1, 100)

playing = True

while playing:
    # user_choice= int(input("Choose number:"))
    user_choice= int(input("Choose number (1-100):"))
    if user_choice == pc_choice:
        print("You won!")
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")
