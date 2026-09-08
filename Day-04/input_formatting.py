Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=input()
123456
x
'123456'
name=input()
reena
name
'reena'
name=input("enter your name:")
enter your name:kowsar
name
'kowsar'
values=int(input("enter a number"))
enter a number23
values
23
values=int(input("enter numbers:")
3 4 5 6
           
SyntaxError: '(' was never closed
values=int(input("enter numbers:"))
           
enter numbers:3 4 5
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    values=int(input("enter numbers:"))
ValueError: invalid literal for int() with base 10: '3 4 5'
type(values)
           
<class 'int'>
values=input()
           
1 2 3
values
           
'1 2 3'
names=input("enter names:")
           
enter names:reena
names=input("enter names:")

           
enter names:kowsar
names
           
'kowsar'
names=input()
           
reena kowsar
names
           
'reena kowsar'
names.split()
           
['reena', 'kowsar']
names=input("entr the names:").split()
           
entr the names:1 2 3 4 5 67
names
           
['1', '2', '3', '4', '5', '67']
map(int,names)
           
<map object at 0x00000285475DD270>
list(map(int,names))
           
[1, 2, 3, 4, 5, 67]
values=list(map(int,input().split()))
           
1 2 3 4 5 6 78
values
           
[1, 2, 3, 4, 5, 6, 78]
t=input().split()
           
1 2 3 4 5 6
t
           
['1', '2', '3', '4', '5', '6']
map(int,t)
           
<map object at 0x00000285475DDE10>
tuple(map(int,t))
           
(1, 2, 3, 4, 5, 6)
t1=tuple(map(int,input().split()))
           
1 23 4 4 55 6765
t1
           
(1, 23, 4, 4, 55, 6765)
t2=tuple(map(float,input().split()))
           
4.0 5.0 6.0 5 7
t2
           
(4.0, 5.0, 6.0, 5.0, 7.0)
s1=input().split()
           
3 4 5 4 6
s1
           
['3', '4', '5', '4', '6']
map(int,s1)
           
<map object at 0x00000285475DF160>
set(map(int,s1))
           
{3, 4, 5, 6}
s2=set(map(in,input().split()))
           
SyntaxError: invalid syntax
s2=set(map(int,input().split()))
           
1 2 3 4 5 6 3 4
s2
           
{1, 2, 3, 4, 5, 6}
s3=set(map(float,input().split()))
           
1 2 3 4 5 6
s3
           
{1.0, 2.0, 3.0, 4.0, 5.0, 6.0}
a,b=[1,2]
           
a
           
1
b
           
2
a,b=(1,2)
           
a
           
1
b
           
2
email,password=input("enter the email and password").split()
           
enter the email and passwordreena@gmail.com
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    email,password=input("enter the email and password").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("enter the email and password").split()
           
enter the email and passwordreena@gmail.com 123456
email
           
'reena@gmail.com'
password
           
'123456'
a,b,c=list(map(int,input().split()))
           
1 2 3
a
           
1
b
           
2
c
           
3
name,marks=input().split()
           
nmae
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    name,marks=input().split()
ValueError: not enough values to unpack (expected 2, got 1)
names
           
['1', '2', '3', '4', '5', '67']
name
           
'kowsar'
name,marks=input().split()
           
reena 70
name
           
'reena'
marks
           
'70'
int(marks
    )
           
70
>>> e=eval(input())
...            
3
>>> e
...            
3
>>> e=eval(input())
...            
reena
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'reena' is not defined
>>> e=eval(input())
...            
"reena"
>>> e
...            
'reena'
>>> e=eval(input()
...        [1,2,3,4,5]
...        e
...        
SyntaxError: '(' was never closed
>>> e=eval(input())
...        
[1 2 3 4 5]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    [1 2 3 4 5]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> e=eval(input())
...        
[1,2,3,4,5]
>>> e
       
[1, 2, 3, 4, 5]
e=eval(input())
       
(1,2,3,3,4)
e
       
(1, 2, 3, 3, 4)
e=eval(input())
       
{1:'reena',2:'kowsar}
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    {1:'reena',2:'kowsar}
                 ^
SyntaxError: unterminated string literal (detected at line 1)
e=eval(input())
     
e=eval(input())
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    e=eval(input())
     ^
SyntaxError: invalid syntax
l=eval(input())
     
{1:'reena',2:'kowsar'}
l
     
{1: 'reena', 2: 'kowsar'}
