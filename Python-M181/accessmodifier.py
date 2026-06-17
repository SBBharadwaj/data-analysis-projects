class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show_details(self):
        print(f'customer name is:{self.name}')
        print(f'bank balance is:{self.balance}')
class customer(bank):
        def display(self):
            self.show_details()
obj=customer('smith',98000)
obj.display()
#outside the class
print(obj.name)
print(obj.balance)

#Ex2
class person:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def greet(self):
          return f'name is {self.name} and age is {self.age}'
obj1=person('smith',30)
print(obj1.name)
print(obj1.age)
obj1.name='allen'
obj1.age=12
print(obj1.name)
print(obj1.age)
print(obj1.greet())

#Ex3
class bank:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
    def _showdetails(self):
        print(f'customer name is:{self._name}')
        print(f'bank balance is:{self._balance}')
class customer(bank):
        def display(self):
            self._showdetails()
obj=customer('smith',98000)
obj.display()
#outside the class
print(obj._name)
print(obj._balance)

#Ex4
class emp:
    def __init__(self):
         self._salary=45000
    def _showdetails(self):
         print(f'salary:{self._salary}')
class manager(emp):
     def display(self):
          print(self._salary)
m=manager()
m.display
        

#Ex5
class bank:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def __showdetails(self):
        print(f'customer name is:{self.__name}')
        print(f'bank balance is:{self.__balance}')
    def accessdetails(self):
         self.__showdetails()
class customer(bank):
        def display(self):
            self.accessdetails()
obj=customer('smith',98000)
obj.display()
#outside the class
print(obj._bank__name)
print(obj._bank__balance)


#Ex
class employee:
     def __init__(self):
          self.__salary=98000
          print(self.__salary)
e=employee()
print(e._employee__salary)