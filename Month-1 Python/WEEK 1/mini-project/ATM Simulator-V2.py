#====================================
# ATM SIMULATOR V2
#====================================
"""
* display the menu repeatedly until the user chooses to exit.
* Deposit money and update the balance
* Withdraw money with validation
* Check the current balance
* Handle invalid menu choices
* Exit using break
"""

balance = 10000

while True:
    print("\n===== ATM Menu: =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("=====================")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        amount = int(input("Enter the amount to deposit: "))

        if amount > 0:
            balance += amount
            print("Deposit successful. your balance is now", balance)
        else:
            print("Invalid amount.")


    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        elif amount % 100 != 0:
            print("Amount must be a multiple of 100.")
        else:
            balance -= amount
            print("Withdrawal successful. your balance is now", balance)


    elif choice == 3:
        print("Your balance is", balance)

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")