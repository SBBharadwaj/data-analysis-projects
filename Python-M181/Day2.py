import keyword
print (keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword('False'))
print(keyword.iskeyword('false'))
print(keyword.iskeyword('None'))
print(keyword.iskeyword('Ram'))
print(keyword.iskeyword('if'))
print(keyword.iskeyword('for'))
print(keyword.iskeyword('True'))
print(keyword.iskeyword('true'))
print(keyword.iskeyword('for'))
print(keyword.iskeyword('not'))
print(keyword.iskeyword('from'))

#identifier
#syntax:- variable_name.isidentifier()

name='smith'
print('name'.isidentifier())

123name='martin'
print('123name'.isidentifier())
