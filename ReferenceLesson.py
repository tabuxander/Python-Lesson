#change string items
name = 'Zophie a cat'
newName = name[0:7] + "the" + name[8:12]

>>> name = 'Zophie a cat'
newName = name[0:7] + "the" + name[8:12]
SyntaxError: multiple statements found while compiling a single statement
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + "the" + name[8:12]
>>> newname
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    newname
NameError: name 'newname' is not defined
>>> newName
'Zophie the cat'
>>> print(newName)
Zophie the cat
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = spam
>>> import copy
>>> cheese = copy.deepcopy(spam)
>>> cheese[1] = 'cheeza'
>>> spam
['A', 'B', 'C', 'D']
>>> cheese[1] = 42
>>> cheese
['A', 42, 'C', 'D']
>>> spam
['A', 'B', 'C', 'D']
>>> myCat = ['size': 'fat', 'color': 'gray', 'disposition': 'loud']
SyntaxError: invalid syntax
>>> 
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat[color]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    myCat[color]
NameError: name 'color' is not defined
>>> myCat['color']
'gray'
>>> 'My Cat has ' + myCat['color'] + 'furry fur'
'My Cat has grayfurry fur'
>>> spam = { 12345: 'Luggage combination', 42: 'The Answer'}
>>> eggs = {'name' : 'my girl', 'species' = 'cat' , 'age' : 8}
SyntaxError: invalid syntax
>>> eggs = {'name' : 'my girl', 'species' : 'cat' , 'age' : 8}
>>> spam = { 'species' : 'cat', 'name' : 'my girl' , 'age' : 8}
>>> eggs == spam
True
>>> 'name' in eggs
True
>>> eggs
{'name': 'my girl', 'species': 'cat', 'age': 8}
>>> list.eggs(keys())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list.eggs(keys())
AttributeError: type object 'list' has no attribute 'eggs'
>>> list(eggs.keys())
['name', 'species', 'age']
>>> list(eggs.value())
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(eggs.value())
AttributeError: 'dict' object has no attribute 'value'
>>> list(eggs.values())
['my girl', 'cat', 8]
>>> list(eggs.items())
[('name', 'my girl'), ('species', 'cat'), ('age', 8)]
>>> eggs.keys()
dict_keys(['name', 'species', 'age'])
>>> for k in eggs.keys():
	print(k)

	
name
species
age
>>> for i in eggs.key():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for i in eggs.key():
AttributeError: 'dict' object has no attribute 'key'
>>> for m in eggs.keys():
	print(m)

	
name
species
age
>>> for o, x in eggs.items():
	print(o, x)

	
name my girl
species cat
age 8
>>> 'cat' in eggs.values()
True
>>>  eggs['color']
 
SyntaxError: unexpected indent
>>> eggs['color']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    eggs['color']
KeyError: 'color'
>>> eggs['age']
8
>>> if 'color' in eggs:
	print(eggs['color'])

	
>>> eggs.get('age', 0)
8
>>> eggs.get('color', 'you sucks')
'you sucks'
>>>  picnicItems = {'apples' : 5, 'banana' : 7, 'bread' : 3}
 
SyntaxError: unexpected indent
>>> picnicItems = {'apples' : 5, 'banana' : 7, 'bread' : 3}
>>> print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic')
I am bringing 0 to the picnic
>>> eggs
{'name': 'my girl', 'species': 'cat', 'age': 8}
>>> if 'color' not in eggs:
	eggs['color'] = 'black'

	
>>> eggs
{'name': 'my girl', 'species': 'cat', 'age': 8, 'color': 'black'}
>>> eggs['color']
'black'
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'my girl', 'species': 'cat', 'age': 8, 'color': 'black'}
>>> 
