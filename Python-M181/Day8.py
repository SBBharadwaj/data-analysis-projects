#set collection datatype
s={10,30,40}
print(s)
print(type(s))


s1={10,20,40,30,50,30}
print(s1)

s2={1,2,[10,20],3,4}
print(s2)


#ex for hetrogeneous 
s3={10,'smith',98.100,98}
print(s3)


#ex for indexing
s4={10,20,30,40}
print(s4[2])


#ex for indexing by converting set collection into list
s={10,20,30,40,50}
li=list(s)
print(li[0])


#Dict. collection datatype
di={'ename':'smith'}
print(di)
print(type(di))

data={'banglore':25,'goa':35,'pune':65}
print(data['banglore'])
print(data['goa'])
print(data['pune'])

emp={'ename':'smith','sal':800}
emp['sal']=980
print(emp)
emp['job']='analyst'
print(emp)

#ex for nested dict.
employees={'emp1':['smith','clerk',9800],
           'emp2':['martin','salesman',8600],
           'emp3':['scott','analyst',9000],
           'emp4':['king','president',5000]
           }
print(employees['emp1'])
print(employees['emp2'])


#ex to add
employees['emp5']=['allen','manager',7500]
print(employees)

#ex to update
employees['emp5'][2]=98000
print(employees)

#ex to delete
del employees['emp5']
print(employees)
 
print(employees.items())
print(employees.keys())
print(employees.values())
