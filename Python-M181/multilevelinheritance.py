#Ex1
class Bank:
    def __init__(self,bname):
        self.Bname=bname 
class Bankbranch(Bank):
    def branch_details(self,branch):
        self.branch=branch
class Customer(Bankbranch):
    def cust_details(self,cname,balance):
        self.cname=cname
        self.balance=balance
        print(f'Bank name is:{self.Bname}')
        print(f'Bank branch is:{self.branch}')
        print(f'Customer name is:{self.cname}')
        print(f'Bank balance is:{self.balance}')
b=Customer('SBI')
b.branch_details('JP nagar')
b.cust_details('Smith',15000) 

print()

#Ex2
class Employee:
    def __init__(self,ename):
        self.ename=ename
class emp_details(Employee):
    def emp_details(self,sal,job):
        self.sal=sal
        self.job=job
class dept(emp_details):
    def dept_details(self,deptno,dname):
        self.dname=dname
        self.deptno=deptno
        print(self.ename)
        print(self.sal)
        print(self.job)
        print(self.deptno)
        print(self.dname)
emp=dept('Smith')
emp.emp_details(15000,'clerk')
emp.dept_details(10,'sales')


print()

#Ex3
class vehicle:
    def __init__(self,Type):
        self.type=Type
class car(vehicle):
    def car_name(self,carname):
        self.carnamr=carname
class car_details(car):
    def car_info(self,milage,fueltype):
        self.milage=milage
        self.fueltype=fueltype
        print(self.type)
        print(self.carnamr)
        print(self.milage)
        print(self.fueltype)
car=car_details('Four wheel')
car.car_name('BMW')
car.car_info(12,'Petrol')