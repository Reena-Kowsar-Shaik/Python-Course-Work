Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='strings.py'
c.startswith('python')
False
c.startswith('str')
True
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'PYTHONV13'.isupper()
True
c.isalpha()
False
c.isalnum()
False
'    '.isspace()
True
'ree    '.isspace()
False
'this is title'.istitle()
False
This Is Title.istitle()
SyntaxError: invalid syntax
'This Is Title'.istitle()
True
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> l=[]
>>> l=list()
>>> l=[1,2.5,2+3j,'str',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3}]
>>> l
[1, 2.5, (2+3j), 'str', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2, 3: 3}]
>>> l=[1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4,5]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4, 5]
>>> l
[1, 2, 3, 4, 5]
>>> l[3]
4
>>> l[-1]
5
>>> l[1:]
[2, 3, 4, 5]
>>> l[::-1]
[5, 4, 3, 2, 1]
>>> 4 in l
True
>>> 5 in l
True
>>> 6 not in l
True
