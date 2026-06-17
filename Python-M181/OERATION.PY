class deposite(bankaccount):
    def deposite(self,amount):
        self.balance=self.balance + amount
        print(f'{amount} has been deposited')
        print(f'Updated balance is:{self.balance}')
class withdraw(bankaccount):
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'{amount} is withdrawn')
            print(f'updated balance is:{self.balance}')
        else:
            print('Insufficient balance')