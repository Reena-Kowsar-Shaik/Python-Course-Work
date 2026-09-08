'''s='Python Programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
'''
'''
l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)'''

'''nt(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")'''

'''data={}
n=int(input("enter no of students:"))
max_marks=0
for i in range(n):
    name=input("entre name:")
    marks=int(input("enter marks"))
    data[name]=marks
    if marks > max_marks:
        max_marks=marks
print(data)
print("Maximum Marks:",max_marks)'''

products={}
t_bill=0
n=int(input("no of prodocts"))
for i in range(1,n+1):
    product=input(f"product-{i}:")
    price=int(input(f"product-{i}:"))
    quantity=int(input(f"product-{i}:"))
    f_p=price*quantity
    t_bill+=f_p
    products[product]=f'{price} * {quantity} * {f_p}'
print(products)
print("Total bill:",t_bill)




