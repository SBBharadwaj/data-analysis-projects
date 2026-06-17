#create a class emp and display
class emp:
    ename='smith'
    sal=800
    deptno=10
    job='clerk'
obj=emp()
print(obj.ename)
print(obj.sal)
print(obj.deptno)
print(obj.job)

#Multiple employee
class employee:
    pass
emp1=employee()
emp1.ename='smith'
emp1.sal=800
emp1.deptno=10
emp1.job='clerk'
emp2=employee()
emp2.ename='martin'
emp2.sal=8000
emp2.deptno=20
emp2.job='salesman'
print(f'first employee name is:{emp1.ename}')
print(f'first employee salary is:{emp1.sal}')
print(f'first employee deptno is:{emp1.deptno}')
print(f'first employee job is:{emp1.job}')
print(f'second employee name is:{emp2.ename}')
print(f'second employee salary is:{emp2.sal}')
print(f'second employee deptno is:{emp2.deptno}')
print(f'second employee job is:{emp2.job}')


#Car example
class car:
    pass
car1=car()
car1.make='mini cooper'
car1.model='s'
car1.color='white'
car1.mileage=12
car2=car()
car2.make='BMW'
car2.model='M3'
car2.color='black'
car2.mileage=15
print(f'car :{car1.make}')
print(f'make :{car1.make}')
print(f'model:{car1.model}')
print(f'mileage:{car1.mileage}')
print(f'car :{car2.make}')
print(f'make :{car2.make}')
print(f'model:{car2.model}')
print(f'mileage:{car2.mileage}')


#EX using class variable and object variable
class employee:
    company_name='QSpider'
    office_location='banglore'
emp1=employee()
emp1.name='Alice'
emp1.sal=12000
emp1.job='SQL developer'
print(f'company:{employee.company_name},location:{employee.office_location}')
print(f'Employee 1:name:{emp1.name},sal:{emp1.sal},')


#Bank example
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


#constructor method
class employee:
    def __init__(self):
        self.ename='smith'
        self.sal=10000
e=employee()
print(e.ename)
print(e.sal)


#emp class using constructor method
class employee:
    def __init__(self,ename,sal,job):
        self.ename=ename
        self.sal=sal
        self.job=job
    def display(self):
        print(self.ename)
        print(self.sal)
        print(self.job)
e1=employee('smith',23000,'clerk')
e1.display()


#ex 3
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'person name:{self.name}')
        print(f'person age:{self.age}')
p=person('smith',23)
p.display()


#bank example
class bank:
    bankname='SBI'
    def __init__(self,name,balance):
        self.name=name
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
        print(f'customer name:{self.name}')
        print(f'Account balance:{self.balance}')
c1=bank('smith',50000)
c1.deposite(10000)
c1.withdraw(8000)
c1.display()