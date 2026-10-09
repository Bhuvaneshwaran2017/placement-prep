#====================================
#ATM SIMULATOR
#====================================

balance = 10000
choice = int(input(
    "ATM Menu:\n" \
    "1. Deposit\n"
    "2. Withdraw\n"
    "3. Check Balance\n"
    "4. Exit\n"
    "Enter your choice: "
))

if choice == 1:
    deposit = int(input("Enter the amount to deposit: "))

    if deposit > 0:
        balance += deposit
        print("Deposited successfully!. New balance: ", balance)
    else:
        print("Invalid amount!")

elif choice == 2:
    withdraw = int(input("Enter the amount to withdraw: "))

    if withdraw > 0 and withdraw <= balance and withdraw % 100 == 0:
        balance -= withdraw
        print("Withdrawn successfully!. New balance: ", balance)
    else:
        print("Invalid amount!")

elif choice == 3:
    print("Your current balance is: ", balance)

elif choice == 4:
    print("Thank you for using the ATM!")
    exit()

else:
    print("Invalid choice!")