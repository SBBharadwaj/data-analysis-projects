from bank import Bank

# creating object for Bank class to access members of an class  
bank = Bank()

while True:
    print("\n--- Banking System ---")
    print("1. Create Account")  
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no = int(input("Account Number: "))
        name = input("Account Holder Name: ")
        balance = float(input("Initial Balance: "))
        bank.create_account(acc_no, name, balance)

    elif choice == "2":
        acc_no = int(input("Account Number: "))
        amount = float(input("Amount to deposit: "))
        bank.deposit_money(acc_no, amount)

    elif choice == "3":
        acc_no = int(input("Account Number: "))
        amount = float(input("Amount to withdraw: "))
        bank.withdraw_money(acc_no, amount)

    elif choice == "4":
        acc_no = int(input("Account Number: "))
        bank.check_balance(acc_no)

    elif choice == "5":
        bank.view_all_accounts()

    elif choice == "6":
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid choice!")
