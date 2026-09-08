#user details
'''def display(name,email,password):
    print(f'Hello {name}')
    print(f'Your email:{email}')
    print(f'Your password:{password}')
display('reena','reena@gmail.com','reena@123')
display('amani','amani@gmail.com','amani@123')'''

#year is leap year or not
'''def isleapyear(year):
    if year%400 ==0 or (year%4==0 and year%100!=0):
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')
for year in range(2004,2027,2):
    isleapyear(year)'''


#sum of digits
'''def sumofdigits(n):
    sum=0
    while n>0:
        sum+= n%10
        n=n//10
    return sum
n=int(input('enter the number:'))
print(f'sum of {n} digits is {sumofdigits(n)}')
'''
'''#product of digits
def productfdigits(n):
    c=1
    while n>0:
        c *= n%10
        n=n//10
    return c
n=int(input('enter the number:'))
print(f'product of {n} digits is {productfdigits(n)}')'''

'''#password is strong or weak
def checkpassword(password):
    if len(password) > 8:
        check=set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check)==4:
            return "Strong Password"
    return "Weak Password"
password=input("enter password:")
print(f"password is {checkpassword(password)}")'''


#1 to 20 tables
def table(n):
    print(f'--------Table - {n}------------')
    for i in range(1,11):
        print(f'{n} * {i} ={n*i}')
for i in range(1,21):
    table(i)




