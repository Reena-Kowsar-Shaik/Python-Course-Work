#instead of resturn we are using yeild keyword
#to call varaiable we use next
'''def retrivedata():
    data=['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i
reels=retrivedata()
while True:
    status=input("[s]croll or [q]uit:")
    if status=='s':
        print(next(reels))
    else:
        break'''

'''#even numbers generation
def even():
    i=0
    while True:
        i+=2
        yield i
n=5
res=even()
for i in range(n):
    print(next(res))'''
'''
def fac(n):
    for i in range(1,n+1):
        if n%i==0:
            yield(i)

n=50            
res = fac(n)
for i in res:
    print(i)

'''

#primenumbers
'''def isprime(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True

def primes(n):
    for i in range(2,n+1):
        if isprime(i):
            yield(i)
    

n=50            
res = primes(n)
for i in res:
    print(i)'''

def count(n):
    for i in range(n,0,-1):
        yield(i)
n=10
res=count(n)
for i in range(n):
    print(next(res))


