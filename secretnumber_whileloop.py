import random

secret = random.randint(1, 30)
guess = 0

while secret != guess:
    user_input = input("Please enter a number between 1 and 30: ")
    guess = int(user_input)
    if secret == guess:
        print("Correct guess.")
    elif secret > guess:
        print("Too small.")
    else:
        print("Too big.")


