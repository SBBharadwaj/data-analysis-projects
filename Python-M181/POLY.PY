class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposite (self,amount):
        if amount < 0:
            raise ValueError("must  greater than 0")
        self.balance += amount
        print(f'Deposited:{amount} to {self.name} account. new balance:{self.balance}')
    def withdraw(self,amount):
        if self.balance < amount:
            raise ValueError('insufficient fund')
        self.balance -= amount
        print(f'withdrawn:{amount} from {self.name} account, new balance {self.balance}')
class savingsbank(bank):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def withdraw(self,amount):
        if amount > 10000:
            raise ValueError('maximum limit is 10000')
        super().withdraw(amount)
c1=bank('smith',10000)
c2=savingsbank('martin',20000)
c1.deposite(5000)
c2.withdraw(5000)
c1.withdraw(15000)
try:
    c2.withdraw(15000)
except ValueError as e:
    print(f'error in saving account{e}')
c2.withdraw(8000)