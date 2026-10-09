#Session 4
#Match-Case
"""
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Deposit")
    case 2:
        print("Withdraw")
    case 3:
        print("Check Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")
"""
"""
command = input("Enter your command: ").lower()

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case "resume":
        print("Resuming...")
    case _:
        print("Invalid command")
"""

choice = input("1. Addiditon \n2. Subtraction \n3. Multiplication \n4. Division \nEnter your choice: ").lower()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1 / num2)
    case _:
        print("Invalid choice")