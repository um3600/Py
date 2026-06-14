# ATM Machine Simulation

pin = 1234
balance = 50000

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("\nWelcome Umar bank Limited ATM")
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")

    choice = int(input("\nEnter choice: "))

    if choice == 1:
        print(f"\nYour current balance is: Rs. {balance}")

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
        else:
            balance += amount
            print(f"Deposit successful.")
            print(f"Updated balance: Rs. {balance}")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > balance:
            print("Insufficient Balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful.")
            print(f"Remaining balance: Rs. {balance}")

    elif choice == 4:
        old_pin = int(input("Enter old PIN: "))

        if old_pin != pin:
            print("Incorrect old PIN.")
        else:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN must be exactly 4 digits.")
            elif int(new_pin) == pin:
                print("New PIN cannot be the same as old PIN.")
            else:
                pin = int(new_pin)
                print("PIN changed successfully.")

    else:
        print("Invalid option. Please choose a valid menu option.")

else:
    print("Wrong PIN. Access Blocked.")
