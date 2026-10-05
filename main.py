import random

while True:
    answer = input("Roll the dice? Y/N: ")

    if answer.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Your numbers are {dice1} and {dice2}")
        print(f"Your total number is {dice1 + dice2}")
    elif answer.lower() == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid input. Please enter Y or N.")
