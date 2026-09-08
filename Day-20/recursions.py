#printing 1 to 10
'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)'''

#printing 10 to1

'''def display(n):
    if n==0:
        return
    print(n)
    display(n-1)

display(10)'''

#printing 10 t0 1
'''def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)'''

'''#sum of n numbers
def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(5))'''

'''#product of n numbers
def displayproduct(n):
    if n==1:
        return 1
    return n * displayproduct(n-1)
print(displayproduct(5))'''

#display string indexes

'''def display(ind):
    if ind==len(s):
        return 
    print(s[ind],end=' ')
    display(ind+1)
s='python programming'
display(0)
'''

'''#display in reverse order
def display(ind):
    if ind==len(s):
        return 
    display(ind+1)
    print(s[ind],end=' ')
s='python programming'
display(0)'''

'p'
'py'
'pyt'
'pyth'
'python'


#print like pattern
'''def display(n):
    if n >len(s):
        return
    print(s[:n])
    display(n+1)
s='python'
display(1)'''

'''python programming
pytho
ython
thon 
hon p
'''
'''def pattern(ind,wid):
    if ind >len(s)-wid:
        return
    print(s[ind:ind+wid])
    pattern(ind+1,wid)

s='python programming'
pattern(ind=int(input('enter index')),wid=int(input('enter width')))
'''
'''#n=98765
def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
display(98765)'''

#n=98765 sum
'''def display(n):
    if n==0:
        return 0
    return n%10 + display(n//10)
n=int(input())
print(display(n))'''

#fibnoaaci series

def fib(n,a=0,b=1):
  if n==0:
    return
  print(a,end=" ")
  fib(n-1,b,a+b)
fib(10)
  
