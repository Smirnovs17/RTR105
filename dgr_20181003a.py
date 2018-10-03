Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> a=2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 2, '__package__': None}
>>> b=4
>>> vars()
{'a': 2, 'b': 4, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(input("Ievads: "))
Ievads: 36
<type 'int'>
>>> vars(a)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    vars(a)
TypeError: vars() argument must have __dict__ attribute
>>> a * b
8
>>> 5.48
5.48
>>> type(input("Ievads:"))
Ievads:7.48
<type 'float'>
>>> ddddd

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ddddd
NameError: name 'ddddd' is not defined
>>> type(raw_input("Ievads:"))
Ievads:dddddd
<type 'str'>
>>> type(a)
<type 'int'>
>>> print

>>> eeeee = a * b
>>> print

9
>>> print(eeeee)
8
>>> fff = 'hello''+ 'there'
SyntaxError: invalid syntax
>>> print(fff)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(fff)
NameError: name 'fff' is not defined
>>> fff = 'hello'
>>> print(fff)
hello
>>> print(fff*2)
hellohello
>>> 
