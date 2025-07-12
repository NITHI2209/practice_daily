#12/07/2025
#question:
# Problem Statement:
# Design a simple ATM simulation in Python with the following features:
# Set an initial account balance (e.g., ₹5000).
# Display a menu with options:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# Let the user select an option by entering a number (1–4).
# Based on the user's choice:
# If 1, display the current balance.
# If 2, ask for the amount to deposit and update the balance.
# If 3, ask for the amount to withdraw:
# Allow withdrawal only if sufficient balance is available.
# If 4, exit the program.
# Show an error message if the user enters an invalid option.
# The menu should keep repeating until the user chooses to exit.
#code:
a = int(input("Enter the balance amount in bank: "))

while True:
    print("\n----- ATM OPTIONS -----")
    print("1 - Check Balance")
    print("2 - Deposit Money")
    print("3 - Withdrawal")
    print("4 - Exit")

    key = int(input("Enter your choice: "))

    if key == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    elif key == 3:
        w = int(input("Enter amount to withdraw: "))
        if w > a:
            print("Insufficient balance.")
        else:
            a = a - w
            print(f"Withdrawal successful: ₹{w}")
            print(f"Balance amount is: ₹{a}")

    elif key == 2:
        d = int(input("Enter amount to deposit: "))
        if d <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            a = a + d
            print(f"Deposit successful: ₹{d}")
            print(f"Balance amount is: ₹{a}")

    elif key == 1:
        print(f"Your current balance is: ₹{a}")

    else:
        print("Invalid option. Please enter a number between 1 and 4.")
