'''i=1
while i<=10:
    print(i)
    i+=1'''

'''i=10
while i>0:
    print(i)
    i-=1'''

'''i=2
while i<=100:
    print(i)
  i+=2
'''
#itertae a string using while loop
'''s='reena kowsar'
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1'''

'''l1=[1,0,0,0,3,4,5,6,7,8,9,0,12,0,13,0,0,0,16,0]
while 0 in l1:
    l1.remove(0)
print(l1)'''

'''d={}
t_b=0
while True:
    product=input('enter product name(for exit):')
    if product=='exit':
        break
    price=int(input('enter product price:'))
    t_b +=price
    d[product]=price
print(d)
print('Total bill:',t_b)'''

i=0
while i<10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print('end of the loop')



#8,9,11,14,17,18,20