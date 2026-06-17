#Numbers from 1 to 10
a=1
while a<=10:
    print(a)
    a=a+1

#Numbers from 5 to 1
a=5
while a>=1:
    print(a)
    a=a-1

#Even numbers from 1 to 10
a=1
while a<=10:
    if a%2==0:
        print(a)
    a=a+1
      
        #or

a=2
while a<=10:
    print(a)
    a=a+2

#Odd numbers from 1 to 9
a=1
while a<=10:
    if a%2!=0:
        print(a)
    a=a+1

#Hello python 6 times
a=1
while a<=6:
    print('Hello Python', a)
    a=a+1

#Table of 4
a=1
while a<=10:
    print(a*4)
    a=a+1


#Tables of given number
a=1
num=int(input('Enter the number'))
while a<=10:
    print(num*a)
    a=a+1

#sum of numbers from 1 to 6
a=1
total=0
while a<=6:
    total=total+a
    a=a+1
print(total)

#sum of even numbers from 1 to 6
a=1
total=0
while a<=6:
    if a%2==0:
        total=total+a
    a=a+1
print(total)

#Factorial of a number 5
a=int(input('Enter a number'))
fact = 1
while a>0:
    fact=fact*a
    a=a-1
print(fact)

#To check prime number
num=5
i=2
count=0
while i<num:
    if num % i==0:
        count=count+1
    i=i+1
if count==0 and num>1:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

#To check Armstrong number
num=153
temp=num
sum_cubes=0
while num>0:
    digit=num%10
    sum_cubes=sum_cubes+digit**3
    num=num//10
if temp==sum_cubes:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#To check Neon number
num=9
square=num*num
sum_digits=0
temp=square
while temp>0:
    digit=temp%10
    sum_digits+=digit
    temp=temp//10
if sum_digits==num:
    print("Neon number")
else:
    print("Not an Neon number")

#To check spy number
num=1124
sum=0
prod=1
while num>0:
    digit=num%10
    sum=sum+digit
    prod=prod*digit
    num=num//10
if sum==prod:
    print("Spy number")
else:
    print("Not a Spy number")

#To check perfect number
num = 6
i = 1
sum = 0
while i < num:
    if num % 1 == 0:
        sum = sum+i
    i = i + 1
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")