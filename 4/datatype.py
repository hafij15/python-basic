#### Datatypes ####
# In python all datatypes are objects. 
# In python, everything is an objects.
# String, Boolean, Numbers, List, Set, Tuple, Dictionary
# In Dictionary has key value pairs.
"""
name = "Hafijur Rahman"
a = 1
b = 1.3
c = 2+5j
d = True

print(type(name))   # <class 'str'>
print(type(a))      # <class 'int'>    
print(type(b))      # <class 'float'>
print(type(c))      # <class 'complex'>
print(type(d))      # <class 'bool'>

"""
# In set duplicate data is not allowed. 
# List and set can have empty value but tuple must have multiple value. 
"""

li = [1, 1, 2, 3]
s = {1, 1, 2, 2}
t = (1, 2, 3)
d = {'name': 'Hafijur Rahman', 'channel':'Tech Seasons'}

print(type(li))     #<class 'list'>
print(type(s))      #<class 'set'>
print(type(t))      #<class 'tuple'>
print(type(d))      #<class 'dict'>

"""
# Python is Dynamic typing. 
# Static typing is variable has a defined datatype. (int n = 10)
# Dynamic typing not need to declare the data type. (n = 10)
# Python is Strongly typing because cannot concate different type datatypes. Its implicit. 
"""
n = 10
print('Test' +' '+ str(n))

"""

