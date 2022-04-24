# Ïmporting The Resource

import random


# Asking The User Wheter Play or Not
playing = input("So, Let's Start The Game? Y|N ")
if playing.lower() != "y":
    quit("Okay! We Will Play Again")

else:
    print("Let's Get Started")

comp_guss = random.randrange(100)
attempts = 0


while True:
    user_guess = input("Guess a Number Between 1 - 100 ") # Taking Inputs From the user
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            quit(" Please Enter Number Greater Than 0")
    else:
        quit("Plese Enter A number")

    if user_guess == comp_guss:
        print("You Won")
        attempts += 1
        break
    if user_guess > comp_guss:
        print("Try With a lower Number")
        attempts += 1
    if user_guess < comp_guss:
        print("Try again With a Bigger Number")
        attempts += 1

else:
    print("Not a number")

print(attempts)
