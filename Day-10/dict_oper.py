Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data={'name':'reena','batch'=63,'course'='PFS'}
SyntaxError: ':' expected after dictionary key
data={'name':'reena','batch':63,'course':'PFS'}
data
{'name': 'reena', 'batch': 63, 'course': 'PFS'}
data['name']
'reena'
data['batch']
63
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=62
data
{'name': 'reena', 'batch': 62, 'course': 'PFS'}
data['skills']=['python','java','mysql','flask']
data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask']}
data['age']=21
data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'age': 21}

data.update({'phno':9876543210,'email':'reena@gmail.com'})
data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'reena@gmail.com'}
data.update({'phno':2345678987654,'email':'reena@gmail.com'})
data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'age': 21, 'phno': 2345678987654, 'email': 'reena@gmail.com'}
>>> data.pop('age')
21
>>> data.pop('phno')
2345678987654
>>> data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'email': 'reena@gmail.com'}
>>> del data['name']
>>> data
{'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'email': 'reena@gmail.com'}
>>> data.popitem()
('email', 'reena@gmail.com')
>>> data
{'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask']}
>>> data
{'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask']}
>>> data.clear()
>>> data
{}
>>> data={'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'age': 21, 'phno': 2345678987654, 'email': 'reena@gmail.com'}
>>> data
{'name': 'reena', 'batch': 62, 'course': 'PFS', 'skills': ['python', 'java', 'mysql', 'flask'], 'age': 21, 'phno': 2345678987654, 'email': 'reena@gmail.com'}
>>> data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
>>> data.values()
dict_values(['reena', 62, 'PFS', ['python', 'java', 'mysql', 'flask'], 21, 2345678987654, 'reena@gmail.com'])
>>> data.items()
dict_items([('name', 'reena'), ('batch', 62), ('course', 'PFS'), ('skills', ['python', 'java', 'mysql', 'flask']), ('age', 21), ('phno', 2345678987654), ('email', 'reena@gmail.com')])
>>> sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
>>> sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
min(data)
data
data['age']
data.setdefault('age',0)
data
data.setdefault(name,' ')
data
s={1:1,2:2}
b=a
b[3]=3
andb
c=a.copy()
c[4]=4
c
a
d=dict.fromkeys(["a","b"],0)
d