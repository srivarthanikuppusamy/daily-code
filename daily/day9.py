key = 25
attempts = 0

while True:
    num = int(input("Enter a number: "))
    attempts += 1

    if num < key:
        print("Too low")
    elif num > key:
        print("Too high")
    else:
        print("Correct!")
        print("Attempts:", attempts)
        break
