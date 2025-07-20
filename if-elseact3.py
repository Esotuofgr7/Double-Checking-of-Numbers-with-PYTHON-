number = int(input("Enter a number: "))

if number > 50:
    print("The number is greater than 50.")
    if number % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is not greater than 50.")
