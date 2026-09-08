Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,12,324,654,65,23423}
s
{1, 2, 3, 324, 4, 65, 12, 654, 23423}
s=set()

s
set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s
{1, 12.3, (2+4j)}
s={1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
{2}<=a
True
{5}<=b
True
a>={3,4,5}
True
{1,2,3,4,5}<=1
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    {1,2,3,4,5}<=1
TypeError: '<=' not supported between instances of 'set' and 'int'
{1a2,3,4,5}<=1
SyntaxError: invalid decimal literal
{1,2,3,4,5}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
3 in a
True
10 in b
False
max(a)
5
min(a)
1
soretd(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    soretd(a)
NameError: name 'soretd' is not defined. Did you mean: 'sorted'?
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update([45,66,77])
a
{1, 2, 3, 4, 5, 66, 12, 77, 45, 123}
a.pop()
1
a
{2, 3, 4, 5, 66, 12, 77, 45, 123}
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a.remove(77)
a
{2, 3, 4, 5, 66, 12, 45, 123}
a.remove(100)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.remove(100)
KeyError: 100
a.discard(4)
a
{2, 3, 5, 66, 12, 45, 123}
a.discard(125)
a
{2, 3, 5, 66, 12, 45, 123}
a.clear()
a
set()
a={1,2,3,4,5,'str',12,13,-1}
len(a)
9
all(a)
True
any(a)
True
a=frozenset({1,12,13,10,16,59,20})
a
frozenset({16, 1, 20, 10, 59, 12, 13})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}

d
{}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2704855721664
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+3j]='com'
d
{1: 'int', 12.3: 'float', (2+3j): 'com'}
d['str']='string'
d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d={}
d[1]=1
d[2]=12.21
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3,4]
>>> d[6]=(1,2,3)
>>> d[7]=(1,2,3)
>>> d[8}={1:1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.21, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: (1, 2, 3), 8: {1: 1}, 9: True}
>>> 9 ind
SyntaxError: invalid syntax
>>> 9 in d
True
>>> 10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(12.21)
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d
{1: 1, 2: 12.21, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: (1, 2, 3), 8: {1: 1}, 9: True}
>>> d[3]=4
>>> d
{1: 1, 2: 12.21, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: (1, 2, 3), 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.21, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: 20, 8: {1: 1}, 9: True}
