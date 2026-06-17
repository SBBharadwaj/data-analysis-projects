#positional
def add(a,b):
    print(a+b)
add(2,4)

def add(a,b,c):
    print(a*b*c)
add(2,4,6)

def info(name,age):
    print(name,age)
info('smith',21)

#Keyword

def add(a,b):
    print(a+b)
add(b=20,a=10)


def emp(name,sal,job):
    print(name,sal,job)
emp(name='smith',job='clerk',sal=800)


#Default

def emp(ename,sal=800):
    print(ename,sal)
emp('smith')


def emp(ename,sal=800):
    print(ename,sal)
emp('smith',1000)


#Variable length

def display(*num):
    print(num)
display(10,20,30)


def display(*num):
    print(sum(num))
display(10,20,30)


def display(*num):
    print(max(num))
display(10,20,30)


#Variable keyword

def emp(**data):
    print(data)
emp(ename='smith',sal=800)


#All types of arguments together

def emp(empno,ename,sal,
        *mobno,
        job='salesman',
        **details):
    print("employee no:",empno)
    print("employee name:",ename)
    print("salary:",sal)
    print("job:",job)
    print("mobile no.:",mobno)
    print("other details:",details)
emp(101,'smith',50000,1234567890,7894561235,job='clerk',deptno=10)



