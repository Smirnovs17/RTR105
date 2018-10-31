Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> fhand = open('mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fhand = open('mbox-short.txt')
IOError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> inp = fhand.read()

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    inp = fhand.read()
NameError: name 'fhand' is not defined
>>> print(len(inp))

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(len(inp))
NameError: name 'inp' is not defined
>>> print(inp[:20])

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(inp[:20])
NameError: name 'inp' is not defined
>>> xfile = open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    xfile = open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> stuff = ('Hello\nMy\nFriend')
>>> print(stuff)
Hello
My
Friend
>>> fhand = open('mbox.txt','r')
>>> xfile = open('mbox.txt')
>>> print(cheese)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(cheese)
NameError: name 'cheese' is not defined
>>> fhand = open('mbox.txt')
>>> count = 0
>>> count = count + 1
>>> print('Line Count:',count)
('Line Count:', 1)
>>> open('mbox.txt')
<open file 'mbox.txt', mode 'r' at 0x7fe91df34e40>
>>> open('mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    open('mbox-short.txt')
IOError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
6
>>> print(inp[:20])
Hello

>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.startswith('From:'):
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	print(line)

	
>>> fhand = opem('mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    fhand = opem('mbox-short.txt')
NameError: name 'opem' is not defined
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not '@utc.ac.za' in line:
		continue
	print(line)

	
>>> fname = input('Enter the file name:')
Enter the file name:mbox.txt

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    fname = input('Enter the file name:')
  File "<string>", line 1, in <module>
NameError: name 'mbox' is not defined
>>> fhand = open(fname)

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    fhand = open(fname)
NameError: name 'fname' is not defined
>>> fname = input('Enter the file name:')
Enter the file name:mbox-short.txt

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fname = input('Enter the file name:')
  File "<string>", line 1, in <module>
NameError: name 'mbox' is not defined
>>> 
