#variable declared outside of function is gloabal variable

'''def display(n):
    n=n+10
    print('Inside:',n)
n=10
display(n)
print('Outside:',n)

def display():
    print('Inside:',n)'''

'''def display():
    print('Inside:',n)
n=10
display()
print('Outside:',n)'''

'''def display():
    n=10
    print('Inside:',n)

display()
print('Outside:',n)'''

'''def display():
    global n
    n=n+10
    print('Inside:',n)
n=10
display()
print('Outside:',n) '''

'''def display():
    global n
    n='PFS'
    print('Updated Course:',n)
n='JFS'
display()
print("Final Course:",n)'''

def display():
    n='JFS'
    def update():
        nonlocal n
        n='PFS'
        print('Updated Course:',n)
    update()
    print('Final Course:',n)
display()