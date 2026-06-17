class bank:
    bankname='SBI'
    def details(self,customer,balance):
        self.customer=customer
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f'Amount deposited:{amount}')
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f'Amount withdraw:{amount}')
        else:
            print('Insufficient balance')
    def display(self):
        print(f'Bank name:{self.bankname}')
        print(f'customer name:{self.customer}')
        print(f'Account balance:{self.balance}')
c1=bank()
c1.details('smith',50000)
c1.deposite(10000)
c1.withdraw(8000)
c1.display()