#the greatest digit in a given number
num=123
grt=0
while num > 0:
    digit=num%10
    if digit>grt:
        grt=digit
    num//=10
print(grt)

#smalest
num=123
grt=9
while num > 0:
    digit=num%10
    if digit<grt:
        grt=digit
    num//=10
print(grt)

#
str='abcd'
rev=''
for i in str:
    rev=i+rev
print(rev)
#
str='abcd'
rev=''
i=0
while str[i:]:
    rev=str[i]+rev
    i = i+1
print(rev)

#
s='hello'
out=''
count=0
i=0
di={}
while s[i:]:
    if s[i] in 'AEIOUaeiou':
        out=out+s[i]
        count=count+1
    i=i+1
di[out]=count
print(di)

#happy unhappy
n=int(input())
m=n
while n!=1 and n!=4:
    s=0
    while n>0:
        last=n%10
        s=s+last**2
        n//=10
    n=s
if n==1:
    print('happu')
else:
    print('unhappy')