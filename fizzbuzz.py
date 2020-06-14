user_input = int(input("Bitte gib eine Nummer zwischen 1 und 100 ein: "))

for x in range(1, user_input + 1):
    if (x % 3 == 0) and (x % 5 == 0):
        print("fizzbuzz")
    elif (x % 5) == 0:
        print("buzz")
    elif (x % 3) == 0:
        print("fizz")
    else:
        print(x)




