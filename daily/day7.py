num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
op=input("Enter Operator:")
if (op == "+"):
    print(num1 + num2)
elif (op == "-"):
    print(num1 - num2)
elif (op == "*"):
    print(num1 * num2)
elif(op == "/"):
    print(num1 / num2)
else:
    print("invalid operator")
