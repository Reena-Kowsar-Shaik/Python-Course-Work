#a small function without function name used to perform simple task
#lambda arguments : expression

#greatest of numbers

'''greater = lambda a,b:a if a > b else b
print(greater(12,13))
print(greater(50,100))
print(greater(200,70))

wish=lambda name : f'welcome to the course: {name}'
print(wish('reena'))
print(wish('kowsar'))

iseven = lambda n: "Even" if n%2==0 else "odd"
print(iseven(44))
print(iseven(18))
print(iseven(51))

avg=lambda a,b,c :(a+b+c)/3
print(avg(4,5,6))
print(avg(30,26,15))'''

'''domain= lambda mail : (mail.split('@')[-1]).split('.')[0]
print(domain('reena@codegnan.com'))
print(domain('reena@gmail.com'))
'''

'''gst = lambda price : price + price * 0.18
print(gst(1000))
print(gst(5000))
print(gst(8000))'''

'''prices=[5678,8765,567,124,123,1600,3000]
res=list(map(lambda price : price + price * 0.18 , prices))
print(res)'''

'''names=['reena','kowsar','amani','nandu']
res=list(map(lambda name: name.title(),names))
print(res)'''

'''prices=[1234,345,367,987,654,432]
res=list(map(lambda price : price - price*0.30 ,prices))
print(res)'''

'''prices=[1234,5345,367,6987,654,432]
res=list(filter(lambda price : price%2!=0 ,prices))
print(res)'''

''''names={'reena','kowsar','rafiya'}
res=list(filter(lambda name :len(name) >5 , names))
print(res)

#reduce():reduce into a single unit
from functools import reduce
l=[3,567,6,24,124,435,462]
res=reduce(lambda sum,i:sum+i,l)
print(res)

names={'reena','kowsar','rafiya'}
res=reduce(lambda res,i:res+''+i,names)
print(res)'''

products={'sugar':60,
          'salt':50,
          'eggs':120,
          'bread':100,
          'cooking oil':180}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))