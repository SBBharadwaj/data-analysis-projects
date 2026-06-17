#Tuple datatype
t1=(10,20,30,40,50)
print(type(t1))

t2=('smith',30,True,8.24)
print(t2)

t3=(25,)
print(type(t3))

#tuple datatype is immutable
t=(100,200,300)
t[1]=800
print(t)


#indexing in tuple
t4=(900,100,300,500,600,500)
print(t4[0])
print(t4[1])
print(t4[2])
print(t4[5])
print(t4[3])
print(t4[6])
print(t4[7])

#sliceing in tuple
t5=(900,100,300,500,600,500)
print(t5[::])
print(t5[0:5:1])
print(t5[2:6:1])
print(t5[6:1:1])
print(t5[0::2])
print(t5[2::2])
print(t5[1::2])
print(t5[::-1])
print(t5[::-2])
print(t5[-2::-2])
print(t5[-1::-2])

#Nested tuple
t=(1,(10,20,30),98,100)
print(type(t))


#Tuple is mutable
t6=(1,2,[90,75,30],3,4)
t6[2][1]=300
print(t6)

