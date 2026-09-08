'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and j>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or (j==0 and i<m) or(j==n-1 and i>m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0  or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input('enter the size:'))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0  and i<m) or (j==n-1 and i<m) or (i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

(i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print('*',end=' ')









