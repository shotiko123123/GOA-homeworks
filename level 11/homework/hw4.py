# მომხმარებლისგან ორი რიცხვის და ოპერაციის შეყვანა
num1 = float(input("Enter Number: "))
num2 = float(input("Enter Nubmer: "))
operation = input("Enter which one you need (+, -, *, /): ")
if operation == "+":
    print("Reseult:", num1 + num2)
elif operation == "-":
    print("Reseult:", num1 - num2)
elif operation == "*":
    print("Reseult:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Reseult:", num1 / num2)
    else:
        print("Wrong Operation!")
else:
    print("Wrong Operation!")