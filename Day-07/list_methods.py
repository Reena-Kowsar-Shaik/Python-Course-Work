Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l1=[10,9,6,1,2,3,4]
l1
[10, 9, 6, 1, 2, 3, 4]
id(l)
2814839513088
l.append(12)
l
[1, 2, 3, 4, 5, 12]
id(l)
2814839513088
l.insert(1,13)
l
[1, 13, 2, 3, 4, 5, 12]
l.extend([10,20,30])
l
[1, 13, 2, 3, 4, 5, 12, 10, 20, 30]
id(l)
2814839513088
l[3]=40
l
[1, 13, 2, 40, 4, 5, 12, 10, 20, 30]
l.pop()
30
l.pop()
20
l.remove(4)
l
[1, 13, 2, 40, 5, 12, 10]
del l[1]
l
[1, 2, 40, 5, 12, 10]
l.clear()
l
[]
l=[12,34,56,77,99]
max(l)
99
min(l)
12
sorted(l)
[12, 34, 56, 77, 99]
l.revers()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    l.revers()
AttributeError: 'list' object has no attribute 'revers'. Did you mean: 'reverse'?
l.reverse()
l
[99, 77, 56, 34, 12]
l.sort()
l
[12, 34, 56, 77, 99]
>>> l.sort(reverse=True)
>>> l
[99, 77, 56, 34, 12]
>>> sum(l)
278
>>> l=[1,2,3]
>>> m=[1,2,3]
>>> l
[1, 2, 3]
>>> n=l
>>> n
[1, 2, 3]
>>> n.append(4)
>>> n
[1, 2, 3, 4]
>>> l
[1, 2, 3, 4]
>>> m=l.copy()
>>> m
[1, 2, 3, 4]
>>> m,append(10)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    m,append(10)
NameError: name 'append' is not defined
>>> m.append(10)
>>> m
[1, 2, 3, 4, 10]
>>> l
[1, 2, 3, 4]
>>> 
>>> all([0,'',[],(),set(),{},False])
False
>>> any([0,'',[],(),set(),{},False])
False
>>> all([1,'',[],(),set(),{},False])
False
>>>l.index(4)
l.count(3)
l.count(5)
