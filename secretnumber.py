secret = 5
guess = int(input("Please enter a number: "))

if secret == guess:
    print("Congrats. Correct guess.")
else:
    print("Sorry. Not the secret number.")


while secret != guess:
    print("Sorry. Not the secret number.")
    guess = int(input("Please enter a new number: "))
    if secret == guess:
        print("Yes")
        break