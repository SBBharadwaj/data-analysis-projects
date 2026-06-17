#String methods in python

#1) Upper()

s1='python'
print(s1.upper())

#2) Lower()
s1='PYTHON'
print(s1.lower())

#3) title()
s1='python'
print(s1.title())

#4) Capitalized()
s1='python world'
print(s1.capitalize())

#5)Swapcase()
s1='heLLo pYtHoN'
print(s1.swapcase())

#6)length()
s1='python'
print(len(s1))

#7)Strip()
s1='  python  '
print(s1.strip())

#8)lstrip()
s1='  python  '
print(s1.lstrip())

#9)rstrip()
s1='  python  '
print(s1.rstrip())

#10)Startwith()
s1='python'
print(s1.startswith('p'))
print(s1.startswith('py'))
print(s1.startswith('yt'))
print(s1.startswith('P'))

#11)endswith()
s1='python'
print(s1.endswith('p'))
print(s1.endswith('n'))
print(s1.endswith('on'))
print(s1.endswith('N'))

#12)find()
s1='python'
print(s1.find('p'))
print(s1.find('y'))
print(s1.find('t'))
print(s1.find('n'))
print(s1.find('h'))
print(s1.find('o'))
print(s1.find('j'))

#13)Index()
s1='python'
print(s1.index('p'))
print(s1.index('n'))
print(s1.index('j'))

#Example
s1='welcome to english class'
first=s1.index('e')
print(first)
second=s1.index('e',first+2)
print(second)


li=range(10)
print(list(li))