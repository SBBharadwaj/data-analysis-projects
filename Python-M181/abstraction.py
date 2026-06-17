#Ex1
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print('car start with key')
obj=car()
obj.start()

print()
#Ex2
from abc import ABC, abstractmethod
class bank(ABC):
    @abstractmethod
    def deposite(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class SBI(bank):
    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} has been deposited')
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance=self.balance - amount
            print(f'{amount} has been debited')
        else:
            print('invalid amount')
    def check_balance(self):
        print(f'Bank balance is:{self.balance}')
amount=SBI()
amount.deposite(5000)
amount.withdraw(1000)
amount.check_balance()

print()
#Ex3
from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def show_details(self):
        pass
class developer(employee):
    def __init__(self,ename,salary,job):
        self.ename=ename
        self.salary=salary
        self.job=job
    def show_details(self):
        print(f'employee name:{self.ename}')
        print(f'employee salary:{self.salary}')
        print(f'employee job:{self.job}')
emp=developer('smith',98000,'analyst')
emp.show_details()