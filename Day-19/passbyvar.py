#when we use built in functions they act as varaibles

'''l=[1,2,3,4,5]
max=20
sum=10
print(sum)'''


#int float str list tuple set dict bool

#pass by value:passing a immutable value
#pass by reference :passing mutable items

#int float str tuple bool
#list set dict

'''def display(n):
    n=10
    print('Inside:',n)
n=20
display(n)
print('Outside:',n)'''

'''def display(n):
    n=n+10.5
    print('Inside:',n)
n=20.5
display(n)
print('Outside:',n)'''

'''def display(n):
    n='reena'+n
    print('Inside:',n)
n='kowsar'
display(n)
print('Outside:',n)'''

'''def display(n):
    n=(1,2,3,4)
    print('Inside:',n)
n=(1,2,3,4,5)
display(n)
print('Outside:',n)'''

'''def display(n):
    n='False'
    print('Inside:',n)
n='True'
display(n)
print('Outside:',n)'''

'''def display(n):
    n.append(5)
    print('Inside:',n)
n=[1,2,3]
display(n)
print('Outside:',n)'''

'''def display(n):
    n.add(6)
    print('Inside:',n)
n={1,2,3,4,5}
display(n)
print('Outside:',n)'''

def display(n):
    n[6]=6
    print('Inside:',n)
n={1:2,3:4}
display(n)
print('Outside:',n)