Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='pythonprogramming'
len(c)
17
ord('p')
112
ord('a')
97
chr('A')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    chr('A')
TypeError: 'str' object cannot be interpreted as an integer
ch(90)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ch(90)
NameError: name 'ch' is not defined. Did you mean: 'c'?
min(c)
'a'
max(c)
'y'
sorted(c)
['a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
ord('0')
48
chr(90)
'Z'
chr(102)
'f'
chr(115)
's'
c="String is immutable"
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize
<built-in method capitalize of str object at 0x0000026B71EE88B0>
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
s.swapcase()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.swapcase()
NameError: name 's' is not defined
c.swapcase()
'sTRING IS IMMUTABLE'
'dfgA@T".casefold()
SyntaxError: unterminated string literal (detected at line 1)
'dfgA@T'.casefold()
'dfga@t'
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
c.ljust(60,'-')
'String is immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------String is immutable'
'12'.zfill(4)
'0012'
c.find('i')
3
c.find('r')
2
c.find('s')
8
c.find('z')
-1
c
'String is immutable'
c.rfind('i')
10
c.count('i')
3
c.count('g')
1
a="reena"
a.count('e')
2
c.replace('i','0')
'Str0ng 0s 0mmutable'
c.replace('string','Float')
'String is immutable'
c.replace('string','Float')
'String is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345')
            )
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
c.split()
['String', 'is', 'immutable']
'String', 'is', 'immutable'.split()
('String', 'is', ['immutable'])
'String', 'is', 'immutable' .split()
('String', 'is', ['immutable'])
'string,is,immutable' .split()
['string,is,immutable']
'string,is,immutable' .rsplit()
['string,is,immutable']
s='''
python
programming
language'''
s
'\npython\nprogramming\nlanguage'
s.splitlines()
['', 'python', 'programming', 'language']
" ".join(['python', 'programming', 'language'])
'python programming language'
"-".join(['python', 'programming', 'language'])
'python-programming-language'
",".join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ",".join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> a=','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a=','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> a=','.join(['1','2','3'])
>>> a
'1,2,3'
>>> s='java','python','c','c++'
>>> s.partition(',')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
>>> s
('java', 'python', 'c', 'c++')
>>> s.partition(',')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
>>> s='java,c,python,c++'
>>> s
'java,c,python,c++'
>>> s.partition(',')
('java', ',', 'c,python,c++')
>>> s.rpartition(',')
('java,c,python', ',', 'c++')
>>> s='          Hello              Hi    '
>>> s.strip()
'Hello              Hi'
>>> s.lstrip()
'Hello              Hi    '
>>> s.rstrip()
'          Hello              Hi'
>>> text="Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
