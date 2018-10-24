Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
str2 = "there"
abc = str1 + str2
print(abc)
>>> str1 = "Happy"
>>> str2 = "holiday"
>>> ABC = str1 + str2
>>> print(ABC)
Happyholiday
>>> str3 = '189'
>>> str3 = str3 + 25

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str3 = str3 + 25
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) + 25
>>> print(x)
214
>>> name = input('Enter:')
Enter:Konnor

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Konnor' is not defined
>>> name = input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> name = raw_input('Enter:')
Enter:Chuck
>>> print(name)
Chuck
>>> orange = raw_input('Enter:')
Enter:326
>>> x = orange - 137

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x = orange - 137
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(orange) - 137
>>> print(x)
189
>>> fruit = 'orange'
>>> letter = fruit[1]
>>> print(letter)
r
>>> x = 4
>>> w = fruit[x -1]
>>> print(w)
n
>>> fruit = 'orange'
>>> print(len(fruit))
6
>>> 
