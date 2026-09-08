'''#list comprehension:simple and easy way to create list in one line of code using for loop

syntax:
l=[updating for loop]
l=[updating for loop if cond]
l=[upd1 if cond else upd2 for loop]
l=[upd for loop1 for loop2]
l=[updfor loop1 for loop2 if cond]

#printing numbers from 1 t0 11
res=[i for i in range(1,11)]
print(res)

#factors of n
n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

#even append number odd append 0
r=[12,34,5567,8765,23,22,11,10]
res=[i if i%2==0 else 0 for i in r]
print(res)

#even numbers in nested list
r=[[12,23,45],[687,34,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)'''

'''#for set comprehension use curly braces
s=[1,2,3,4,5,6,4,3,2,1]
res={i for i in s}
print(res)'''

'''res=[int(input(f"enter the number-{i+1}:")) for i in range(10)]
print(res)'''
'''
res=[input(f"enter then name-{i+1}") for i in range(5)]
print(res)'''

''''
names={input(f"enter a name-{i+1}: "):int(input("enter the marks:")) for i in range(5)}
print(names)'''

numbers={i:i*i for i in range(1,11)}
print(numbers)