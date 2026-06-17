#Ex1
class bank:
    def bank_details(self):
        self.bname='SBI'
        self.branch='JP nagar'
        print(f'bank name is:{self.bname}')
        print(f'bank branch is:{self.branch}')
class customer(bank):
    def cust_details(self):
        self.cname='smith'
        self.job='clerk'
        self.sal=800
        print(f'customer name is:{self.cname}')
        print(f'customer designation is:{self.job}')
        print(f'customer salary is:{self.sal}')
b1=customer()
b1.bank_details()
b1.cust_details()
  
print()


#Ex2
class bank:
    def bank_details(self):
        self.bname='SBI'
        self.branch='JP nagar'
class customer(bank):
    def cust_details(self):
        self.cname='smith'
        self.job='clerk'
        self.sal=800
        print(f'bank name is:{self.bname}')
        print(f'bank branch is:{self.branch}')
        print(f'customer name is:{self.cname}')
        print(f'customer designation is:{self.job}')
        print(f'customer salary is:{self.sal}')
b1=customer()
b1.bank_details()
b1.cust_details()

print()

#Ex3
class employee():
    def __init__(self,ename,sal):
        self.ename=ename
        self.sal=sal
class empdept_details(employee):
    def employee_details(self,job,deptno):
        self.job=job
        self.deptno=deptno
        print(f'employee name is:{self.ename}')
        print(f'employee salary is:{self.sal}')
        print(f'employee job is:{self.job}')
        print(f'employee deptno is:{self.deptno}')
emp=empdept_details('smith',15000)
emp.employee_details('clerk',10)

