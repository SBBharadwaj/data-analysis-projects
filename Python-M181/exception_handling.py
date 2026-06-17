#using try and except 

try:
    a=int(input('enter first number:'))
    b=int(input('enter second number:'))
    print(a/b)
except:
    print('not posible')


#value error
try:
    num=int(input('enter the number:'))
    print(num)
except:
    print('invalid input')

#index error
try:
    list=[12,13,45]
    print(list[5])
except:
    print('out of range')

#key_error
try:
    dict={'name':'smith'}
    print(dict[number])
except:
    print('invalid input')

#using try, else , except
try:
    a=int(input('enter first number:'))
    b=int(input('enter second number:'))
    result=a/b
except:
    print('not posible')
else:
    print(result)

#using try, else , except and finally
try:
    a=int(input('enter first number:'))
    b=int(input('enter second number:'))
    result=a/b
except:
    print('not posible')
else:
    print(result)
finally:
    print('execution completed')

#multiple except block
try:
    a=int(input('enter first number:'))
    b=int(input('enter second number:'))
    result=a/b
except ZeroDivisionError:
    print('not posible')
except ValueError:
    print('invalid input')
else:
    print(result)
finally:
    print('execution completed')

#coustom user defined exception
age=int(input('enter your age:'))
if age < 18:
    print('wrong')
    raise Exception('age must be greater than 18')
else:
    print(age)

#ex2
try:
    sal=float(input('enter your sal:'))
    if sal <= 100:
        raise Exception('sal should be greater than 100')
    else:
        print(sal)
except ValueError:
    print('invalid sal')
