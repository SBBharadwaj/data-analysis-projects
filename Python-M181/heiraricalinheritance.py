#Ex1
class bankaccount:
    def __init__(self,cname,accno,balance):
        self.cname=cname
        self.accno=accno
        self.balance=balance
        print(f'Customer name is:{self.cname}')
        print(f'Account number is:{self.accno}')
        print(f'Bank balance is:{self.balance}')
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
b=deposite('smith',123,15000)
b.deposite(5000)
print()
bb=withdraw('martin',456,15000)
bb.withdraw(3000)

print()

#Ex2
class employee:
    def __init__(self,salary):
        self.salary=salary
        print(f'Employee salary is:{self.salary}')
        print(f'Employee bonus is:{self.salary * 0.10}')
class developer(employee):
    def get_bonus(self, salary):
        self.salary=salary
        print(f'developer bonus is:{self.salary * 0.30}')
class manager(employee):
    def get_bonus(self, salary):
        self.salary=salary
        print(f'manager bonusnis:{self.salary*0.60}')
d1=developer(10000)
d1.get_bonus(65000)
m1=manager(100)
m1.get_bonus(75000)

print()

#Ex3
class bankaccount:
    def __init__(self,cname,accno,balance):
        self.cname=cname
        self.accno=accno
        self.balance=balance
        print(f'Customer name is:{self.cname}')
        print(f'Account number is:{self.accno}')
        print(f'Bank balance is:{self.balance}')
class deposite(bankaccount):
    def __init__(self, cname, accno, balance):
        super().__init__(cname, accno, balance)
    def deposite(self,amount):
        self.balance=self.balance + amount
        print(f'{amount} has been deposited')
        print(f'Updated balance is:{self.balance}')
        return self
class withdraw(bankaccount):
    def __init__(self, cname, accno, balance):
        super().__init__(cname, accno, balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'{amount} is withdrawn')
            print(f'updated balance is:{self.balance}')
        else:
            print('Insufficient balance')
        return self
b=deposite('smith',123,15000)
b.deposite(5000)
print()
bb=withdraw('martin',456,15000)
bb.withdraw(3000)

