from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}  

    def create_account(self, acc_no, name, balance=0):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = Account(acc_no, name, balance)
            print("Account created successfully!")

    def deposit_money(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found!")

    def withdraw_money(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found!")

    def check_balance(self, acc_no):
        if acc_no in self.accounts:
            print("Current Balance:", self.accounts[acc_no].balance)
        else:
            print("Account not found!")

    def view_all_accounts(self):
        if not self.accounts:
            print("No accounts available!")
        else:
            for acc in self.accounts.values():
                print(f"Acc No: {acc.acc_no}, Name: {acc.name}, Balance: {acc.balance}")
