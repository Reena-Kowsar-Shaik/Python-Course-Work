'''n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print(i,end=' ')
    print()'''

n=int(input())
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or  i==n-1):
            print('*',end='')
    print()