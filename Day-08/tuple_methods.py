Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=()
>>> t=(10,)
>>> t
(10,)
>>> a=(1,2)
>>> b=(3,4)
>>> print(a+b)
(1, 2, 3, 4)
>>> print(a*3)
(1, 2, 1, 2, 1, 2)
>>> data=(10,20,30,40)
>>> print(data[0])
10
>>> print(data[-1])
40
>>> data=(10,20,30,40,50)
>>> print(data[1:4])
(20, 30, 40)
>>> print(data[::-1])
(50, 40, 30, 20, 10)
>>> print(20 in data)
True
>>> print(10 not in data)
False
>>> len(data)
5
>>> max(data)
50
>>> min(data)
10
>>> sum(data)
150
>>> sorted(data)
[10, 20, 30, 40, 50]
>>> tuple(data)
(10, 20, 30, 40, 50)
>>> any((0,0,1))
True
>>> all((0,0,1,1))
False
data.count(10)
1
data.index(20)
1
data=10,20,30
print(data)
(10, 20, 30)
data=(10,20,30)
a,b,c=data
a
10
b
20
c
30
data=((1,2),(3,4))
print(data[0])
(1, 2)
print(data[1][1])
4
data=(10,20,30)
data[0]=100
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    data[0]=100
TypeError: 'tuple' object does not support item assignment
data=(10,20,[30,40,50],60)
data[2].append(70)
data
(10, 20, [30, 40, 50, 70], 60)
