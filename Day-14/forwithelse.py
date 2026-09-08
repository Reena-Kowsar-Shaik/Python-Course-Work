'''for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print('end of the loop')
 '''

'''pin=1234
for _ in range(5):
    epin=int(input('enter a pin'))
    if pin == epin:
        print('unlock phone')
        break
    else:
        print('Invalid pin')
else:
    print('Try again aftersome time')'''

'''n=int(input('enter a number'))
print('Factors of a Number:')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')'''

'''n=int(input('enter a number'))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print('print prime number')
else:
    print('not a prime number ')'''

n=int(input('enter a number'))
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime number')
        break
else:
    print('prime number')
