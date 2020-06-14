import random

secret = random.randint(1, 30)
guess = 0
attempts = 5

for x in range(5):
    user_input = input("Please enter a number between 1 and 30: ")
    guess = int(user_input)

    if secret == guess:
        print("Correct guess.")
        break

    elif secret > guess:
        attempts_left = attempts - 1 - x
        if attempts_left == 0:
            print("Too small. You have got no attempts left. Game over.")
        else:
            print("Too small. You have got " + str(attempts_left) + " attempt(s) left.")

    else:
        attempts_left = attempts - 1 - x
        if attempts_left == 0:
            print("Too big. You have got no attempts left. Game over.")
        else:
            print("Too big. You have got " + str(attempts_left) + " attempt(s) left.")


