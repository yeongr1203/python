age = int(input("How old are you?"))

if age < 18:
    print("You can't drink.")
elif age >= 18 and age =< 35:
    print("You drink Beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")