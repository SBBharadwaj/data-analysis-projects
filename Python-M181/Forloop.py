#Natural numbers from 1 to 10
for i in range(1,11):
    print(i)

#Even numbers from 1 to 20
for i in range(2,21,2):
    print(i)

#Odd numbers from 1 to 20
for i in range(1,21,2):
    print(i)

#Sum of 1st 10 natural numbers
total=0
for i in range(1,11):
    total=total+i
print(total)

#Sum of even digit number from 1 to 10
total=0
for i in range(2,11,2):
    total=total+i
print(total)

#Square of starting 5 numbers
for i in range(1,6):
    print(i*i)

#Cube of starting 5 numbers
for i in range(1,6):
    print(i**3)

#Multiplication table of an number
num=5
for i in range(1,11):
    print(f'{num}*{i}={i*num}') 

#Number of digits in given number
num=23456
count=0
for i in str(num):
    count=count+1
print(count)

#Reverse a number
num=123
rev=' '
for i in str(num):
    rev=i+rev
print(rev)

#To check palindrome
num=121
rev=''
for i in str(num):
    rev=rev+i
if int(rev)==num:
    print('palindrome')
else:
    print('not an palindrome')

#Print all items in the list
fr=["apple","banana","orange"]
for fr in fr:
    print(fr)

#Else block with an forloop
for i in range(3):
    print(i)
else:
    print('loop finished')

#Print each institute from a list
inst=["Pyspider","Qspider","Jspider"]
for inst in inst:
    print(inst)

#Print each char. in a string
subject='python'
for sub in subject:
    print(sub)

#Print number from 1 to 8 are even or odd
for i in range(1,9):
    if i%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

#Factorial of a number(1 to 5)
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)