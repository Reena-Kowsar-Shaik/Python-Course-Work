Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
count=10
count
10
type(count)
<class 'int'>
cost=90.8
cost
90.8
type(cost)
<class 'float'>
com=6+8j
com
(6+8j)
type(com)
<class 'complex'>
s="Reena"
s
'Reena'
type(s)
<class 'str'>
l=[]
l1=[1,2,3,4,asd,54,98]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l1=[1,2,3,4,asd,54,98]
NameError: name 'asd' is not defined
l1=[1,2,3,4,"qw","asdfg"]
l1
[1, 2, 3, 4, 'qw', 'asdfg']
type(1)
<class 'int'>
type(l1)
<class 'list'>
t=()
t1=()
t2=(1,2,3,4,5)
t2
(1, 2, 3, 4, 5)
>>> t3=(1,2,3,"asdf",5)
>>> t3
(1, 2, 3, 'asdf', 5)
>>> type(t3)
<class 'tuple'>
>>> #mapping
>>> s=set()
>>> 
>>> type(s)
<class 'set'>
>>> s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> d=
SyntaxError: invalid syntax
>>> d={1:'reena',2:'ram'}
>>> d
{1: 'reena', 2: 'ram'}
>>> type(d)
<class 'dict'>
>>> s='True'
>>> s
'True'
>>> type(s)
<class 'str'>
>>> s=True
>>> s
True
>>> type(s)
<class 'bool'>
>>> s=None
>>> type(s)
<class 'NoneType'>
>>> s={1,2,3,4,5}
>>> s1=frozenset(s)
>>> s1
frozenset({1, 2, 3, 4, 5})
>>> type(s1)
<class 'frozenset'>
