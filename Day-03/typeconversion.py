Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
doct(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    doct(a)
NameError: name 'doct' is not defined. Did you mean: 'oct'?
dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=1.0
int(b)
1
complex(b)
(1+0j)
str(b)
'1.0'
list(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
com=1+2j
int(com)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(com)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(complex)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(complex)
TypeError: float() argument must be a string or a real number, not 'type'
str(com)
'(1+2j)'
list(com)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(com)
TypeError: 'complex' object is not iterable
tuple(com)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(com)
TypeError: 'complex' object is not iterable
set(com)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(com)
TypeError: 'complex' object is not iterable
dict(com)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(com)
TypeError: 'complex' object is not iterable
c="reena"
int(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'reena'
float(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: 'reena'
complex(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
list(c)
['r', 'e', 'e', 'n', 'a']
tuple(c)
('r', 'e', 'e', 'n', 'a')
set(c)
{'n', 'e', 'a', 'r'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(c)
True
>>> bool(com)
True
>>> l=[1,2,3,4,5,'sra',4,5]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(l)
"[1, 2, 3, 4, 5, 'sra', 4, 5]"
>>> tuple(l)
(1, 2, 3, 4, 5, 'sra', 4, 5)
>>> set(l)
{1, 2, 3, 4, 5, 'sra'}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> bool(com)
True
>>> t=(1,2,3,4,5)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(l)
"[1, 2, 3, 4, 5, 'sra', 4, 5]"
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s1={1,2,3,4,5}
str(s1)
'{1, 2, 3, 4, 5}'
list(s1)
[1, 2, 3, 4, 5]
tuple(s1)
(1, 2, 3, 4, 5)
bool(s1)
True
d={1:"reena",2:"lot"}
int(d)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
list(d)
[1, 2]
tuple(d)
(1, 2)
set(d)
{1, 2}
dict(d)
{1: 'reena', 2: 'lot'}
bool(d)
True
str(d)
"{1: 'reena', 2: 'lot'}"
t=True
int(t)
1
float(t)
1.0
list(t)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    list(t)
TypeError: 'bool' object is not iterable
set(t)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    set(t)
TypeError: 'bool' object is not iterable
tuple(t)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tuple(t)
TypeError: 'bool' object is not iterable
str(t)
'True'
