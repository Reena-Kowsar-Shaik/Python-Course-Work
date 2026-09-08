Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> a,b,c=10,20,30
>>> c
30
>>> a=b=c=10
>>> b
10
>>> a,b=b,a
>>> b
10
>>> s=1
>>> r=1
>>> s+r
2
>>> del r
>>> r
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    r
NameError: name 'r' is not defined
>>> myvar=30
>>> myvae
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myvae
NameError: name 'myvae' is not defined. Did you mean: 'myvar'?
>>> myvar
30
