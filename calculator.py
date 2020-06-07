first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
operation = input("Enter arithmetic operation")

if operation == "+" :
    result = first_number + second_number
    print("Result: " + str(result))

if operation == "-" :
    result = first_number - second_number
    print("Result: " + str(result))

if operation == "*" :
    result = first_number * second_number
    print("Result: " + str(result))

if operation == "/" :
    if second_number == 0:
        print("Division by zero is not a valid operation")
    else:
        result = first_number / second_number
        print("Result: " + str(result))