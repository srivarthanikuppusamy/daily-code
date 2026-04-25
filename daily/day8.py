print("Choice 1: Addition")
print("Choice 2: Subtraction")
print("Choice 3: Multiplication")
print("Choice 4: Division")
choice = int(input("Enter your choice (1-4): "))
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if choice == 1:
    print("The addition of the 2 numbers is:", num1 + num2)
elif choice == 2:
    print("The subtraction of the 2 numbers is:", num1 - num2)
elif choice == 3:
    print("The multiplication of the 2 numbers is:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("The division of the 2 numbers is:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
