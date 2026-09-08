Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
2**3
8
4**2
16
a>b
True
a<b
False
a<=b
False
a>=b
True
a==b
False
a!=b
True
c=10
c=c+10
c
20
c=c+20
c
40
c +=10
c
50
c -=10
c
40
c *=10
c
400
c //= 2
c
200
c %=2
c
0
c =100
c
100
c *=3
c
300
c %=3
c
0
c=400
c %=3
c
1
c /=2
c
0.5
True and True
True
True and False
False
n%2==0 and n%3--0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    n%2==0 and n%3--0
NameError: name 'n' is not defined
NameError: name 'n' is not defined
SyntaxError: invalid syntax
n%2==0 and n%3==0
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    n%2==0 and n%3==0
NameError: name 'n' is not defined
n=10
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n
10
n<5
False
not n<5
True
not n>10
True
#str list tuple set dict
s='reena'
'e' in s
True
's' in s
False
'a' not in a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'a' not in a
TypeError: argument of type 'int' is not iterable
'e' not in s
False
's' not in s
True
l=[1,2,3,4,5]
4 in l
True
6 in l
False
3 not in l
False
2 not in l
False
6 not in l
True
t=(1,2,3,4,5)
2 in l
True
2 not in t
False
6 in t
False
6 not in t
True
s={1,2,3,4,5}
2 in s
True
6 in s
False
6 not in s
True
d={name:'reena',batch=63}
SyntaxError: ':' expected after dictionary key
d={name"'reena',batch:63}
   
SyntaxError: unterminated string literal (detected at line 1)
d={name:'reena',batch=63}
   
SyntaxError: ':' expected after dictionary key
d={name:'reena',batch:63}
   
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    d={name:'reena',batch:63}
NameError: name 'name' is not defined
d={'name':'reena','batch':63}
   
name in d
   
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
d
   
{'name': 'reena', 'batch': 63}
'name' in d
   
True
'reena' in d
   
False
'batch' in d
   
True
63 in d
   
False
#key can be searched and checked values cant be
   
'batch' not in d
   
False
l=[1,2,3,4]
   
m=[1,2,3,4]
   
id(l)
   
2870107546880
id(m)
   
2870107543680
l is m
   
False
m is l
   
False
n=l
   
n is l
   
True
n not is l
   
SyntaxError: invalid syntax
n is not l
   
False
l is not m
   
True
#mutable
   
str="reena"
   
id(str)
   
2870107602992
str="reena kowsar"
   
id(str)
   
2870107579632
l=[1,2,3,4,5]
   
id(l)
   
2870107187712
l.add(6)
   
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    l.add(6)
AttributeError: 'list' object has no attribute 'add'
s={1,2,3,4,5}
   
id(s)
   
2870107148064
s.add(6)
   
s
   
{1, 2, 3, 4, 5, 6}
id(s)
   
2870107148064
l=l+10
   
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    l=l+10
TypeError: can only concatenate list (not "int") to list
l.append(7)
   
id(l)
   
2870107187712
#bitwise operators
   
9&10
   
8
9|10
   
11
9^10
   
3
8>>2
   
2
8<<2
   
32
#and  0(00) 0(10) 0(10) 1(11)
   
''' or 0(00) 1(11) 1(01) 1(10)
'''
   
' or 0(00) 1(11) 1(01) 1(10)\n'
#output formating
   
a=10
   
b=10.3
   
c='codegnan'
   
print(a,b,c)
   
10 10.3 codegnan
print("a value is ",a)
   
a value is  10
print("a value is ",a,"b value is ",b,"c value is ",c)
   
a value is  10 b value is  10.3 c value is  codegnan
print(a,b,c,sep='')
   
1010.3codegnan
>>> print(a,b,c,sep= " - ") #seperator
...    
10 - 10.3 - codegnan
>>> print(a,b,c,sep= "\n")
...    
10
10.3
codegnan
>>> print(a,b,c,sep= "\t")
...    
10	10.3	codegnan
>>> print(a,b,c,sep= "\t",end='@')
...    
10	10.3	codegnan@
>>> print(a,b,c,sep= "\t",end='\n\n')
...    
10	10.3	codegnan

>>> print(f'a={a} b={b} c={c}')
...    
a=10 b=10.3 c=codegnan
>>> print('a=%d b=%f c=%s',%(a,b,c))
...    
SyntaxError: invalid syntax
>>> print('a=%d b=%f c=%s'%(a,b,c))
...    
a=10 b=10.300000 c=codegnan
>>> rint('a=%d b=%.2f c=%s'%(a,b,c))
...    
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    rint('a=%d b=%.2f c=%s'%(a,b,c))
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...    
a=10 b=10.30 c=codegnan
>>> print('a={} |b={} | c={}'.format(a,b,c))
...    
a=10 |b=10.3 | c=codegnan
>>> print('a={} |b={} | c={}'.format(c,a,b))
...    
a=codegnan |b=10 | c=10.3
print('a={1} |b={2} | c={3}'.format(a,b,c))
   
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print('a={1} |b={2} | c={3}'.format(a,b,c))
IndexError: Replacement index 3 out of range for positional args tuple
print('a={1} |b={2} | c={0}'.format(a,b,c))
   
a=10.3 |b=codegnan | c=10
