# # d={'a':1,'b':2,'c':3,'d':4}
# # d2=d.copy()
# # p={}
# # while d:
# #     k,v=d.popitem()
# #     p[k]=v
# # print(p)
# # print(d2)

# # if (a:=input('enter a name : ')) !='quit':
# #     print(a)

# # while (a:=input()) !='quit':
# #     print(a)


# #WAP to print mul of 18th table
# # a=1
# # num=18
# # while a<=10:
# #     print(num*a)
# #     a=a+1

# # num=18
# # for i in range(1,11):
# #     print(i*num)



# # while (a:=int(1) num:=int(18)) a<=10:
# #     print(num*a)
# #     a=a+1 

# #WAP to fetch and store all the vowel from given string
# # a=('python')
# # b=('')
# # i=0
# # while i<len(a):
# #     if a[i] in 'AEIOUaeiou':
# #         b=b+a[i]
# #     i=i+1
# # print(b)


# #WAP to add all even numbers prest in a list
# #1
# a=[23,24,54,53,23,5,6,7,3,2,6,3,'vghda']
# i=0
# b=[]
# sumof=0
# while i<len(a):
#     if (str(a[i]).isdigit()):
#         if a[i]%2==0:
#             b.append(a[i])
#             sumof=sumof+int(a[i])
#     i=i+1
# print(b,sumof)
# #2
# a=[23,24,54,53,23,5,6,7,3,2,6,3,'vghda']
# i=0
# sumof=0
# while i<len(a):
#     if type(a[i]==int) and a[i]&1==0:
#         sumof+=a[i]
#     i+=1
# print(sumof)


# a=input('enter your email:')
# i=0
# upp=('')
# low=('')
# spc=('')
# dig=0
# while i<len(a):
#     if a[i] in 

#list
# a=[12,435,546,6,756]
# small=a[0]
# large=a[0]
# for i in a:
#     if i<small:
#         small=i
#     elif i>large:
#         large=i
# print(small)
# print(large)

# a=[12,435,546,6,756]
# print(sum(a))
#or
# a=[12,435,546,6,756]
# s=0
# for i in a:
#     s=s+i
# print(s)

# a=[12,12,435,546,6,6,756]
# res=[]
# for i in a:
#     if i not in res:
#         res.append(i)
# print(res)

# a=[12,12,435,546,6,6,756]
# res={}
# for i in a:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# print(res)

# a=[12,435,546,6,756]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)

# a=[12,435,546,6,756]
# eve=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         eve.append(i)
#     else:
#         odd.append(i)
# print(eve)
# print(odd)


# a=[12,435,546,6,756,756]
# c=list(set(a))
# d=sorted(c)
# print(d[-2])

# a=[12,435,546,6,756,756]
# b=[23,53,57,78,45,56]
# res=[]
# for i in a:
#     for j in b:
#         res.append(i+j)
#         break
# print(res)


# a=[12,435,546,6,756,756]
# b=[23,53,57,78,45,56]
# a.extend(b)
# print(a)


# a=[]
# while True:
#     b=input('enter your number:')
#     if b=='quit':
#         print(a)
#         break
#     a.append(b)
#     print(a)



#pattern prog
# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i+j<=6:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i+j>=6:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i+j==6:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==1 or i==5 or j==5:
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==1 or i==5 or j==5:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i+j==6 or i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i==3 or j==3 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if (i+j)%2==0:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,10):
#         if i+j==6 or i==5 or i+4==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# for i in range(0,6):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()
# for i in range(4,0,-1):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()


# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()
# for i in range(0,6):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()


#inheritance
class demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def disp(self):
        print(self.a,self.b)
class child(demo):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
class child2(child):
    def __init__(self,e,f,a,b,c,d):
        super().__init__(a,b,c,d)
        self.e=e
        self.f=f
    def dis(self):
        print(self.e,self.f)
obj=child2(1,2,3,4,5,6)
obj.dis

